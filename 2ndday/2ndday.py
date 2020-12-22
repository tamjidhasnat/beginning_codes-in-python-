
fund=["arif","rahim","karim"]
reserver=["1","2"]
fund.append("nabid")
fund.insert(0,"abir")
fund.extend(reserver)
print(fund[4:])
print(" new list = " + str(fund))
fund.sort() 
rev=fund.copy()
print(fund)
print(rev)
rev.reverse()
print(rev)

req=(1,5)

print(req)


def desire(alias):
	print(alias+"you are being watched")
desire("nasif, ")
life= int(input("enter the number "))

if life==1:
	print("life is beautiful\n")

else:
	print("irrelavent\n")	
	
i=0
while i<5:
	print("there is a matrix in a matrix\n")
	i+=1	
	
word="desire"
guess=""


while guess!=word:
       guess=input("Guess the word ")
       if guess==word:
       	print("win")
	
	
	
