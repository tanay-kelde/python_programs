# Count Number of Digits in an Integer using while loop #
num = 3452
count = 0

while num != 0:
    num //= 10
    count += 1

print("Number of digits: " + str(count))


# Using inbuilt methods #
num = 123456
print(len(str(num)))

