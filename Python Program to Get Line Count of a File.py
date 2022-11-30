# file my_file.txt is

# honda 1948
# mercedes 1926
# ford 1903


# Using list comprehension #
num_of_lines = sum(1 for l in open('my_file.txt'))

print(num_of_lines)
