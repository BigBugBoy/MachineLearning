# -*- coding: UTF-8 -*-

from matplotlib.font_manager import FontProperties
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np
import operator

"""
数据集说明
文件名: KNN_02DateSet.txt
特征名：
1.每年获得的飞行常客里程数	
2.玩视频游戏所耗时间百分比
3.每周消费的冰淇淋公升数
"""

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
			classLabelVector.append(1)
		elif listFromLine[-1] == 'smallDoses':
			classLabelVector.append(2)
		elif listFromLine[-1] == 'largeDoses':
			classLabelVector.append(3)
		# classLabelVector.append(listFromLine[-1])
		index += 1
	return returnMat, classLabelVector

if __name__ == '__main__':
	file2matrix('KNN_02DateSet.txt')