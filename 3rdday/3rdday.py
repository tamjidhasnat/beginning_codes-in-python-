def mat(number,times):
	d=1
	for i in range(times):	
		d=d*number
	return d
n=int(input('enter number '))
t=int(input('times '))
print("result = ",mat(n,t))


"""number_list=[]
i=0
while i<3:
	number=input()
	i+=1
	number_list.append(number)
print(number_list)
"""

"""array=[
[1,2,5,7],
[8,4,6,9,],
[0,0,12,22],
[0]
]

print(array[2][2])
"""
"""try:
	number=int(input('enter the number = '))
	print("valid")
except:
	print("invalid input")	
	"""
	
