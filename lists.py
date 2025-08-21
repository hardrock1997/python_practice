import copy

# ---------- List basics ----------
l = [1, 2, 3, "hello", 4.5]
n = len(l)
print(n, l[0], l[n-1], l[-n], l[0:n], l[0:3:1], type(l))

# Mutable type comparison
l1 = [1, 2, 3, "hello", 4.5]
print(l == l1, l1 is l, id(l), id(l1))

# Slice assignment
l[0:3] = "hello"
print(l)

# ---------- Nested list iteration ----------
nested = [[1, 2], [3, 4]]
for i in range(len(nested)):
    for j in range(len(nested[i])):
        print(nested[i][j])

# ---------- Insertion & appending ----------
l1.insert(2, "Yash")      # insert at index
l1.append("Mundra")       # append at end
print(l1)

# Adding list elements one by one
l2 = [1, 2, 3, 4, 5]
for i in range(len(l2)):
    l1.append(l2[i])
print(l1)

# Appending a list as a single element
l1.append(l2)
print(l1)

# Extending a list (flatten merge)
l1.extend(l2)
print(l1)

# ---------- Removing elements ----------
l1.append("Yash")
l1.remove("Yash")   # removes first occurrence
l1.pop(0)           # remove by index
l1.pop()            # remove last element

L = [1, 2, 3, 4]
L.pop()             # default removes last
print(L)

# ---------- Iterating a list ----------
l = [1, 2, 3, 4]
for i in range(len(l)):
    print(l[i])

for ele in l:
    print(ele)

i = 0
while i < len(l):
    print(l[i])
    i += 1

# Nested iteration
l = ["yash", "mundra"]
for ele in l:
    for char in ele:
        print(char)

# ---------- Range usage ----------
m = range(1, 6)
print(type(m), len(m), m[0], m[-1])
for ele in m:
    print(ele)

m = range(1, 6, 2)  # with step
print(list(m))

# ---------- Odd numbers in a list ----------
l = []
for number in range(1, 100):
    if number % 2 == 0:
        continue
    else:
        l.append(number)
print(l)

# ---------- Sorting & reversing ----------
l = [1, 2, 3, 4, 5]
l.reverse()
print(l)

l.sort()
l.reverse()
l.sort(reverse=True)
print(l)

l1 = ["apple", "aeroplane", "air"]
l1.sort()  # lexicographic
print(l1)

l = [1, 2, 3, 4]
sortedList = sorted(l)  # returns a new list
print(sortedList)

# ---------- List operations ----------
l = [1, 2, 3, 4]
l1 = [5, 6, 7, 8]
print(l + l1, l * 3, l1 * 5)

# ---------- User input example ----------
# (disabled input for auto-run, uncomment to use)
# x = input().split(" ")
# for i in range(len(x)):
#     x[i] = int(x[i])
# x.sort()
# print(x, type(x), x)

# ---------- Shallow vs Deep copy ----------
l1 = [1, 2, 3, 4, [1, 5], 6]

# Shallow copy
l2 = l1.copy()
l2[4][0] = "nested change"
print(l1, l2, id(l1[0]), id(l2[0]))

# Deep copy
l2 = copy.deepcopy(l1)
l1[-2][0] = "changing nested one"
print(l1, l2)

'''
if I have 2 lists: l1 and l2
all the elements' memory references are stored in the lists and not the actual values.

using l1 = l2 just points the list l2 to the same memory reference of l1

using shallow copy (copy()) copies each and every element’s memory reference to the other
list including the complex nested objects as well. Changing them will affect 
both the lists since the memory references are still the same.

using copy.deepcopy does the same thing but for the complex objects a new memory reference is
created, so making changes in them does not affect the copied list.
'''
