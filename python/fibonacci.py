number=int(input("Limit: "))
def fibo(num):
	fiboList=[]
	i=1
	if num==0:
		fiboList=[]
	elif num==1:
		fiboList=[1]
	elif num>=2:
		fiboList=[1,1]
		while i<num-1:
			tmp=fiboList[i]+fiboList[i-1]
			fiboList.append(tmp)
			i+=1
	return fiboList

print(fibo(number))