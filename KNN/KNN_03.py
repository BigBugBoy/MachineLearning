# -*- coding: UTF-8 -*-

# 手写识别系统

"""
问题说明
	根据已知数字的二进制图片作为训练集，
数据描述

"""


import numpy as np
from os import listdir 
from KNN_01 import classify0


"""
Function:
	将图片数据转换为计算机可以处理的向量格式
Parameters:
	文件名称
Return:
	1*1024的向量
"""
def img2vector(filename):
	returnVect = np.zeros((1,1024))
	fr = open(filename)
	for i in range(32):
		lineStr = fr.readline()
		for j in range(32):
			returnVect[0,32*i+j] =int(lineStr[j])
	return returnVect


"""
Function:
Patameters:
Return:
"""
def handwritingClassTest():
	hwLabels = []
	trainingFileList = listdir('trainingDigits')
	# 获得训练集文件目录
	m = len(trainingFileList)
	trainingMat = np.zeros((m, 1024))
	# m行*1024列，每一个元素都没zeros
	for i in range(m):
		fileNameStr = trainingFileList[i]
		fileStr = fileNameStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])
		hwLabels.append(classNumStr)
		trainingMat[i,:] = img2vector('trainingDigits/%s'%fileNameStr)
	testFileList = listdir('testDigits')
	# 获得测试集文件目录
	errorCount = 0.0
	# 错误计数变量
	mTest = len(testFileList)
	for i in range(mTest):
		fileNameStr = testFileList[i]
		fileStr = fileNameStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])
		vectorUnderTest = img2vector('testDigits/%s'%fileNameStr)
		classifierResult = classify0(vectorUnderTest,trainingMat,hwLabels,3)
		print("the classifier came back with : %d, the real answer is : %d"%(classifierResult,classNumStr))
		if(classifierResult != classNumStr):
			errorCount += 1.0
	print("\n the total number of errors is %d" %errorCount)
	print("\n the total error rate is :%f" %(errorCount/float(mTest)))



if __name__ == '__main__':
	handwritingClassTest()
