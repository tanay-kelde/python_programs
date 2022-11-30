# Let the content of the file data_file.txt be

# honda 1948
# mercedes 1926
# ford 1903

# Using for loop and list comprehension #
with open('data_file.txt') as f:
    content_list = [line for line in f]

print(content_list)

# removing the characters
with open('data_file.txt') as f:
    content_list = [line.rstrip() for line in f]

print(content_list)