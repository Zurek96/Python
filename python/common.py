a=[1, 2, 3, 4, 5, 6]
b=[4, 5, 6, 7, 6, 9]
common=[]
for i in b:
	if i in a:
		common.append(i)
print(set(common))