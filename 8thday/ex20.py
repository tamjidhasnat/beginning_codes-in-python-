class de:
    def by_7(self,n):
        for i in range(1,n+1):

            if i%7==0: yield i

d=de()
ge=d.by_7(int(input('enter number = ')))
for i in ge:
    print(i)
                

