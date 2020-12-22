import math
x,y=0,0
print("enter \"Result\" to show the result")
while True: 
   
    s=input().split(' ')
    if  s[0]=='Result':    
        break
    if s[0]=='UP':
        x-=int(s[1])    
    if s[0]=='DOWN':
        x+=int(s[1])
    if s[0]=='RIGHT':
        y+=int(s[1])
    if s[0]=='LEFT':
        y-=int(s[1])

di=round(math.sqrt(x**2+y**2)) 
print(di)   
