def takefirst(elem):
return elem[0]		#指定排列函数，只看元组第一项（质量）

def update():
    import os, os.path
    DIR = '/home/pi/Desktop/Pictures'
    listofnames = []
    q = []
    for name in os.listdir(DIR):
        if os.path.isfile(os.path.join(DIR,name)):
            listofnames.append(name)	#列出Pictures里所有的文件名
    if len(listofnames) > 10:				#如果照片数量超过指定值：
        i = 0
        for name in listofnames:
            nq = name.split("*")
            nq[1] = int(nq[1].replace(".jpg",""))
            qe = int(int(nq[0]) * nq[1])			#将文件名转换成照片质量
            q.append((qe,i))		#用（照片质量，照片索引）的形式打包数据
            i += 1
        q = sorted(q,key = takefirst)		#按照质量从低到高排列
        last = q[0][1]
