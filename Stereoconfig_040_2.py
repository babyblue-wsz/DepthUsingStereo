import numpy as np


# 双目相机参数
class stereoCamera(object):
    def __init__(self):
        # 左相机内参
        self.cam_matrix_left = np.array([[867.6994, 0.0540, 657.1304],
                                         [0, 863.4875, 381.7076],
                                         [0, 0, 1]
                                         ])
        # 右相机内参
        self.cam_matrix_right = np.array([[902.1189, 0.3332, 684.5776],
                                          [0, 897.6722, 376.8460],
                                          [0, 0, 1]
                                          ])

        # 左右相机畸变系数:[k1, k2, p1, p2, k3]
        self.distortion_l = np.array([[-0.4125, 0.3554, -0.0013, -0.0030, -0.5077]])
        self.distortion_r = np.array([[-0.3674, -0.6338, 0.0011, -0.0021, 4.0875]])

        # 旋转矩阵
        self.R = np.array([[0.9973, -0.0600, 0.0422],
                           [0.0604, 0.9981, -0.0094],
                           [-0.0415, 0.0119, 0.9991]
                           ])

        # 平移矩阵
        self.T = np.array([[1.8190], [54.9169], [-37.2388]])

        # todo: 焦距
        # self.focal_length = 859.367  # 默认值，一般取立体校正后的重投影矩阵Q中的 Q[2,3]

        # 基线距离
        self.baseline = 1.8190  # 单位：mm， 为平移向量的第一个参数（取绝对值）
