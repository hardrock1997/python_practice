import copy
# def sum(c,a=10,b=20): #default arguments have to be at the end
#     return a+b+c

# x=sum(30)
# print(x)

# def func(a,b,c): #parameters
#     print(a,b,c)

# func(10,20,30) #positional arguments
# func(c=30,a=20,b=10) #keyword arguments

#mixture of keyword and positional arguments
# def fun(a,b, /, c,d, *,e,f):  
#     print(a,b,c,d,e,f)

# fun(10,20,c=30,d=40,f=20,e=45)


#Important:
#default and keyword arguments should be at the end
#poisitional arguments should be at the starting
#parameters before / are positional, after * are keyword only and c and d can be anything


# def func(name, *args): #positional arbitrary arguments, type(args)=>tuple
#     print(name, args, type(args))

# func("Yash", 1,2,3,4,5,6,7,8)
# func("Yash", [1,2,3,4,5])

# def func(name, **kwargs): #keyword arbitrary arguments, type(kwargs)=>dictionary
#     print(name, kwargs, type(kwargs))

# func("Yash", a=10,b=20,c=30)

#Passing by value and passing by reference for the arguments
#in python only the concept pass by object reference is there.

# def fun(a,b,c):
#     a=a+1
#     b+=1
#     c+=1
#     print(a,b,c, "Inside")

# a=10
# b=20
# c=30                                #for the immutables: it behaves like pass by value
# fun(a,b,c)
# print(a,b,c,"Outside")

# def fun2(a,b,c):
#     a+="1"
#     b+="2"
#     c+="3"
#     print(a,b,c,"Inside")
# a="yash"
# b="mundra"
# c="rinku"
# fun2(a,b,c)
# print(a,b,c,"Outside")


# def func3(l):
#     l.append(10)            #for the mutables: it behaves like pass by reference
#     print(l,"Inside")

# p=[1,2,3]
# func3(p)
# func3(p.copy()) #making a copy and then passing but this copy is a shallow copy
# func3(copy.deepcopy(p)) #this is the deepcopy, nested lists or nested mutables are also copied and then passed
# print(p,"Outside")


#Scopes

# x=100
#         # global scope
# y=200
# def fun():
#     print(x)
# fun()
# print(x)

# def fun():
#     x=200 #local scope
#     x+=100
#     print(x,y)
# fun()
# print(x,y)

# def fun():
#     x=200
# fun()
# print(z) #z is not defined error as z was in the local scope and it gets detroyed once the function is executed

#LEGB rule

# y=200
# def fun():
#     x=100
#     z=100
#     def gun():
#         print(x,y,z) #if not in the local scope ->encloding scope(parent function,s scope ->global scope)
#     gun()
# fun()

#function gun, x and z are in the local scopes of the function fun
#there is no x,y or z variables in the local scope of the gun function , so it then goes to the enclosing scope (of fun) and 
#finds x and z there but for y it goes one more step further to the global scope and finds y there

# y=100
# def f():
#     x=100
#     def g():
#         nonlocal x #now x is not in the local scope of the function g but instead is the same as the x that is in the local of f
#         x=200
#         print(x,"in g")
#         global y
#         y=300
#         print(y,"in g")
#         z=y
#         print(z)
#     g()
#     print(x,"in f")
# f()
# print(y,"changed as this global y only used inside the function g")