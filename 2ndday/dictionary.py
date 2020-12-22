weeks={
    "006":"Saturday",
    "004":"Sunday",
    "005":"Monday",
    "002":"Tuesday", 
    "003":"Thursday",
    "001":"Friday"
}


#weeks.update({input('enter key = '):input('enter data = ')})
#print(weeks.get("fri"))
#p=weeks.values()

#print(p)
"""
k =input('enter key = ')
try:
    print(weeks[k])
except KeyError:
    print(f'{k} this key is not exist')"""

k=input('enter value = ')
for i,j in weeks.items():
    #print(i)
    #print(j)
    if k==j:
        print(i)
print(weeks)    
    

"""key_list = list(weeks.keys()) 
val_list = list(weeks.values())
print(key_list[val_list.index(input('enter value = '))]) """
