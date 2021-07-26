import cv2
import shutil
import numpy as np


k = np.array([1303.206437, 0.000000, 604.443674, 0.000000, 1300.853527, 301.882005, 0.000000, 0.000000, 1.000000]).reshape([3, 3])
d = np.array([-0.451650, 0.176863, -0.000502, 0.002665, 0.000000])


def undistort(img):
    h, w = img.shape[:2]
    mapx, mapy = cv2.initUndistortRectifyMap(k, d, None, k, (w, h), 5)
    return cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)


if __name__ == "__main__":
    srcframedir = "/data/ftp/data_0624/image0"
    dstframedir = "/data/ftp/data_0624/image0_undistort"
    # nTotalfilenum = 30328
    nTotalfilenum = 1
    for Idx in range(nTotalfilenum):
        # srcfilename = srcframedir + "/%06d.png" % Idx
        srcfilename = '/home/idriver/data/39_2021-07-09-11-35-50_0/1625801849600194931.jpg'
        # dstfilename = dstframedir + "/%06d.png" % Idx
        dstfilename = '/home/idriver/data/39_2021-07-09-11-35-50_0/1625801849600194931_undistort.jpg'
        frame = cv2.imread(srcfilename)
        frame = undistort(frame)
        cv2.imwrite(dstfilename, frame)
        print("processing at Idx = %d" % Idx)
