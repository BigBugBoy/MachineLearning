# -*- coding: UTF-8 -*-
# 约会匹配
"""
问题说明：
	根据采集的数据（训练集），标签有喜欢、有点喜欢和不喜欢，匹配约会对象
数据描述：
	文件名: 
		KNN_02_dataSet.txt
	特征名：
		1.每年获得的飞行常客里程数	
		2.玩视频游戏所耗时间百分比
		3.每周消费的冰淇淋公升数
	标签名：
		largeDoses
		smallDoses
		didntLike
"""

from matplotlib.font_manager import FontProperties
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np
import operator


'''
Function:
	将文件内的数据转换成可供直接分析处理的数据集
Parameters: 
	filename: 文件名
Return：
	returnMat: 数据矩阵
	classLabelVector: 标签向量
'''
def filematrix(filename):
	fr = open(filename)
	arrayOLines = fr.readlines()
	# 获得数据长度
	numberOfLines = len(arrayOLines)
	#  创建一个3列的数组
	returnMat = np.zeros((numberOfLines,3))
	classLabelVector = []
	index = 0
	for line in arrayOLines:
		line = line.strip()
		listFromLine = line.split('\t')
		returnMat[index,:] = listFromLine[0:3]
		# print(returnMat)
		if listFromLine[-1] == 'didntLike':
			classLabelVector.append(1)
		elif listFromLine[-1] == 'smallDoses':
			classLabelVector.append(2)
		elif listFromLine[-1] == 'largeDoses':
			classLabelVector.append(3)
		# classLabelVector.append(listFromLine[-1])
		index += 1
	return returnMat, classLabelVector


'''
Function：
	归一化特征值
	newValue: (oleValue-min)/(max-min)
Parameters：
	dataSet: 
'''
def autoNorm(dataSet):
	# 计算数据集的列的最小值和最大值
	minValue = dataSet.min(0)
	maxValue = dataSet.max(0)
	ranges = maxValue - minValue
	normDataSet = np.zeros(np.shape(dataSet))
	# 数据集的条数（行数）
	m = dataSet.shape[0]
	normDataSet = dataSet - np.tile(minValue,(m,1))
	normDataSet = normDataSet/np.tile(ranges,(m,1))
	return normDataSet,ranges,minValue


if __name__ == '__main__':
	datingDataMat,datingLabels = filematrix('KNN_02_dataSet.txt')
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15*np.array(datingLabels),15*np.array(datingLabels))
	plt.show()

