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
from KNN_01 import classify0


'''
Function:
	将文件内的数据转换成可供直接分析处理的数据集
Parameters: 
	filename: 文件名
Return：
	returnMat: 数据矩阵
	classLabelVector: 标签向量
'''
def file2matrix(filename):
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
			classLabelVector.append(0)
		elif listFromLine[-1] == 'smallDoses':
			classLabelVector.append(1)
		elif listFromLine[-1] == 'largeDoses':
			classLabelVector.append(2)
		# classLabelVector.append(listFromLine[-1])
		index += 1
	return returnMat, classLabelVector


'''
Function：
	归一化特征值
	newValue: (oleValue-min)/(max-min)
Parameters：
	dataSet：矩阵化数据集
Return：
	normDataSet: 归一化后的数据集
	ranges: 列取值跨度组成的数组
	minValue: 列最小值组成的数组
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


'''
Function:
	分类器针对约会匹配的测试函数
	hoRatio = 0.1并且 k = 3的条件下：匹配错误率为5%
Parameters：
	NULL
Return：
	打印结果
'''
def datingClassTest():
	hoRatio = 0.9
	datingDataMat,datingLabels = file2matrix('KNN_02_dataSet.txt')
	norMat,ranges,minValue = autoNorm(datingDataMat)
	# 测试向量的总数量
	m = norMat.shape[0]
	# print(m)

	# 分类，将一部分用于训练样本，一部分用于测试
	numTestVecs = int(m*hoRatio)
	# print(numTestVecs)

	# 错误计数
	errorCount = 0.0
	for i in range(numTestVecs):
		classifierResult = classify0(norMat[i,:],norMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
		print("the classifier came back with: %d,the real answer is: %d" %(classifierResult,datingLabels[i]))
		if(classifierResult != datingLabels[i]):
			errorCount +=1.0
	# print("errorCount is : %f; totalCount is : %f" %(errorCount,float(numTestVecs)))
	# print("the total error rate is: %f" %(errorCount/float(numTestVecs)))


'''
Function:
	文件内容转换为可用数据
	利用可视化图表对比进行数据的粗放比较
Parameters：
	NULL
Return：
	可视化表
'''
def dataMap():
	datingDataMat,datingLabels = file2matrix('KNN_02_dataSet.txt')
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15*np.array(datingLabels),15*np.array(datingLabels))
	plt.show()

'''
Function:
	跟据输入数据向量，得到约会匹配结果	
Parameters:
	NULL
Return:
	给出预测结果
'''
def classifyPerson():
	resultList = ["notLike","littleLove","veryLove"]
	inx1 = float(input("airplane:"))
	inx2 = float(input("play game time:"))
	inx3 = float(input("buy ice one week:"))
	# 构造测试数据集inX（这里只有一条数据）
	inArray = np.array([inx1, inx2, inx3])
	datingDataMat,datingLabels = file2matrix('KNN_02_dataSet.txt')
	norMat,ranges,minValue = autoNorm(datingDataMat)
	classifyResult = classify0((inArray - minValue)/ranges,norMat, datingLabels, 3)
	print("The result is : ",resultList[classifyResult])


if __name__ == '__main__':
	classifyPerson()

