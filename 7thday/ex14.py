sen=input()
count=0
c=0
for i in sen:
    if i.isupper():
        count+=1
    elif i.lower():
        c+=1

print("upper case = ",count,"\nlower case = ",c ) 
