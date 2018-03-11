# -*- coding: UTF-8 -*-
# 电影类别
"""
问题说明：
	根据爱情片和动作片的镜头数（训练集），得到目标数据（测试集）分类
数据描述：
	特征名： 
		1.爱情类镜头数
		2.动作类镜头数
	标签名：
		1.爱情片
		2.动作片
"""

import numpy as np
import operator

'''
Function:
	创建数据集和数据标签

Parameters：
	NULL
Return：
	group: 矩阵化测试集
	labels: 标签列表
'''
def createDataSet():
	group = np.array([[3,104],[2,100],[1,81],[101,10],[99,5],[98,2]])
	labels = ['爱情片1','爱情片2','爱情片3','动作片1','动作片2','动作片3']
	return group,labels


'''
Function:
	基于knn算法的分类器
Parameters:
	inX: 用于分类的数据（测试集）
	dataSet: 训练集
	labels: 分类的标签列表
	k: 选择knn算法中，距离最小的k个点
Return: 
	sortedClassCount[0][0]: 分类标签
'''
def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	# tile(A,(B,C))  用inX构成一个B*C的矩阵
	diffMat = np.tile(inX,(dataSetSize,1)) - dataSet
	sqDiffMat = diffMat**2
	# sum()所有元素相加，saxis=0列相加，axis=1行相加
	sqDistance = sqDiffMat.sum(axis = 1)
	# 距离列表
	distances = sqDistance**0.5

	# 升序排序，索引数组
	sortedDistIndicies = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		# get()返回集合的voteIlabel键值，没有则默认返回0
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
	# Python3中items()替代了iteritems()
	# key=operator.itemgetter(1)根据字典的值进行排序
	# key=operator.itemgetter(0)根据字典的键进行排序
	# reverse降序排序字典
	sortedClassCount = sorted(classCount.items(),key = operator.itemgetter(1),reverse = True)
	return sortedClassCount[0][0]


if __name__ == '__main__':
	group,labels= createDataSet()
	# 测试数据
	test = [18,90]
	result = classify0(test,group, labels,3)
	print(result)
