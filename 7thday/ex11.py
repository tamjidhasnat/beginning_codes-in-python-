def binaryToDecimal(binary): 
      
    binary1 = binary 
    decimal, i, n = 0, 0, 0

    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    if decimal % 5==0:

        print(binary1," , This binary is devisible by 5 ") 

   
n=3      

for i in range (1, n+1): 
    fq=int(input('enter binary number : '))   
    binaryToDecimal(fq)
   
