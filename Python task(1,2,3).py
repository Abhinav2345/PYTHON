# Write a program to make a list and square its each element and add them to elements of second list.
list1=[1,3,5,7,9]
list2=[2,4,6,8,10]
print(list1)
print(list2)
for i in range(len(list1)):
    list1[i]=list1[i]**2
print(list1)
for i in range(len(list2)):
    list2[i]=list1[i]+list2[i]
print(list2)

# Write a program to print sum of 'n' numbers.
n=int(input("Enter a number:"))
sum=0
for i in range(n+1):
    sum+=i
print(sum)

# Write a program to print a given string in reverse order.
def reverse(s):
    str= " "
    for i in s:
        str = i + str
    return str
str_g='my name is ansh'
print(str_g)
print(reverse(str_g))
