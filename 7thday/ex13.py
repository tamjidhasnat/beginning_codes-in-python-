sen=input()
letter=0
d=0
for i in sen:
    if ('a'<=i and 'z'>=i) or ('A'<=i and 'Z'>=i):
        letter+=1
    elif('0'<=i and '9'>=i):
        d+=1   

print("letter = " ,letter,"\nword = ",d)
