net=0



while True:
    
    data=input().split(" ")
    
    w,d=map(str,data)
    if w=="D":  
        net+=int(d)

    if w=="W":
        net-=int(d)
    if w=="T":
        break

print("total money = ",net)
