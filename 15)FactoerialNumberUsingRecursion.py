def factorial(num):
    if (num == 1 or num == 0):
        return 1
    else:
            return (num*factorial(num-1))


num = 5
print(" the factorial number is: ",factorial(num))






