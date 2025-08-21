# l=[1,2,3,"hello",4.5]
# n=len(l)
# print(n,l[0],l[n-1],l[-n],l[0:n],l[0:3:1], type(l))

# #mutable type
# l1=[1,2,3,"hello",4.5]
# print(l==l1, l1 is l,id(l),id(l1))

# l[0:3]="hello"
# print(l)

# nested = [[1,2],[3,4]]
# for i in range(len(nested)):
#     for j in range(len(nested[i])):
#         print(nested[i][j])

# l1.insert(2,"Yash") #adding "Yash" at index 2 in the list
# l1.append("Mundra") # always insert at the end
# print(l1)

# l2=[1,2,3,4,5]
# for i in range(len(l2)):
#     l1.append(l2[i])

# print(l1)

# l1.append(l2)
# print(l1) #this will simpley put the entire list as the element in the end

# l1.extend(l2)
# print(l1) #this will put each element of the list as an individual element


# l1.append("Yash")
# l1.remove("Yash") #remove the first occurrence 

# l1.pop(0)
# l1.pop()

# L=[1,2,3,4]
# L.pop() #if the index is not provided then the last element is removed
# print(L)

#Removing index from list
    #by index
    #pop(index) or pop()

    #by value
    #remove(<value to be removed>)

#Adding into the list
    #adding at an index
    #insert(index, <value to add>)

    #at the end
    #append(<value> to add)

    #for adding a list (not as a nested one)
    #extend(<list>)

# clear the entire list
    #clear()

#ways of iterating on the list (iterable)
# l=[1,2,3,4]
# for i in range(len(l)):
#     print(l[i])

# for ele in l:
#     print(ele)

# i=0
# while i<len(l):
#     print(l[i])
#     i+=1

# l=["yash", "mundra"]
# for ele in l:
#     for char in ele:
#         print(char)

# m=range(1,6)
# print(type(m), len(m), m[0], m[-1])
# #creates an iterable of numbers from 1 to 5

# for ele in m:
#     print(ele)

# m=range(1,6,2)
#numbers 1 to 5 with a jump of 2

#print odd numbers from 1 to 100 and store in a list
# l=[]
# for number in range(1,100):
#     if(number%2==0):
#         continue
#     else:
#         l.append(number)

# print(l)

############### Sorting and reversing a list
# l=[1,2,3,4,5]
# l.reverse()
# print(l)

# l.sort()
# l.reverse()
# l.sort(reverse=True)
# print(l)

# l1=["apple","aeroplane","air"]
# l1.sort() #sorted lexographically
# print(l1)

# l=[1,2,3,4]
# sortedList = sorted(l) #returns another list which is sorted
# print(sortedList)

# l=[1,2,3,4]
# l1=[5,6,7,8]
# print(l+l1, l*3, l1*5)

#given a space separated numbers from the user as the input, sort them
# x = input().split(" ") #array of numbers which are strings as of now (user entering the numbers)

# for i in range(len(x)):
#     x[i]=int(x[i])

# x.sort()
# print(x, type(x),x)
