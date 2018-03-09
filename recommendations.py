cirtics = {
'WangWenJun':{'Lady in Water':2.5,'Snakes on a Plane':3.5,'Just My Luck':3.0,'Superman Returns':3.5,'You,Me and Dupree':2.5,'The Night Listener':3.0},
'WangBing':{'Lady in Water':3.0,'Snakes on a Plane':3.5,'Just My Luck':1.5,'Superman Returns':5.0,'You,Me and Dupree':3.5,'The Night Listener':3.0},
'MenShuCheng':{'Lady in Water':2.5,'Snakes on a Plane':3.0,'Superman Returns':3.5,'The Night Listener':4.0},
'LuJingXia':{'Snakes on a Plane':3.5,'Just My Luck':3.0,'Superman Returns':4.0,'You,Me and Dupree':2.5,'The Night Listener':4.5},
'ZhouJieLun':{'Lady in Water':3.0,'Snakes on a Plane':4.0,'Just My Luck':2.0,'Superman Returns':3.0,'You,Me and Dupree':2.0,'The Night Listener':3.0},
'YangQianHua':{'Lady in Water':3.0,'Snakes on a Plane':4.0,'Just My Luck':3.0,'Superman Returns':5.0,'You,Me and Dupree':3.5},
'ChengYiXun':{'Snakes on a Plane':4.5,'You,Me and Dupree':1.0,'The Night Listener':4.0}
}

from math import sqrt

# 欧几里得距离评价
def sim_distance(prefs, person1, person2):
	si = {}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item] = 1

	# 判断是否有相同的电影，没有则返回0
	if len(si) == 0:
		return 0

	sum_of_squares = sum([pow(prefs[person1][item]-prefs[person2][item], 2) 
		for item in prefs[person1] if item in prefs[person2]])

	return 1/(1+sqrt(sum_of_squares))

print(sim_distance(cirtics,'WangWenJun','WangBing'))

def sim_person(prefs, person1, person2):
	si = {}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item] = 1

	n = len(si)

	if n==0:return 1

	# 求和
	sum1 = sum([prefs[person1][it] for it in si])
	sum2 = sum([prefs[person2][it] for it in si])

	# 平方和
	sqSum1 = sum([prefs[person1][it]**2.0 for it in si])
	sqSum2 = sum([prefs[person2][it]**2.0 for it in si])

	# 乘积之和
	pSum = sum([prefs[person1][it]*prefs[person1][it] for it in si])

	num = pSum-(sum1*sum2/n)
	den = sqrt((sqSum1-pow(sum1,2)/n)*(sqSum2-pow(sum2,2)/n))

	if den==0:return 0

	return num/den

print(sim_person(cirtics, 'WangWenJun','WangBing'))

def topMatches(prefs, person, n=5, similarity = sim_person):
	scores = [(similarity(prefs, person,other),other) for other in prefs if other!=person]

	scores.sort()
	scores.reverse()
	return scores[0:n]

print(topMatches(cirtics,'WangWenJun'))