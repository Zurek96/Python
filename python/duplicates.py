list=[1,1,1,2,2,3,3,4,4]

def manSet(list):
	list2=[]
	for i in list:
		if i not in list2:
			list2.append(i)
	return list2

def autoSet(list):
	list=set(list)
	return list

print(manSet(list))
print(autoSet(list))