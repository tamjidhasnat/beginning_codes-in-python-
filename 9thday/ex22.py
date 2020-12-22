s=input().split()

sor=sorted(set(s))
print(sor)
for i in sor:
    print("{}:{}".format(i,s.count(i)))
