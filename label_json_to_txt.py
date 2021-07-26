import json

dstlabeldir = "/data/ftp/data_0624/label_txt"
srclabeldir = "/data/ftp/data_0624/label"


def json2str(onelabel):
    oneline = ""
    bIswrite = False
    mainclass = onelabel['type']

    if (mainclass == 'car'):
        subclass = onelabel.get('sub_class')
        genre = onelabel.get('genre')
        if (subclass is not None):
            subclass = onelabel['sub_class']
        if (genre is not None):
            subclass = onelabel['genre']
    else:
        subclass = '-'

    cover = onelabel['cover']
    coverval = '2'
    if (cover == 'none'):
        coverval = '0'
    if (cover == 'moderately'):
        coverval = '1'
    if (cover == 'severely'):
        mainclass = 'DontCare'
        subclass = '-'
        converval = '2'
    xloc = onelabel['position']['x']
    yloc = onelabel['position']['y']
    zloc = onelabel['position']['z']
    length = onelabel['size'][0]
    width = onelabel['size'][1]
    height = onelabel['size'][2]
    rotation_y = onelabel['rotation']['phi']
    pointnum = onelabel['pointNum']

    oneline = oneline + mainclass + ' ' + subclass + ' ' + coverval + ' '
    oneline = oneline + '0.0 0.0 0.0 0.0' + ' '
    oneline = oneline + width + ' ' + height + ' ' + length + ' '
    oneline = oneline + xloc + ' ' + yloc + ' ' + zloc + ' '
    oneline = oneline + rotation_y + ' ' + '%d\n' % pointnum
    return oneline


def jsonfile2txtfile(srcfilename, dstfilename):
    srcfile = open(srcfilename, 'r')
    dstfile = open(dstfilename, 'w')
    srcdata = json.load(srcfile)
    label = srcdata['label']['3D']
    for Idx in range(len(label)):
        print('Idx = %d' % Idx)
        onelabel = label[Idx]
        oneline = json2str(onelabel)
        dstfile.write(oneline)
    dstfile.close()
    srcfile.close()


if __name__ == "__main__":
    nTotalfilenum = 30328
    for Idx in range(nTotalfilenum):
        srcfilename = srclabeldir + '/%06d.json' % Idx
        dstfilename = dstlabeldir + '/%06d.txt' % Idx
        print(srcfilename)
        print(dstfilename)
        jsonfile2txtfile(srcfilename, dstfilename)
        print('processing at Idx = %d' % Idx)
