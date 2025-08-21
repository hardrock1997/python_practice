# # Immutable form of the list DS
# tup=(1,2,3,4,4,5,5,6)
# print(len(tup), tup[0], tup[3], tup[-1], tup[0:5:1])
# n=len(tup)
# print(tup[1-n:-1])
# # tup.reverse()
#             #reverse() and sort() are not defined in tuple class
# # tup.sort()
# print(tup)
# tup1=("yash","follow")
# tup=tup+tup1
# print(tup)
# # tup[0]="changing"# cannot do this as tuple is an immutable DS
# print(tup)

# # tup.extend(tup1)#extend() is also not defined for tuples
# # tup.append(9)# append() is also not defined
# # tup.insert(n-1,10)#insert() is also not defined for tuples
#remove(), pop() are also not defined in tuples

# tup=([1,2,3],4,5,6,(7,8,9))
# l=list(tup)
# t=tuple(l)
# print(tup, l,type(l), type(t))

# t=(1,2,(4,5),6,[7,8])
'''
we say that tuple is an immutable but doing 
t[4][0]="changed" , how are we able to mutate the tuple?


in memory, 1,2,6
the memory reference of the list
the memory reference of the tuple
tyring to change anything in the list is actually making in the change
in the list where its actually stored and the tuple t only has the 
reference of it and since list is mutable so its correct

IMP: tuples can be mutated iff the mutation is done on some
mutable that is inside the tuple
'''
# t[4][0]="changed"
# print(t)