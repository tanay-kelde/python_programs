# file my_file.txt is

# honda 1948
# mercedes 1926
# ford 1903

# Open file in append mode and write to it #

with open("my_file.txt", "a") as f:
   f.write("new text")