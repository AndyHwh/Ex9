import matplotlib.pyplot as plt
import math
import numpy as np
import random
import csv
plt.rcParams['font.sans-serif'] = ['SimHei']#设置显示中文
fig = plt.figure()
ax = fig.add_subplot(111)#将画布分割成1行1列，图像画在从左到右从上到下的第1块
#阶数为6阶
order=6
#生成曲线上的各个点
dataMat = np.loadtxt(open("/users/wangfeng/desktop/price1.csv","rb"),delimiter=",",skiprows=0)
size=dataMat.shape
num=size[0]
trandata=np.transpose(dataMat)#矩阵转置
xa=trandata[0]#得到天数数组（横坐标）
ya=trandata[1]#实测盐度值数组
#数据筛选,去除盐度值为零的，提高拟合精度
i=0
x=[]
y=[]
for yy in ya:
 if yy>0:
  xx=xa[i]
  i+=1
  x.append(xx)
  y.append(yy)
#绘制原始数据
ax.plot(x,y,label=u'原始数据',color='m',linestyle='',marker='.')
#计算多项式
c=np.polyfit(x,y,order)#拟合多项式的系数存储在数组c中
yy=np.polyval(c,x)#根据多项式求函数值
#进行曲线绘制
x_new=np.linspace(0, 365, 2000)
f_liner=np.polyval(c,x_new)
#ax.plot(x,y,color='m',linestyle='',marker='.')
ax.plot(x_new,f_liner,label=u'拟合多项式曲线',color='g',linestyle='-',marker='')
# labels标签设置
ax.set_xlim(0, 366)
ax.set_xlabel(u'天')
ax.set_ylabel(u'盐度')
ax.set_title(u'盐度的日变化', bbox={'facecolor':'0.8', 'pad':5})
ax.legend()
plt.show()