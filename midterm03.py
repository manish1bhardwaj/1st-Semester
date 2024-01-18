# write the python programme to remove the vowels from the strings ?

str= input("enter the strings : ")
vowels="aeiouAEIOU"
res=""
for i in str:
    if i not in vowels:
        res +=i
print(res)        
