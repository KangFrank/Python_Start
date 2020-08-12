from sprites import *

ball = Sprite(1)             # 新建精灵，默认是小虫子，写1会生成一个弹球
while True:
    ball.fd(10)              # 前进10
    ball.bounce_on_edge() 
    time.sleep(0.2)   # 碰到边缘就反弹