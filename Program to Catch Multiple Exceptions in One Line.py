 # Multiple exceptions as a parenthesized tuple #
string = input()

try:
    num = int(input())
    print(string+num)
except (TypeError, ValueError) as e:
    print(e)

#Input
# a
# 2
# Output
#can only concatenate str (not "int") to str