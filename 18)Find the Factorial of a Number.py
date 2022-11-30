# import math  
# def fact(n):  
#     return(math.factorial(n))  
  
# num = int(input("Enter the number:"))  
# factorial = fact(num)  
# print("factorial of the given number is: ",factorial)  




# find factorial number

n = int(input (" enter the number: " ))
factorial = 1
if n >= 1:
 for i in range (1, n+1):
       factorial = factorial *i

print("factorial of the given number is: ", factorial)
