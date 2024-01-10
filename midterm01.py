'''Write a Python program that takes an integer n as input and 
prints the sum of all numbers from 1 to n that are divisible by both 2 and 3.
Use a for loop for this task.'''

a = int(input("enter the number"))
b=0
for i in range(a+1):
    if a%2==0 and a%3==0:
       b+=1
print("the sum of all number is",b)       
