
def is_upper(x):
    for i in x:
        if 'A'<=i and i<='Z':
            
            return True
    return False
def is_lower(x):
    for i in x:
        if 'a'<=i and i<='z':
            return True
    return False
def is_digit(x):
    for i in x:
        if '0'<=i and i<='9':
           
            return True
            
    return False
def is_other(x):
    for i in x:
        if i=='$' or i=='#'or i=='@':
            return True
    return False       

sen=input().split(',')

s=[]

for i in sen:
    length=len(i)
    if length>=6 and length<=12 and is_upper(i) and is_lower(i) and is_digit(i) and is_other(i):
        s.append(i)
print(",".join(s))
