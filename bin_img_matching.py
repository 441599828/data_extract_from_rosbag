import os


# def check_if_depack(files_root):
#     files = os.listdir(files_root)
#     files_check = []
#     for file in files:
#         if '35_perception' in file:
#             files_check.append(file)
#     emptycheck = 0
#     for file in files_check:
#         file = os.path.join(files_root, file, 'cameras', 'FRONT_SHORT')
#         if not os.listdir(file):
#             emptycheck += 1
#             print(file)
#     if emptycheck == 1:
#         print("need unpack.")
#     else:
#         print('unpacked.')


def one_unit_pairing(LIDAR_TOP_int, FRONT_SHORT_int, TIME_DELAY_THRES_raw):
    # match (LIDAR_TOP, FRONT_SHORT) pairs
    print("Starting to match (LIDAR_TOP, FRONT_SHORT) pairs:")
    matched_pairs = []
    for LIDAR_TOP_pc in LIDAR_TOP_int:
        best_match = [LIDAR_TOP_pc, -1]
        TIME_DELAY_THRES = TIME_DELAY_THRES_raw
        for FRONT_SHORT_img in FRONT_SHORT_int:
            time_pause_now = abs(FRONT_SHORT_img - LIDAR_TOP_pc)
            if time_pause_now < TIME_DELAY_THRES:
                best_match[1] = FRONT_SHORT_img
                TIME_DELAY_THRES = time_pause_now
        matched_pairs.append(best_match)

    # ignore frame bigger than 50ms
    matched_result = []
    for i in matched_pairs:
        if i[1] != -1:
            matched_result.append(i)
    print("Finished data pairing.")
    return (matched_result)


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
            split_line = one_line.strip().split(',')
            if (len(split_line) == 5):
                velofilename = split_line[0]
                lframename = split_line[1]
                sframename = split_line[-1]
                velofiles.append(velofilename)
                lframefiles.append(lframename)
                sframefiles.append(sframename)
                nvalidline += 1
        else:
            break
    print('nTotalline=%d,nvalidline=%d' % (ntotalline, nvalidline))
    print('Generate index end!')
    return velofiles, lframefiles, sframefiles


# def transferfile(matched_pairs):
#     # velofiles,lframefiles,sframefiles = get_name_array(marktxtfilename)
#     # print("length of velofiles=%d,length of lframefiles=%d,length of sframefiles=%d" %(len(velofiles),len(lframefiles),len(sframefiles)))
#     labelfile = open(labeltxtfilename, 'r')
#     ntotalline = 0
#     nvalidline = 0
#     Idx = nstartIdx
#     while True:
#         oneline = labelfile.readline()
#         print("processing at lineIdx = %d" % ntotalline)
#         ntotalline += 1
#         if (oneline is not None and oneline != ""):
#             splitline = oneline.strip().split()
#             frameinfo = splitline[0]
#             datainfo = splitline[-1]
#
#             timeval = frameinfo.split('_')[-1]
#             scenefolder = frameinfo.replace('_' + timeval, '')
#             timeval = timeval.replace('.zip', '')
#
#             veloname = srcvelodir + scenefolder + '/lidars/LIDAR_TOP/' + timeval + '.bin'
#             print(veloname)
#             if (os.path.exists(veloname)):
#                 # dstveloname = dstvelodir + '%06d.bin' %Idx
#                 # copyfile(veloname,dstveloname)
#                 json_info = json.loads(datainfo, strict=False)
#                 json_info = json_info['extra'][0]
#                 label = json_info['label']['3D']
#                 if (len(label) > 0):
#                     dstveloname = dstvelodir + '%06d.bin' % Idx
#                     copyfile(veloname, dstveloname)
#                     dstlabelname = labeljsondir + '%06d.json' % Idx
#                     with open(dstlabelname, 'w') as json_f:
#                         json.dump(json_info, json_f)
#                     Idx += 1
#                     nvalidline += 1
#             else:
#                 print('error:not find velo file')
#             # nameIdx = [i for i,x in enumerate(velofiles) if x==veloname]
#             # if(len(nameIdx)==1):
#             #    lframename = lframefiles[nameIdx[0]]
#             #    sframename = sframefiles[nameIdx[0]]
#             #    if(os.path.exists(veloname) and os.path.exists(lframename) and os.path.exists(sframename)):
#             #	    dstveloname = dstvelodir + '%06d.bin' %Idx
#             #	    copyfile(veloname,dstveloname)
#             #	    dstlframename = dstlframedir + '%06d.png' %Idx
#             #       copyfile(lframename,dstlframename)
#             #	    dstsframename = dstsframedir + '%06d.png' %Idx
#             #       copyfile(sframename,dstsframename)
#             #	    json_info = json.loads(datainfo,strict=False)
#             #	    json_info = json_info['extra'][0]
#             #	    dstlabelname = labeljsondir + '%06d.json' %Idx
#             #	    with open(dstlabelname,'w') as json_f:
#             #		json.dump(json_info,json_f)
#             #	    Idx += 1
#             #	    nvalidline += 1
#             #	else:
#             #	    print('error:')
#             #	    print(scenefolder)
#             #       print(timeval)
#         # elif(len(nameIdx)==0):
#         #	print('error:not find frame file')
#         # elif(len(nameIdx)>=2):
#         #	print(nameIdx)
#         #   print('erro:two frame files has been find')
#         else:
#             break
#     print("Total %d frames in %d frames transfered!" % (nvalidline, ntotalline))


if __name__ == '__main__':
    files_root = '/data/ftp/resolved'

    # label_file = '/data/ftp/mark/202105061545266948/457247.txt'
    # label_file = '/data/ftp/mark/202105131346365963/463828.txt'
    # label_file = '/data/ftp/mark/202105131354425578/result_0514.txt'
    # label_file = '/data/ftp/mark/202102041712494010/4434219.txt'
    # label_file = '/data/ftp/mark/202103181838344882/robosense80_225.txt'
    # label_file = '/data/ftp/mark/202105281357291519/all.txt'
    label_file = '/data/ftp/mark/202105251326177197/475722.txt'
    TIME_DELAY_THRES = 50000000

    # find 35_perception*.bag
    files = os.listdir(files_root)
    filespack = []
    for file in files:
        # if '30_2021' in file:
        # if '31_video' in file or '31_banche' in file:
        # if '32_sanlunche' in file:
        # if '26_2020-12' in file:
        # if '27_xj8' in file:
        # if '36_perception' in file or '36_8897_wuhan' in file:
        if '35_perception' in file:
            filespack.append(file)

    # find LIDAR_TOP and FRONT_SHORT and FRONT_LONG
    LIDAR_TOP = []
    markfile = open(label_file, 'r')
    while True:
        one_line = markfile.readline()
        if (one_line is not None and one_line != ""):

            splitline = one_line.strip().split()
            frameinfo = splitline[0]
            timeval = frameinfo.split('_')[-1]
            timeval = timeval.replace('.zip', '')
            LIDAR_TOP.append(int(timeval))
        else:
            LIDAR_TOP.sort()
            break

    FRONT_SHORT = []
    FRONT_SHORT_ABS = []
    FRONT_LONG_ABS = []
    LIDAR_TOP_ABS = []
    for bagfile in filespack:
        FRONT_SHORT_raw = os.listdir(os.path.join(files_root, bagfile, 'cameras', 'FRONT_SHORT'))

        for i in FRONT_SHORT_raw:
            FRONT_SHORT_ABS.append(os.path.join(files_root, bagfile, 'cameras', 'FRONT_SHORT') + '/' + i)
            FRONT_LONG_ABS.append(os.path.join(files_root, bagfile, 'cameras', 'FRONT_LONG') + '/' + i)
        for i in range(len(FRONT_SHORT_raw)):
            FRONT_SHORT.append(int(FRONT_SHORT_raw[i][:-4]))
        FRONT_SHORT.sort()

        LIDAR_TOP_raw = os.listdir(os.path.join(files_root, bagfile, 'lidars', 'LIDAR_TOP'))
        for i in LIDAR_TOP_raw:
            LIDAR_TOP_ABS.append(os.path.join(files_root, bagfile, 'lidars', 'LIDAR_TOP') + '/' + i)

    matched_pairs = one_unit_pairing(LIDAR_TOP, FRONT_SHORT, TIME_DELAY_THRES)
    matched_pairs_abs = []
    for rel in matched_pairs:
        matched_one = []
        for lidar_abs in LIDAR_TOP_ABS:
            if str(rel[0]) in lidar_abs:
                matched_one.append(lidar_abs)
        for fs_abs in FRONT_SHORT_ABS:
            if str(rel[1]) in fs_abs:
                matched_one.append(fs_abs)
        for fl_abs in FRONT_LONG_ABS:
            if str(rel[1]) in fl_abs:
                matched_one.append(fl_abs)
        matched_ones=[]
        for filenamecheck in range(0, len(matched_one)):
            if matched_one[0].split('/')[0:-3] == matched_one[filenamecheck].split('/')[0:-3]:
                matched_ones.append(matched_one[filenamecheck])
        matched_pairs_abs.append(matched_ones)
    # save paired_result to .txt
    # fileObject = open('202105061545266948.txt', 'w')
    # fileObject = open('202105131346365963.txt', 'w')
    # fileObject = open('202105131354425578.txt', 'w')
    # fileObject = open('202102041712494010.txt', 'w')
    # fileObject = open('202103181838344882.txt', 'w')
    # fileObject = open('202105281357291519.txt', 'w')
    fileObject = open('202105251326177197.txt', 'w')

    for matched_pair in matched_pairs_abs:
        fileObject.write(str(matched_pair))
        fileObject.write('\n')
    fileObject.close()

    # copy_data
    # transferfile(matched_pairs)
