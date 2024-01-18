str= input("enter the strings : ")
res=""
for i in str:
    if not("A"<=i<="Z"):
        res +=i
print(res)        
