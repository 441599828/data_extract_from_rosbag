import os
import sys

from shutil import copyfile
import json

# import numpy as np

# marktxtfilename = '/data/ftp/mark/202105131354425578/mark.txt'
# marktxtfilename = '/home/wanghuanan/home/wanghuanan/scripts/202102041712494010.txt'
# marktxtfilename = '/home/wanghuanan/home/wanghuanan/scripts/202103181838344882.txt'
# marktxtfilename = '/home/wanghuanan/home/wanghuanan/scripts/202105061545266948.txt'
# marktxtfilename = '/home/wanghuanan/home/wanghuanan/scripts/202105131346365963.txt'
# marktxtfilename = '/home/wanghuanan/home/wanghuanan/scripts/202105131354425578.txt'
# marktxtfilename = '/home/wanghuanan/home/wanghuanan/scripts/202105251326177197.txt'
marktxtfilename = '/home/wanghuanan/home/wanghuanan/scripts/202105281357291519.txt'

# labeltxtfilename = '/data/ftp/mark/202102041712494010/4434219.txt'
# labeltxtfilename = '/data/ftp/mark/202103181838344882/robosense80_225.txt'
# labeltxtfilename = '/data/ftp/mark/202105061545266948/457247.txt'
# labeltxtfilename = '/data/ftp/mark/202105131346365963/463828.txt'
# labeltxtfilename = '/data/ftp/mark/202105131354425578/result_0514.txt'
# labeltxtfilename = '/data/ftp/mark/202105251326177197/475722.txt'
labeltxtfilename = '/data/ftp/mark/202105281357291519/all.txt'

srcvelodir = '/data/ftp/resolved/'

# dstlframedir = '/data/ftp/data_0624/image1/'
dstsframedir = '/data/ftp/data_0624/image0/'
dstvelodir = '/data/ftp/data_0624/velodyne/'
labeljsondir = '/data/ftp/data_0624//label/'

# nstartIdx = 0
# nstartIdx = 59
# nstartIdx = 281
# nstartIdx = 4676
# nstartIdx = 9446
# nstartIdx = 19452
nstartIdx = 23497


def get_name_array(markfilename):
    namefile = open(markfilename, 'r')
    velofiles = []
    lframefiles = []
    sframefiles = []
    ntotalline = 0
    nvalidline = 0
    while True:
        one_line = namefile.readline()
        if (one_line is not None and one_line != ""):
            print('processing at lineIdx=%d' % ntotalline)
            ntotalline += 1
            split_line = one_line.strip().strip('[').strip(']').split(',')
            if (len(split_line) == 3):
                velofilename = split_line[0][1:-1]
                sframename = split_line[1][2:-1]
                lframename = split_line[-1][2:-1]
                velofiles.append(velofilename)
                lframefiles.append(lframename)
                sframefiles.append(sframename)
                nvalidline += 1
        else:
            break
    print('nTotalline=%d,nvalidline=%d' % (ntotalline, nvalidline))
    print('Generate index end!')
    return velofiles, lframefiles, sframefiles


def transferfile():
    velofiles,lframefiles,sframefiles = get_name_array(marktxtfilename)
    print("length of velofiles=%d,length of lframefiles=%d,length of sframefiles=%d" %(len(velofiles),len(lframefiles),len(sframefiles)))
    labelfile = open(labeltxtfilename, 'r')

    ntotalline = 0
    nvalidline = 0
    Idx = nstartIdx
    while True:
        oneline = labelfile.readline()
        print("processing at lineIdx = %d" % ntotalline)
        ntotalline += 1
        if (oneline is not None and oneline != ""):
            splitline = oneline.strip().split()
            frameinfo = splitline[0]
            datainfo = splitline[-1]

            timeval = frameinfo.split('_')[-1]
            scenefolder = frameinfo.replace('_' + timeval, '')
            timeval = timeval.replace('.zip', '')

            veloname = srcvelodir + scenefolder + '/lidars/LIDAR_TOP/' + timeval + '.bin'
            print(veloname)
            for i in range(0, len(velofiles)):
                if (os.path.exists(veloname)) and velofiles[i] == veloname:
                    json_info = json.loads(datainfo, strict=False)
                    json_info = json_info['extra'][0]
                    label = json_info['label']['3D']
                    if (len(label) > 0):
                        dstveloname = dstvelodir + '%06d.bin' % Idx
                        copyfile(veloname, dstveloname)
                        dstsframename = dstsframedir + '%06d.jpg' % Idx
                        copyfile(sframefiles[i], dstsframename)
                        # dstlframename = dstlframedir + '%06d.jpg' % Idx
                        # copyfile(lframefiles[i], dstlframename)
                        dstlabelname = labeljsondir + '%06d.json' % Idx
                        with open(dstlabelname, 'w') as json_f:
                            json.dump(json_info, json_f)
                        Idx += 1
                        nvalidline += 1
        else:
            break
    print("Total %d frames in %d frames transfered!" % (nvalidline, ntotalline))


if __name__ == "__main__":
    transferfile()
