a =input().split()
b=0
c=''
for i in a:
    if i[-1]=="e" or i[-1]=="E":
        b+=1
        c+=i
        c+=' '
print(b) 
print(c)       

