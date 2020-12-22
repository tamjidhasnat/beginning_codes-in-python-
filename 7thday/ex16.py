q=input().split(',')
s=[]
q = [int(i) for i in q]  # converts string to integer
for i in q:   
    if i%2!=0:
        i=i*i
        s.append(i)

s = [str(i) for i in s]   # All the integers are converted to string to be able to apply join operation
print(",".join(s))
