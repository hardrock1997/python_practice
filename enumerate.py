'''
enumerate() creates a tuple with the first value as the index and the second value as the element,s value of an iterable container
'''
l=[1,2,3,4]
s={1,2,3,4}
t=(1,2,3,4)
enumerate_object_as_list = list(enumerate(t))
enumerate_object_as_set = set(enumerate(t))
enumerate_object_as_tuple = tuple(enumerate(t))

print(enumerate_object_as_list)
print(enumerate_object_as_set)
print(enumerate_object_as_tuple)

for item in enumerate(l):
    print(item[0], item[1])

for item in enumerate(s):
    print(item[0], item[1])

for item in enumerate(t):
    print(item[0], item[1])

#item is the tuple of (index, value) of the iterable, item[0] is the index and item[1] is the value