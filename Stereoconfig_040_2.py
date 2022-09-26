import numpy as np


# 双目相机参数
class stereoCamera(object):
    def __init__(self):
        # 左相机内参
        self.cam_matrix_left = np.array([[861.0238, 0.8785, 646.3517],
                                         [0, 856.4744, 379.3723],
                                         [0, 0, 1]
                                         ])
        # 右相机内参
        self.cam_matrix_right = np.array([[912.4512, 1.2331, 674.5979],
                                          [0, 907.6271, 376.3592],
                                          [0, 0, 1]
                                          ])

        # 左右相机畸变系数:[k1, k2, p1, p2, k3]
        self.distortion_l = np.array([[-0.3928, 0.3222, 0.0005432, -0.0008847, -0.2972]])
        self.distortion_r = np.array([[-0.4187, 0.2275, 0.0016, -0.0005, -0.2972]])

        # 旋转矩阵
        self.R = np.array([[1, -0.0082, -0.0006],
                           [0.0082, 0.9994, -0.0344],
                           [0.0009, 0.0344, 0.9994]
                           ])

        # 平移矩阵
        self.T = np.array([[1.0203], [65.8590], [-32.6730]])

        # todo: 焦距
        # self.focal_length = 859.367  # 默认值，一般取立体校正后的重投影矩阵Q中的 Q[2,3]

        # 基线距离
        self.baseline = 1.0203  # 单位：mm， 为平移向量的第一个参数（取绝对值）
