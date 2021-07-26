import os.path
import random
import numpy as np
from shutil import copyfile


def split_train_val(num, ratio):
    ntrainnum = int(num * ratio + 0.5)
    mainlist = ['%06d' % i for i in range(num)]
    random.seed(23)
    random.shuffle(mainlist)
    trainlist = mainlist[0:ntrainnum].sort()
    vallist = mainlist[ntrainnum:].sort()
    mainlist.sort()
    return mainlist, trainlist, vallist


def sample_seg(ntotalnum, outnum):
    mainlist = ['%06d' % i for i in range(ntotalnum)]
    random.seed(23)
    random.shuffle(mainlist)
    for i in range(0, 300):
        copyfile('/data/ftp/data_0624/image0/' + mainlist[i] + '.jpg',
                 '/data/ftp/data_0624/image_for_seg/01_300/' + mainlist[i] + '.jpg')
    for i in range(301, 601):
        copyfile('/data/ftp/data_0624/image0/' + mainlist[i] + '.jpg',
                 '/data/ftp/data_0624/image_for_seg/02_300/' + mainlist[i] + '.jpg')
    for i in range(602, 902):
        copyfile('/data/ftp/data_0624/image0/' + mainlist[i] + '.jpg',
                 '/data/ftp/data_0624/image_for_seg/03_300/' + mainlist[i] + '.jpg')
    for i in range(902, outnum):
        copyfile('/data/ftp/data_0624/image0/' + mainlist[i] + '.jpg',
                 '/data/ftp/data_0624/image_for_seg/04_100/' + mainlist[i] + '.jpg')


if __name__ == "__main__":
    ntotalnum = 30328
    img_seg = sample_seg(ntotalnum, 1002)

    # mainlist, trainlist, vallist = split_train_val(ntotalnum, 30)
    # print('total:%d,train:%d,val:%d' % (len(mainlist), len(trainlist), len(vallist)))
    # np.savetxt('/data/ftp/data_0624/test.txt', np.array(mainlisst))
    # np.savetxt('/data/ftp/data_0624/train.txt', np.array(trainlist))
    # np.savetxt('/data/ftp/data_0624/val.txt', np.array(vallist))
    print('Generated finished!')
