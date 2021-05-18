from modelsori import *
from utils.utils import *
import numpy as np
from copy import deepcopy
from test import test
from terminaltables import AsciiTable
import time
from utils.prune_utils import *
import argparse
import torchvision

def copy_conv(conv_src,conv_dst):
    conv_dst[0] = conv_src.conv
    conv_dst[1] = conv_src.bn
    conv_dst[2] = conv_src.act

def copy_weight_lv4(modelyolov5,model):
    focus = list(modelyolov5.model.children())[0]
    copy_conv(focus.conv, model.module_list[1])

    conv1 = list(modelyolov5.model.children())[1]
    copy_conv(conv1, model.module_list[2])

    cspnet1 = list(modelyolov5.model.children())[2]
    copy_conv(cspnet1.cv2, model.module_list[3])
    copy_conv(cspnet1.cv1, model.module_list[5])
    copy_conv(cspnet1.m[0].cv1, model.module_list[6])
    copy_conv(cspnet1.m[0].cv2, model.module_list[7])
    copy_conv(cspnet1.m[1].cv1, model.module_list[9])
    copy_conv(cspnet1.m[1].cv2, model.module_list[10])
    copy_conv(cspnet1.m[2].cv1, model.module_list[12])
    copy_conv(cspnet1.m[2].cv2, model.module_list[13])
    copy_conv(cspnet1.cv3, model.module_list[16])

    conv2 = list(modelyolov5.model.children())[3]
    copy_conv(conv2, model.module_list[17])

    cspnet2 = list(modelyolov5.model.children())[4]
    copy_conv(cspnet2.cv2, model.module_list[18])
    copy_conv(cspnet2.cv1, model.module_list[20])
    copy_conv(cspnet2.m[0].cv1, model.module_list[21])
    copy_conv(cspnet2.m[0].cv2, model.module_list[22])
    copy_conv(cspnet2.m[1].cv1, model.module_list[24])
    copy_conv(cspnet2.m[1].cv2, model.module_list[25])
    copy_conv(cspnet2.m[2].cv1, model.module_list[27])
    copy_conv(cspnet2.m[2].cv2, model.module_list[28])
    copy_conv(cspnet2.m[3].cv1, model.module_list[30])
    copy_conv(cspnet2.m[3].cv2, model.module_list[31])
    copy_conv(cspnet2.m[4].cv1, model.module_list[33])
    copy_conv(cspnet2.m[4].cv2, model.module_list[34])
    copy_conv(cspnet2.m[5].cv1, model.module_list[36])
    copy_conv(cspnet2.m[5].cv2, model.module_list[37])
    copy_conv(cspnet2.m[6].cv1, model.module_list[39])
    copy_conv(cspnet2.m[6].cv2, model.module_list[40])
    copy_conv(cspnet2.m[7].cv1, model.module_list[42])
    copy_conv(cspnet2.m[7].cv2, model.module_list[43])
    copy_conv(cspnet2.m[8].cv1, model.module_list[45])
    copy_conv(cspnet2.m[8].cv2, model.module_list[46])
    copy_conv(cspnet2.cv3, model.module_list[49])

    conv3 = list(modelyolov5.model.children())[5]
    copy_conv(conv3, model.module_list[50])

    cspnet3 = list(modelyolov5.model.children())[6]
    copy_conv(cspnet3.cv2, model.module_list[51])
    copy_conv(cspnet3.cv1, model.module_list[53])
    copy_conv(cspnet3.m[0].cv1, model.module_list[54])
    copy_conv(cspnet3.m[0].cv2, model.module_list[55])
    copy_conv(cspnet3.m[1].cv1, model.module_list[57])
    copy_conv(cspnet3.m[1].cv2, model.module_list[58])
    copy_conv(cspnet3.m[2].cv1, model.module_list[60])
    copy_conv(cspnet3.m[2].cv2, model.module_list[61])
    copy_conv(cspnet3.m[3].cv1, model.module_list[63])
    copy_conv(cspnet3.m[3].cv2, model.module_list[64])
    copy_conv(cspnet3.m[4].cv1, model.module_list[66])
    copy_conv(cspnet3.m[4].cv2, model.module_list[67])
    copy_conv(cspnet3.m[5].cv1, model.module_list[69])
    copy_conv(cspnet3.m[5].cv2, model.module_list[70])
    copy_conv(cspnet3.m[6].cv1, model.module_list[72])
    copy_conv(cspnet3.m[6].cv2, model.module_list[73])
    copy_conv(cspnet3.m[7].cv1, model.module_list[75])
    copy_conv(cspnet3.m[7].cv2, model.module_list[76])
    copy_conv(cspnet3.m[8].cv1, model.module_list[78])
    copy_conv(cspnet3.m[8].cv2, model.module_list[79])
    copy_conv(cspnet3.cv3, model.module_list[82])

    conv4 = list(modelyolov5.model.children())[7]
    copy_conv(conv4, model.module_list[83])

    spp = list(modelyolov5.model.children())[8]
    copy_conv(spp.cv1, model.module_list[84])
    model.module_list[85] = spp.m[0]
    model.module_list[87] = spp.m[1]
    model.module_list[89] = spp.m[2]
    copy_conv(spp.cv2, model.module_list[91])

    cspnet4 = list(modelyolov5.model.children())[9]
    copy_conv(cspnet4.cv2, model.module_list[92])
    copy_conv(cspnet4.cv1, model.module_list[94])
    copy_conv(cspnet4.m[0].cv1, model.module_list[95])
    copy_conv(cspnet4.m[0].cv2, model.module_list[96])
    copy_conv(cspnet4.m[1].cv1, model.module_list[97])
    copy_conv(cspnet4.m[1].cv2, model.module_list[98])
    copy_conv(cspnet4.m[2].cv1, model.module_list[99])
    copy_conv(cspnet4.m[2].cv2, model.module_list[100])
    copy_conv(cspnet4.cv3, model.module_list[102])

    conv5 = list(modelyolov5.model.children())[10]
    copy_conv(conv5, model.module_list[103])

    upsample1 = list(modelyolov5.model.children())[11]
    model.module_list[104] = upsample1

    cspnet5 = list(modelyolov5.model.children())[13]
    copy_conv(cspnet5.cv2, model.module_list[106])
    copy_conv(cspnet5.cv1, model.module_list[108])
    copy_conv(cspnet5.m[0].cv1, model.module_list[109])
    copy_conv(cspnet5.m[0].cv2, model.module_list[110])
    copy_conv(cspnet5.m[1].cv1, model.module_list[111])
    copy_conv(cspnet5.m[1].cv2, model.module_list[112])
    copy_conv(cspnet5.m[2].cv1, model.module_list[113])
    copy_conv(cspnet5.m[2].cv2, model.module_list[114])
    copy_conv(cspnet5.cv3, model.module_list[116])

    conv6 = list(modelyolov5.model.children())[14]
    copy_conv(conv6, model.module_list[117])

    upsample2 = list(modelyolov5.model.children())[15]
    model.module_list[118] = upsample2

    cspnet6 = list(modelyolov5.model.children())[17]
    copy_conv(cspnet6.cv2, model.module_list[120])
    copy_conv(cspnet6.cv1, model.module_list[122])
    copy_conv(cspnet6.m[0].cv1, model.module_list[123])
    copy_conv(cspnet6.m[0].cv2, model.module_list[124])
    copy_conv(cspnet6.m[1].cv1, model.module_list[125])
    copy_conv(cspnet6.m[1].cv2, model.module_list[126])
    copy_conv(cspnet6.m[2].cv1, model.module_list[127])
    copy_conv(cspnet6.m[2].cv2, model.module_list[128])
    copy_conv(cspnet6.cv3, model.module_list[130])

    conv7 = list(modelyolov5.model.children())[18]
    copy_conv(conv7, model.module_list[134])

    cspnet7 = list(modelyolov5.model.children())[20]
    copy_conv(cspnet7.cv2, model.module_list[136])
    copy_conv(cspnet7.cv1, model.module_list[138])
    copy_conv(cspnet7.m[0].cv1, model.module_list[139])
    copy_conv(cspnet7.m[0].cv2, model.module_list[140])
    copy_conv(cspnet7.m[1].cv1, model.module_list[141])
    copy_conv(cspnet7.m[1].cv2, model.module_list[142])
    copy_conv(cspnet7.m[2].cv1, model.module_list[143])
    copy_conv(cspnet7.m[2].cv2, model.module_list[144])
    copy_conv(cspnet7.cv3, model.module_list[146])

    conv8 = list(modelyolov5.model.children())[21]
    copy_conv(conv8, model.module_list[150])

    cspnet8 = list(modelyolov5.model.children())[23]
    copy_conv(cspnet8.cv2, model.module_list[152])
    copy_conv(cspnet8.cv1, model.module_list[154])
    copy_conv(cspnet8.m[0].cv1, model.module_list[155])
    copy_conv(cspnet8.m[0].cv2, model.module_list[156])
    copy_conv(cspnet8.m[1].cv1, model.module_list[157])
    copy_conv(cspnet8.m[1].cv2, model.module_list[158])
    copy_conv(cspnet8.m[2].cv1, model.module_list[159])
    copy_conv(cspnet8.m[2].cv2, model.module_list[160])
    copy_conv(cspnet8.cv3, model.module_list[162])

    detect = list(modelyolov5.model.children())[24]
    model.module_list[131][0] = detect.m[0]
    model.module_list[147][0] = detect.m[1]
    model.module_list[163][0] = detect.m[2]

def copy_weight_sv4(modelyolov5,model):
    focus = list(modelyolov5.model.children())[0]
    copy_conv(focus.conv, model.module_list[1])
    conv1 = list(modelyolov5.model.children())[1]
    copy_conv(conv1, model.module_list[2])
    cspnet1 = list(modelyolov5.model.children())[2]
    copy_conv(cspnet1.cv2, model.module_list[3])
    copy_conv(cspnet1.cv1, model.module_list[5])
    copy_conv(cspnet1.m[0].cv1, model.module_list[6])
    copy_conv(cspnet1.m[0].cv2, model.module_list[7])
    copy_conv(cspnet1.cv3, model.module_list[10])
    conv2 = list(modelyolov5.model.children())[3]
    copy_conv(conv2, model.module_list[11])
    cspnet2 = list(modelyolov5.model.children())[4]
    copy_conv(cspnet2.cv2, model.module_list[12])
    copy_conv(cspnet2.cv1, model.module_list[14])
    copy_conv(cspnet2.m[0].cv1, model.module_list[15])
    copy_conv(cspnet2.m[0].cv2, model.module_list[16])
    copy_conv(cspnet2.m[1].cv1, model.module_list[18])
    copy_conv(cspnet2.m[1].cv2, model.module_list[19])
    copy_conv(cspnet2.m[2].cv1, model.module_list[21])
    copy_conv(cspnet2.m[2].cv2, model.module_list[22])
    copy_conv(cspnet2.cv3, model.module_list[25])
    conv3 = list(modelyolov5.model.children())[5]
    copy_conv(conv3, model.module_list[26])
    cspnet3 = list(modelyolov5.model.children())[6]
    copy_conv(cspnet3.cv2, model.module_list[27])
    copy_conv(cspnet3.cv1, model.module_list[29])
    copy_conv(cspnet3.m[0].cv1, model.module_list[30])
    copy_conv(cspnet3.m[0].cv2, model.module_list[31])
    copy_conv(cspnet3.m[1].cv1, model.module_list[33])
    copy_conv(cspnet3.m[1].cv2, model.module_list[34])
    copy_conv(cspnet3.m[2].cv1, model.module_list[36])
    copy_conv(cspnet3.m[2].cv2, model.module_list[37])
    copy_conv(cspnet3.cv3, model.module_list[40])
    conv4 = list(modelyolov5.model.children())[7]
    copy_conv(conv4, model.module_list[41])
    spp = list(modelyolov5.model.children())[8]
    copy_conv(spp.cv1, model.module_list[42])
    model.module_list[43] = spp.m[0]
    model.module_list[45] = spp.m[1]
    model.module_list[47] = spp.m[2]
    copy_conv(spp.cv2, model.module_list[49])
    cspnet4 = list(modelyolov5.model.children())[9]
    copy_conv(cspnet4.cv2, model.module_list[50])
    copy_conv(cspnet4.cv1, model.module_list[52])
    copy_conv(cspnet4.m[0].cv1, model.module_list[53])
    copy_conv(cspnet4.m[0].cv2, model.module_list[54])
    copy_conv(cspnet4.cv3, model.module_list[56])
    conv5 = list(modelyolov5.model.children())[10]
    copy_conv(conv5, model.module_list[57])
    upsample1 = list(modelyolov5.model.children())[11]
    model.module_list[58] = upsample1
    cspnet5 = list(modelyolov5.model.children())[13]
    copy_conv(cspnet5.cv2, model.module_list[60])
    copy_conv(cspnet5.cv1, model.module_list[62])
    copy_conv(cspnet5.m[0].cv1, model.module_list[63])
    copy_conv(cspnet5.m[0].cv2, model.module_list[64])
    copy_conv(cspnet5.cv3, model.module_list[66])
    conv6 = list(modelyolov5.model.children())[14]
    copy_conv(conv6, model.module_list[67])
    upsample2 = list(modelyolov5.model.children())[15]
    model.module_list[68] = upsample2
    cspnet6 = list(modelyolov5.model.children())[17]
    copy_conv(cspnet6.cv2, model.module_list[70])
    copy_conv(cspnet6.cv1, model.module_list[72])
    copy_conv(cspnet6.m[0].cv1, model.module_list[73])
    copy_conv(cspnet6.m[0].cv2, model.module_list[74])
    copy_conv(cspnet6.cv3, model.module_list[76])
    conv7 = list(modelyolov5.model.children())[18]
    copy_conv(conv7, model.module_list[80])
    cspnet7 = list(modelyolov5.model.children())[20]
    copy_conv(cspnet7.cv2, model.module_list[82])
    copy_conv(cspnet7.cv1, model.module_list[84])
    copy_conv(cspnet7.m[0].cv1, model.module_list[85])
    copy_conv(cspnet7.m[0].cv2, model.module_list[86])
    copy_conv(cspnet7.cv3, model.module_list[88])
    conv8 = list(modelyolov5.model.children())[21]
    copy_conv(conv8, model.module_list[92])
    cspnet8 = list(modelyolov5.model.children())[23]
    copy_conv(cspnet8.cv2, model.module_list[94])
    copy_conv(cspnet8.cv1, model.module_list[96])
    copy_conv(cspnet8.m[0].cv1, model.module_list[97])
    copy_conv(cspnet8.m[0].cv2, model.module_list[98])
    copy_conv(cspnet8.cv3, model.module_list[100])
    detect = list(modelyolov5.model.children())[24]
    model.module_list[77][0] = detect.m[0]
    model.module_list[89][0] = detect.m[1]
    model.module_list[101][0] = detect.m[2]

def copy_weight(modelyolov5,model):
    focus = list(modelyolov5.model.children())[0]
    model.module_list[1][0] = focus.conv.conv
    model.module_list[1][1] = focus.conv.bn
    model.module_list[1][2] = focus.conv.act
    conv1 = list(modelyolov5.model.children())[1]
    model.module_list[2][0] = conv1.conv
    model.module_list[2][1] = conv1.bn
    model.module_list[2][2] = conv1.act
    cspnet1 = list(modelyolov5.model.children())[2]
    model.module_list[3][0] = cspnet1.cv2
    model.module_list[5][0] = cspnet1.cv1.conv
    model.module_list[5][1] = cspnet1.cv1.bn
    model.module_list[5][2] = cspnet1.cv1.act
    model.module_list[9][0] = cspnet1.cv3
    model.module_list[11][0] = cspnet1.bn
    model.module_list[11][1] = cspnet1.act
    model.module_list[6][0] = cspnet1.m[0].cv1.conv
    model.module_list[6][1] = cspnet1.m[0].cv1.bn
    model.module_list[6][2] = cspnet1.m[0].cv1.act
    model.module_list[7][0] = cspnet1.m[0].cv2.conv
    model.module_list[7][1] = cspnet1.m[0].cv2.bn
    model.module_list[7][2] = cspnet1.m[0].cv2.act
    model.module_list[12][0] = cspnet1.cv4.conv
    model.module_list[12][1] = cspnet1.cv4.bn
    model.module_list[12][2] = cspnet1.cv4.act
    conv2 = list(modelyolov5.model.children())[3]
    model.module_list[13][0] = conv2.conv
    model.module_list[13][1] = conv2.bn
    model.module_list[13][2] = conv2.act
    cspnet2 = list(modelyolov5.model.children())[4]
    model.module_list[14][0] = cspnet2.cv2
    model.module_list[16][0] = cspnet2.cv1.conv
    model.module_list[16][1] = cspnet2.cv1.bn
    model.module_list[16][2] = cspnet2.cv1.act
    model.module_list[26][0] = cspnet2.cv3
    model.module_list[28][0] = cspnet2.bn
    model.module_list[28][1] = cspnet2.act
    model.module_list[29][0] = cspnet2.cv4.conv
    model.module_list[29][1] = cspnet2.cv4.bn
    model.module_list[29][2] = cspnet2.cv4.act
    model.module_list[17][0] = cspnet2.m[0].cv1.conv
    model.module_list[17][1] = cspnet2.m[0].cv1.bn
    model.module_list[17][2] = cspnet2.m[0].cv1.act
    model.module_list[18][0] = cspnet2.m[0].cv2.conv
    model.module_list[18][1] = cspnet2.m[0].cv2.bn
    model.module_list[18][2] = cspnet2.m[0].cv2.act
    model.module_list[20][0] = cspnet2.m[1].cv1.conv
    model.module_list[20][1] = cspnet2.m[1].cv1.bn
    model.module_list[20][2] = cspnet2.m[1].cv1.act
    model.module_list[21][0] = cspnet2.m[1].cv2.conv
    model.module_list[21][1] = cspnet2.m[1].cv2.bn
    model.module_list[21][2] = cspnet2.m[1].cv2.act
    model.module_list[23][0] = cspnet2.m[2].cv1.conv
    model.module_list[23][1] = cspnet2.m[2].cv1.bn
    model.module_list[23][2] = cspnet2.m[2].cv1.act
    model.module_list[24][0] = cspnet2.m[2].cv2.conv
    model.module_list[24][1] = cspnet2.m[2].cv2.bn
    model.module_list[24][2] = cspnet2.m[2].cv2.act
    conv3 = list(modelyolov5.model.children())[5]
    model.module_list[30][0] = conv3.conv
    model.module_list[30][1] = conv3.bn
    model.module_list[30][2] = conv3.act
    cspnet3 = list(modelyolov5.model.children())[6]
    model.module_list[31][0] = cspnet3.cv2
    model.module_list[33][0] = cspnet3.cv1.conv
    model.module_list[33][1] = cspnet3.cv1.bn
    model.module_list[33][2] = cspnet3.cv1.act
    model.module_list[43][0] = cspnet3.cv3
    model.module_list[45][0] = cspnet3.bn
    model.module_list[45][1] = cspnet3.act
    model.module_list[46][0] = cspnet3.cv4.conv
    model.module_list[46][1] = cspnet3.cv4.bn
    model.module_list[46][2] = cspnet3.cv4.act
    model.module_list[34][0] = cspnet3.m[0].cv1.conv
    model.module_list[34][1] = cspnet3.m[0].cv1.bn
    model.module_list[34][2] = cspnet3.m[0].cv1.act
    model.module_list[35][0] = cspnet3.m[0].cv2.conv
    model.module_list[35][1] = cspnet3.m[0].cv2.bn
    model.module_list[35][2] = cspnet3.m[0].cv2.act
    model.module_list[37][0] = cspnet3.m[1].cv1.conv
    model.module_list[37][1] = cspnet3.m[1].cv1.bn
    model.module_list[37][2] = cspnet3.m[1].cv1.act
    model.module_list[38][0] = cspnet3.m[1].cv2.conv
    model.module_list[38][1] = cspnet3.m[1].cv2.bn
    model.module_list[38][2] = cspnet3.m[1].cv2.act
    model.module_list[40][0] = cspnet3.m[2].cv1.conv
    model.module_list[40][1] = cspnet3.m[2].cv1.bn
    model.module_list[40][2] = cspnet3.m[2].cv1.act
    model.module_list[41][0] = cspnet3.m[2].cv2.conv
    model.module_list[41][1] = cspnet3.m[2].cv2.bn
    model.module_list[41][2] = cspnet3.m[2].cv2.act
    conv4 = list(modelyolov5.model.children())[7]
    model.module_list[47][0] = conv4.conv
    model.module_list[47][1] = conv4.bn
    model.module_list[47][2] = conv4.act
    spp = list(modelyolov5.model.children())[8]
    model.module_list[48][0] = spp.cv1.conv
    model.module_list[48][1] = spp.cv1.bn
    model.module_list[48][2] = spp.cv1.act
    model.module_list[49] = spp.m[0]
    model.module_list[51] = spp.m[1]
    model.module_list[53] = spp.m[2]
    model.module_list[55][0] = spp.cv2.conv
    model.module_list[55][1] = spp.cv2.bn
    model.module_list[55][2] = spp.cv2.act
    cspnet4 = list(modelyolov5.model.children())[9]
    model.module_list[56][0] = cspnet4.cv2
    model.module_list[58][0] = cspnet4.cv1.conv
    model.module_list[58][1] = cspnet4.cv1.bn
    model.module_list[58][2] = cspnet4.cv1.act
    model.module_list[61][0] = cspnet4.cv3
    model.module_list[63][0] = cspnet4.bn
    model.module_list[63][1] = cspnet4.act
    model.module_list[64][0] = cspnet4.cv4.conv
    model.module_list[64][1] = cspnet4.cv4.bn
    model.module_list[64][2] = cspnet4.cv4.act
    model.module_list[59][0] = cspnet4.m[0].cv1.conv
    model.module_list[59][1] = cspnet4.m[0].cv1.bn
    model.module_list[59][2] = cspnet4.m[0].cv1.act
    model.module_list[60][0] = cspnet4.m[0].cv2.conv
    model.module_list[60][1] = cspnet4.m[0].cv2.bn
    model.module_list[60][2] = cspnet4.m[0].cv2.act
    conv5 = list(modelyolov5.model.children())[10]
    model.module_list[65][0] = conv5.conv
    model.module_list[65][1] = conv5.bn
    model.module_list[65][2] = conv5.act
    upsample1 = list(modelyolov5.model.children())[11]
    model.module_list[66] = upsample1
    cspnet5 = list(modelyolov5.model.children())[13]
    model.module_list[68][0] = cspnet5.cv2
    model.module_list[70][0] = cspnet5.cv1.conv
    model.module_list[70][1] = cspnet5.cv1.bn
    model.module_list[70][2] = cspnet5.cv1.act
    model.module_list[73][0] = cspnet5.cv3
    model.module_list[75][0] = cspnet5.bn
    model.module_list[75][1] = cspnet5.act
    model.module_list[76][0] = cspnet5.cv4.conv
    model.module_list[76][1] = cspnet5.cv4.bn
    model.module_list[76][2] = cspnet5.cv4.act
    model.module_list[71][0] = cspnet5.m[0].cv1.conv
    model.module_list[71][1] = cspnet5.m[0].cv1.bn
    model.module_list[71][2] = cspnet5.m[0].cv1.act
    model.module_list[72][0] = cspnet5.m[0].cv2.conv
    model.module_list[72][1] = cspnet5.m[0].cv2.bn
    model.module_list[72][2] = cspnet5.m[0].cv2.act
    conv6 = list(modelyolov5.model.children())[14]
    model.module_list[77][0] = conv6.conv
    model.module_list[77][1] = conv6.bn
    model.module_list[77][2] = conv6.act
    upsample2 = list(modelyolov5.model.children())[15]
    model.module_list[78] = upsample2
    cspnet6 = list(modelyolov5.model.children())[17]
    model.module_list[80][0] = cspnet6.cv2
    model.module_list[82][0] = cspnet6.cv1.conv
    model.module_list[82][1] = cspnet6.cv1.bn
    model.module_list[82][2] = cspnet6.cv1.act
    model.module_list[85][0] = cspnet6.cv3
    model.module_list[87][0] = cspnet6.bn
    model.module_list[87][1] = cspnet6.act
    model.module_list[88][0] = cspnet6.cv4.conv
    model.module_list[88][1] = cspnet6.cv4.bn
    model.module_list[88][2] = cspnet6.cv4.act
    model.module_list[83][0] = cspnet6.m[0].cv1.conv
    model.module_list[83][1] = cspnet6.m[0].cv1.bn
    model.module_list[83][2] = cspnet6.m[0].cv1.act
    model.module_list[84][0] = cspnet6.m[0].cv2.conv
    model.module_list[84][1] = cspnet6.m[0].cv2.bn
    model.module_list[84][2] = cspnet6.m[0].cv2.act
    conv7 = list(modelyolov5.model.children())[18]
    model.module_list[92][0] = conv7.conv
    model.module_list[92][1] = conv7.bn
    model.module_list[92][2] = conv7.act
    cspnet7 = list(modelyolov5.model.children())[20]
    model.module_list[94][0] = cspnet7.cv2
    model.module_list[96][0] = cspnet7.cv1.conv
    model.module_list[96][1] = cspnet7.cv1.bn
    model.module_list[96][2] = cspnet7.cv1.act
    model.module_list[99][0] = cspnet7.cv3
    model.module_list[101][0] = cspnet7.bn
    model.module_list[101][1] = cspnet7.act
    model.module_list[102][0] = cspnet7.cv4.conv
    model.module_list[102][1] = cspnet7.cv4.bn
    model.module_list[102][2] = cspnet7.cv4.act
    model.module_list[97][0] = cspnet7.m[0].cv1.conv
    model.module_list[97][1] = cspnet7.m[0].cv1.bn
    model.module_list[97][2] = cspnet7.m[0].cv1.act
    model.module_list[98][0] = cspnet7.m[0].cv2.conv
    model.module_list[98][1] = cspnet7.m[0].cv2.bn
    model.module_list[98][2] = cspnet7.m[0].cv2.act
    conv8 = list(modelyolov5.model.children())[21]
    model.module_list[106][0] = conv8.conv
    model.module_list[106][1] = conv8.bn
    model.module_list[106][2] = conv8.act
    cspnet8 = list(modelyolov5.model.children())[23]
    model.module_list[108][0] = cspnet8.cv2
    model.module_list[110][0] = cspnet8.cv1.conv
    model.module_list[110][1] = cspnet8.cv1.bn
    model.module_list[110][2] = cspnet8.cv1.act
    model.module_list[113][0] = cspnet8.cv3
    model.module_list[115][0] = cspnet8.bn
    model.module_list[115][1] = cspnet8.act
    model.module_list[116][0] = cspnet8.cv4.conv
    model.module_list[116][1] = cspnet8.cv4.bn
    model.module_list[116][2] = cspnet8.cv4.act
    model.module_list[111][0] = cspnet8.m[0].cv1.conv
    model.module_list[111][1] = cspnet8.m[0].cv1.bn
    model.module_list[111][2] = cspnet8.m[0].cv1.act
    model.module_list[112][0] = cspnet8.m[0].cv2.conv
    model.module_list[112][1] = cspnet8.m[0].cv2.bn
    model.module_list[112][2] = cspnet8.m[0].cv2.act
    detect = list(modelyolov5.model.children())[24]
    model.module_list[89][0] = detect.m[0]
    model.module_list[103][0] = detect.m[1]
    model.module_list[117][0] = detect.m[2]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--cfg', type=str, default='cfg/yolov5l_v4.cfg', help='cfg file path')
    parser.add_argument('--data', type=str, default='data/goods.data', help='*.data file path')
    parser.add_argument('--weights', type=str, default='weight/last.pt', help='sparse model weights')
    parser.add_argument('--global_percent', type=float, default=0.7, help='global channel prune percent')
    parser.add_argument('--layer_keep', type=float, default=0.1, help='channel keep percent per layer')
    parser.add_argument('--img_size', type=int, default=416, help='inference size (pixels)')
    opt = parser.parse_args()
    print(opt)

    img_size = opt.img_size
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = Darknet(opt.cfg, (img_size, img_size)).to(device)

    modelyolov5 = torch.load(opt.weights, map_location=device)['model'].float()  # load FP32 model
    YOLOV5_V4=True
    if YOLOV5_V4:
        #yolov5-v4
        copy_weight_lv4(modelyolov5, model)
    else:
        #yolov5-v3 yolov5-v2
        copy_weight(modelyolov5, model)

    eval_model = lambda model:test(model=model,cfg=opt.cfg, data=opt.data, batch_size=50, img_size=img_size, conf_thres=0.35)
    obtain_num_parameters = lambda model:sum([param.nelement() for param in model.parameters()])

    print("\nlet's test the original model first:")
    with torch.no_grad():
        origin_model_metric = eval_model(model)
    origin_nparameters = obtain_num_parameters(model)

    CBL_idx, Conv_idx, prune_idx, _, _= parse_module_defs2(model.module_defs)



    bn_weights = gather_bn_weights(model.module_list, prune_idx)

    sorted_bn = torch.sort(bn_weights)[0]
    sorted_bn, sorted_index = torch.sort(bn_weights)
    thresh_index = int(len(bn_weights) * opt.global_percent)
    thresh = sorted_bn[thresh_index].cuda()

    print(f'Global Threshold should be less than {thresh:.4f}.')

    #%%
    def obtain_filters_mask(model, thre, CBL_idx, prune_idx):

        pruned = 0
        total = 0
        num_filters = []
        filters_mask = []
        for idx in CBL_idx:
            # bn_module = model.module_list[idx][1]
            bn_module = model.module_list[idx][1] if type(
                model.module_list[idx][1]).__name__ == 'BatchNorm2d' else model.module_list[idx][0]
            if idx in prune_idx:

                weight_copy = bn_module.weight.data.abs().clone()

                if model.module_defs[idx][ 'type'] == 'convolutional_noconv':
                    channels = weight_copy.shape[0]
                    channels_half=int(channels/2)
                    weight_copy1=weight_copy[:channels_half]
                    weight_copy2 = weight_copy[channels_half:]
                    min_channel_num = int(channels_half * opt.layer_keep) if int(channels_half * opt.layer_keep) > 0 else 1
                    mask1 = weight_copy1.gt(thresh).float()
                    mask2 = weight_copy2.gt(thresh).float()

                    if int(torch.sum(mask1)) < min_channel_num:
                        _, sorted_index_weights1 = torch.sort(weight_copy1, descending=True)
                        mask1[sorted_index_weights1[:min_channel_num]] = 1.

                    if int(torch.sum(mask2)) < min_channel_num:
                        _, sorted_index_weights2 = torch.sort(weight_copy2, descending=True)
                        mask2[sorted_index_weights2[:min_channel_num]] = 1.

                    # regular
                    mask_cnt1 = int(mask1.sum())
                    mask_cnt2 = int(mask2.sum())

                    if mask_cnt1 % 8 != 0:
                        mask_cnt1 = int((mask_cnt1 // 8 + 1) * 8)
                    if mask_cnt2 % 8 != 0:
                        mask_cnt2 = int((mask_cnt2 // 8 + 1) * 8)

                    this_layer_sort_bn = bn_module.weight.data.abs().clone()
                    this_layer_sort_bn1 = this_layer_sort_bn[:channels_half]
                    this_layer_sort_bn2 = this_layer_sort_bn[channels_half:]
                    _, sorted_index_weights1 = torch.sort(this_layer_sort_bn1, descending=True)
                    _, sorted_index_weights2 = torch.sort(this_layer_sort_bn2, descending=True)
                    mask1[sorted_index_weights1[:mask_cnt1]] = 1.
                    mask2[sorted_index_weights2[:mask_cnt2]] = 1.


                    remain1 = int(mask1.sum())
                    pruned = pruned + mask1.shape[0] - remain1
                    remain2 = int(mask2.sum())
                    pruned = pruned + mask2.shape[0] - remain2

                    mask=torch.cat((mask1,mask2))
                    remain=remain1+remain2

                    print(f'layer index: {idx:>3d} \t total channel: {mask.shape[0]:>4d} \t '
                          f'remaining channel: {remain:>4d}')
                else:
                
                    channels = weight_copy.shape[0] #
                    min_channel_num = int(channels * opt.layer_keep) if int(channels * opt.layer_keep) > 0 else 1
                    mask = weight_copy.gt(thresh).float()

                    if int(torch.sum(mask)) < min_channel_num:
                        _, sorted_index_weights = torch.sort(weight_copy,descending=True)
                        mask[sorted_index_weights[:min_channel_num]]=1.

                    # regular
                    mask_cnt = int(mask.sum())

                    if mask_cnt % 8 !=0:
                        mask_cnt=int((mask_cnt//8+1)*8)

                    this_layer_sort_bn = bn_module.weight.data.abs().clone()
                    _, sorted_index_weights = torch.sort(this_layer_sort_bn,descending=True)
                    mask[sorted_index_weights[:mask_cnt]]=1.

                    remain = int(mask.sum())
                    pruned = pruned + mask.shape[0] - remain

                    print(f'layer index: {idx:>3d} \t total channel: {mask.shape[0]:>4d} \t '
                            f'remaining channel: {remain:>4d}')
            else:
                mask = torch.ones(bn_module.weight.data.shape)
                remain = mask.shape[0]

            total += mask.shape[0]
            num_filters.append(remain)
            filters_mask.append(mask.clone())

        prune_ratio = pruned / total
        print(f'Prune channels: {pruned}\tPrune ratio: {prune_ratio:.3f}')

        return num_filters, filters_mask

    num_filters, filters_mask = obtain_filters_mask(model, thresh, CBL_idx, prune_idx)
    CBLidx2mask = {idx: mask for idx, mask in zip(CBL_idx, filters_mask)}
    CBLidx2filters = {idx: filters for idx, filters in zip(CBL_idx, num_filters)}

    for i in model.module_defs:
        if i['type'] == 'shortcut':
            i['is_access'] = False

    print('merge the mask of layers connected to shortcut!')
    merge_mask_regular(model, CBLidx2mask, CBLidx2filters)

    def prune_and_eval(model, CBL_idx, CBLidx2mask):
        model_copy = deepcopy(model)

        for idx in CBL_idx:
            # bn_module = model_copy.module_list[idx][1]
            bn_module = model_copy.module_list[idx][1] if type(
                model_copy.module_list[idx][1]).__name__ == 'BatchNorm2d' else model_copy.module_list[idx][0]
            mask = CBLidx2mask[idx].cuda()
            bn_module.weight.data.mul_(mask)

        with torch.no_grad():
            mAP = eval_model(model_copy)[0][2]

        print(f'mask the gamma as zero, mAP of the model is {mAP:.4f}')


    prune_and_eval(model, CBL_idx, CBLidx2mask)


    for i in CBLidx2mask:
        CBLidx2mask[i] = CBLidx2mask[i].clone().cpu().numpy()

    pruned_model = prune_model_keep_size2(model, prune_idx, CBL_idx, CBLidx2mask)
    print("\nnow prune the model but keep size,(actually add offset of BN beta to following layers), let's see how the mAP goes")

    with torch.no_grad():
        eval_model(pruned_model)

    for i in model.module_defs:
        if i['type'] == 'shortcut':
            i.pop('is_access')

    compact_module_defs = deepcopy(model.module_defs)
    for idx in CBL_idx:
        assert compact_module_defs[idx]['type'] == 'convolutional' or compact_module_defs[idx][
            'type'] == 'convolutional_noconv'
        num=CBLidx2filters[idx]
        compact_module_defs[idx]['filters'] = str(num)
        if compact_module_defs[idx]['type'] == 'convolutional_noconv':
            model_def = compact_module_defs[idx - 1]  # route
            assert compact_module_defs[idx - 1]['type'] == 'route'
            from_layers = [int(s) for s in model_def['layers'].split(',')]
            assert compact_module_defs[idx - 1 + from_layers[0]]['type'] == 'convolutional_nobias'
            assert compact_module_defs[idx - 1 + from_layers[1] if from_layers[1] < 0 else from_layers[1]][
                       'type'] == 'convolutional_nobias'
            half_num = int(len(CBLidx2mask[idx]) / 2)
            mask1 = CBLidx2mask[idx][:half_num]
            mask2 = CBLidx2mask[idx][half_num:]
            remain1 = int(mask1.sum())
            remain2 = int(mask2.sum())
            compact_module_defs[idx - 1 + from_layers[0]]['filters'] = remain1
            compact_module_defs[idx - 1 + from_layers[1] if from_layers[1] < 0 else from_layers[1]]['filters'] = remain2


    compact_model = Darknet([model.hyperparams.copy()] + compact_module_defs, (img_size, img_size)).to(device)
    compact_nparameters = obtain_num_parameters(compact_model)

    init_weights_from_loose_model(compact_model, pruned_model, CBL_idx, Conv_idx, CBLidx2mask)


    random_input = torch.rand((1, 3, img_size, img_size)).to(device)

    def obtain_avg_forward_time(input, model, repeat=200):
        # model.to('cpu').fuse()
        # model.module_list.to(device)
        model.eval()
        start = time.time()
        with torch.no_grad():
            for i in range(repeat):
                output = model(input)[0]
        avg_infer_time = (time.time() - start) / repeat

        return avg_infer_time, output

    print('testing inference time...')
    pruned_forward_time, pruned_output = obtain_avg_forward_time(random_input, pruned_model)
    compact_forward_time, compact_output = obtain_avg_forward_time(random_input, compact_model)

    diff = (pruned_output - compact_output).abs().gt(0.001).sum().item()
    if diff > 0:
        print('Something wrong with the pruned model!')

    print('testing the final model...')
    with torch.no_grad():
        compact_model_metric = eval_model(compact_model)


    metric_table = [
        ["Metric", "Before", "After"],
        ["mAP", f'{origin_model_metric[0][2]:.6f}', f'{compact_model_metric[0][2]:.6f}'],
        ["Parameters", f"{origin_nparameters}", f"{compact_nparameters}"],
        ["Inference", f'{pruned_forward_time:.4f}', f'{compact_forward_time:.4f}']
    ]
    print(AsciiTable(metric_table).table)



    pruned_cfg_name = opt.cfg.replace('/', f'/prune_{opt.global_percent}_keep_{opt.layer_keep}_8x_{opt.weight.split('/')[-1].split['.'][0]}')
    pruned_cfg_file = write_cfg(pruned_cfg_name, [model.hyperparams.copy()] + compact_module_defs)
    print(f'Config file has been saved: {pruned_cfg_file}')

    compact_model_name = opt.weights.replace('/', f'/prune_{opt.global_percent}_keep_{opt.layer_keep}_8x_')
    if compact_model_name.endswith('.pt'):
        chkpt = {'epoch': -1,
                 'best_fitness': None,
                 'training_results': None,
                 'model': compact_model.state_dict(),
                 # 'model': compact_model.module_list,  #部署调试加载的模型
                 'optimizer': None}
        torch.save(chkpt, compact_model_name)
        compact_model_name = compact_model_name.replace('.pt', '.weights')
    # save_weights(compact_model, path=compact_model_name)
    print(f'Compact model has been saved: {compact_model_name}')

