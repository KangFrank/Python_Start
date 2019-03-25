'''
import cv2 as cv
# 读图片
img = cv.imread('img/Lenna.png')
# 图片信息
print('图片尺寸:', img.shape)
print('图片数据:', type(img), img)
# 显示图片
cv.imshow('pic title', img)
cv.waitKey(0)
# 添加文字
cv.putText(img, 'Learn Python with Crossin', (50, 150), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 4)
# 保存图片
cv.imwrite('img/Lenna_new.png', img)

import cv2 as cv
# 读图片
img = cv.imread('img/Lenna.png')
import numpy as np
# 灰度图
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imwrite('img/Lenna_gray.png', img_gray)
# 二值化
_, img_bin = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)
cv.imwrite('img/Lenna_bin.png', img_bin)
# 平滑
img_blur = cv.blur(img, (5, 5))
cv.imwrite('img/Lenna_blur.png', img_blur)
# 边缘提取
_, contours, _ = cv.findContours(img_bin, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
img_cont = np.zeros(img_bin.shape, np.uint8)    
cv.drawContours(img_cont, contours, -1, 255, 3) 
cv.imwrite('img/Lenna_cont.png', img_cont)
'''
#导入cv模块
# -*- coding: utf-8 -*- 
import cv2 as cv
 
#读取图像，支持 bmp、jpg、png、tiff 等常用格式
img = cv.imread("C:/Users/kangl/Desktop/test.png")
# C:/Users/kangl/Desktop/test.png is right
#创建窗口并显示图像
cv.namedWindow("Image")
cv.imshow("Image",img)
cv.waitKey(0)
#释放窗口
cv.destroyAllWindows()

