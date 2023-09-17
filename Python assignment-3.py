# Write a program to print a given string in reverse order.
def reverse(s):
    str= " "
    for i in s:
        str = i + str
    return str
str_g='my name is abhi'
print(str_g)
print(reverse(str_g))

