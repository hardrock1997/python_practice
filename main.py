# x="Hello"
# print(type(x)) 

# y=3
# print(type(y))

# z=4.5
# print(type(z))

# a='c'
# print(type(a))

# b=True
# print(type(b))
#                         # dynamically typed language
# b=3
# print(type(b))


#####################################
#Type Conversions

# x=input()

# print(x, type(x))

# x_int = int(x)
# print(type(x_int))

# y=int(input())
# print(y, type(y))

# y_string = str(y)
# print(y_string, type(y_string))

# y_float  = float(y)
# print(y_float)

# "",{},[],0 ->falsy value
# "True", "False" or any other string is a truthy value

# print(bool([]), bool({}), bool(0), bool(""))
# print(bool("True"), bool("False"))

######################################
#Operators

# x="hello"
# y=x
# print(x,y)

#Integers, strings, bool and float are immutable

# x=int(input())
# y=int(input())
# add = x+y
# prod=x*y
# int_div=x//y
# div=x/y
# diff=x*y
# rem = x%y
# exp = x**y

# print(add, prod, div, diff, int_div, type(div), type(int_div), rem, exp)


# x=5
# y=2
# print(x>y, x<=y, x==y)

# s1="yash mundra"
# s2="yash"

# print(s1==s2, s1!=s2, s1<s2, s1>s2)

# x=int(input())
# y=int(input())
# z=int(input())

# #greatest of x, y and z
# if(x>y and x>z):
#     print("x",x)
# elif(y>x and y>z):
#     print("y",y)
# else:
#     print("z",z)


# n=int(input())
#print all even numbers only till n

# for i in range(n):
#     if(i%2==0):
#         print(i)
# # or
# i=1
# while i<=n:
#     if(i%2==0):
#         print(i)
#     i+=1

# i=2
# while i<=n:
#     print(i)
#     i+=2


#print sqaure of n*n made of *
# n=int(input())
# j=1
# while j<=n:
#     s=""
#     i=1
#     while i<=n:
#         if(i<n):
#             s=s+"* "
#         else:
#             s=s+"*"
#         i+=1
#     print(s)
#     j+=1

# print a matrix of n*m made of *
# n=int(input())
# m=int(input())

# i=1
# j=1
# while i<=n:
#     s=""
#     j=1
#     while j<=m:
#         if(j<m):
#             s+="* "
#         else:
#             s+="*"
#         j+=1
#     print(s)
#     i+=1

# s="yash"
# print(s*3, len(s*3))

# s="yash"
# print(s[-4],s[0], s[0:4])

# s="yashMundra"
# print(s[1:6:2])
 #from the range [1,6) and pick characters on the jump of two

# s="Yash"
# print(s.find("as"), s.index("as")) 
#gives the starting index of the string that we want to find

# s="yash_mundra"
# print("_" in s)
# print("t" not in  s)
#membership operator, tells whether the substring is present in the string or not


# s="Yash"
# s[3]="XX"
# print(s)
# assignment is not allowed in strings as strings are immutable in python

# s="yash_mundra"
# s=s[:4]+"___"+s[5:]
# print(s)
#created the copy of the string before and after the index where we want to change and then assign the value back

# a=10
# print(id(a))
#memory location of the variable s
#immutable types points to the same memory location
#mutable types on the other hand are given different memory locations

# s="hello"
# s1="hello"

# a=[1,2,3]
# b=[1,2,3]

# print(s is s1)
# print(a is b)
#Identity operator (is) checks if the variables are having the same memory address

# print(s==s1)
# print(a==b)
# == checks the content and not if their id (memory addresses) are same or not
