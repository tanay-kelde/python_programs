start = int(input("Enter the lower bound: "))
stop = int(input("Enter the upper bound: "))
print("Prime numbers between", start, "and", stop, "are:")
for num in range(start, stop):
  if num > 1:
    for i in range(2, num):
      if (num % i) == 0:
        break
    else:
      print(num, end=" ")