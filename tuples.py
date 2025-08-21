
#create an empty tuple by t=tuple() or t=()

# Immutable form of the list DS -> Tuple
tup = (1, 2, 3, 4, 4, 5, 5, 6)

# Length of tuple, indexing, negative indexing, slicing
print(len(tup), tup[0], tup[3], tup[-1], tup[0:5:1])

# Negative indexing with length-based slicing
n = len(tup)
print(tup[1-n:-1])   # same as tup[ -7:-1 ]

# Note: reverse() and sort() are not defined in tuple class
# tup.reverse() ❌
# tup.sort()    ❌
print(tup)

# Tuples can be concatenated (returns a new tuple)
tup1 = ("yash", "follow")
tup = tup + tup1
print(tup)

# tup[0] = "changing"  # ❌ Cannot do this (tuples are immutable)
print(tup)

# Methods like extend(), append(), insert(), remove(), pop() 
# are also not defined for tuples (only for lists)
# tup.extend(tup1) ❌
# tup.append(9) ❌
# tup.insert(n-1, 10) ❌
# tup.remove(3) ❌
# tup.pop() ❌

# Tuple containing nested mutable & immutable objects
tup = ([1, 2, 3], 4, 5, 6, (7, 8, 9))

# We can convert tuple -> list and back
l = list(tup)
t = tuple(l)
print(tup, l, type(l), type(t))

# Tuple containing list (mutable) inside it
t = (1, 2, (4, 5), 6, [7, 8])

'''
we say that tuple is an immutable but doing 
t[4][0]="changed" , how are we able to mutate the tuple?

in memory, 1,2,6
the memory reference of the list
the memory reference of the tuple
trying to change anything in the list is actually making the change
in the list where it’s actually stored and the tuple t only has the 
reference of it and since list is mutable so it’s correct

IMP: tuples can be mutated iff the mutation is done on some
mutable that is inside the tuple
'''
t[4][0] = "changed"   # ✅ This works because [7,8] is a mutable list
print(t)
