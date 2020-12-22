s=input().split()

for i in s:
    if s.count(i) > 1:
        s.remove(i)
s.sort()
print(" ".join(s))
