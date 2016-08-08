
#coding=utf-8
import os



#判断目录是否存在的函数
def isexist (i):
    while i<7:
        pa='/'.join(line[0:i])
        path='/'.join(line[i:7])
 
        if os.path.isdir(pa):
            isexist(i=i+1)
        else:
            if os.path.exists(path)==False:
                os.makedirs(path)
            break

#取每行第一个字符，判断以该字符命名的文件夹是否存在
#存在，即判断前两个字符的二级目录是否存在
#不存在，即以该行数据的前七个字符命名一个七级目录


#读取文件每行数据  可以实现创建多级目录  剩下就是当存在时该如何判断？
f=open("sha1.txt","r")
line=f.readline()

while line:
    #pa='/'.join(line[0])
    #path='/'.join(line[0:7])
    #if os.path.isdir(pa):
        #还是继续判断但此时便成了在二级目录里边判断。即此时应该比较的两个目录为
        #pa===line[0:1]   path====line[1:7]  即就是说要传参刚开始传入i=0  然后传入i=1  依次类推
        #封装函数
        
        
    #else:
       # os.makedirs(path)
    isexist(0)    
    line=f.readline()
f.close()





