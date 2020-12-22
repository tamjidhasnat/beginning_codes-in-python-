cols=int(input('enter collumns = '))
rows=int(input('enter rows = ')) 
arr=[] 
for i in range(cols): 
    col = [] 
    for j in range(rows): 
        col.append(int(input())) 
    arr.append(col) 
print(arr)
print("the ans is = " , arr[int(input('enter n-1 row '))
][int(input('enter n-1 collumn '))])
