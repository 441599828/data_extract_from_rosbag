import numpy as np
import os
from scipy.spatial.transform import Rotation

if __name__ == '__main__':
    calib_root = '/home/idriver/data_0624/unk1/calib'
    with open(calib_root + '/calib_05KasP.txt', 'r') as f:
        data = f.read()
        velo2cam = data.split('Tr_velo_to_cam:')[-1].split()
        velo2cam = [float(i) for i in velo2cam]
        velo2cam = np.array(velo2cam).reshape(3, 4)
        print('before:\n', velo2cam)

        velo2cam_rotation = velo2cam[:, 0:3]
        velo2cam_rotation = Rotation.from_matrix(velo2cam_rotation)
        velo2cam_euler = velo2cam_rotation.as_euler('zyx', degrees=True)
        # 1 degree
        velo2cam_euler[0] += 0.01
        # # 2 degree
        # velo2cam_euler[1] += 0.01
        # # 3 degree
        # velo2cam_euler[2] += 0.01

        adjusted = Rotation.from_euler('zyx', velo2cam_euler, degrees=True)
        adjusted = adjusted.as_matrix()
        velo2cam[:, 0:3] = adjusted
        print('adjusted:\n', velo2cam)
