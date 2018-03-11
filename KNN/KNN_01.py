import numpy as np
import operator

def createDataSet():
	# [打斗镜头数，接吻镜头数]
	group = np.array([[3,104],[2,100],[1,81],[101,10],[99,5],[98,2]])
	labels = ['爱情片1','爱情片2','爱情片3','动作片1','动作片2','动作片3']
	return group,labels

def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	# tile(A,(B,C)) 在列方向将A重复C次，行方向重复B次
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

# 测试部分
if __name__ == '__main__':
	group,labels= createDataSet()
	test = [18,90]
	result = classify0(test,group, labels,3)
	print(result)
