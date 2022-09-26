import numpy as np
import cv2

# 分割双目图片，分为上下两部分
# todo: https://blog.csdn.net/qq_40700822/article/details/124251201?spm=1001.2014.3001.5501   这篇文章记录了matlab标定过程

# img1 = cv2.imread(r"/Users/inbc/Desktop/zuo/Left1.bmp")
# img2 = cv2.imread(r"/Users/inbc/Desktop/you/Right1.bmp")
for i in range(5, 57):
    imgT = cv2.imdecode(np.fromfile('./p/IMG_00%d.jpg' % i, dtype=np.uint8), -1)  # 读取拍摄的左右双目照片

    # cv2.imshow("zuo", img1[300:1200, 500:2000])
    # cv2.imshow("you", img2[300:1200, 500:2000])

    # cv2.waitKey(0)

    # 设置左右照片的存储位置
    cv2.imwrite("./p/bottom/bottom_%d.jpg" % i, imgT[0:720, 0:1280])  # imgL的第一个参数是图片高度像素范围，第二个参数是图片宽度的像素范围
    cv2.imwrite("./p/top/top_%d.jpg" % i, imgT[720:1440, 0:1280])
    print("Resize images%d Fnished!" % i)

print("Fnished All!!!")