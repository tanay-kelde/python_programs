# Calculate power of a number using a while loop  #
base = 3
exponent = 4

result = 1

while exponent != 0:
    result *= base
    exponent-=1

print("Answer = " + str(result))

# result = 1 * 3 * 3 * 3 * 3 = 81.#



# Calculate power of a number using a for loop #
base = 6
exponent = 8

result = 1

for exponent in range(exponent, 0, -1):
    result *= base

print("Answer = " + str(result))


# Calculate the power of a number using pow() function #
base = 3
exponent = -4

result = pow(base, exponent)

print("Answer = " + str(result))

