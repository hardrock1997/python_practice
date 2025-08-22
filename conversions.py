l=[1,2,3,1,5]
t=(2,1,3,5,1)
s={2,1,3,5}

list_to_tuple=tuple(l)
set_to_tuple=tuple(s)

list_to_set=set(l)
tuple_to_set=set(t)

set_to_list=list(s)
tuple_to_list=list(t)

print(list_to_tuple,set_to_tuple)
print(list_to_set,tuple_to_set)
print(set_to_list,tuple_to_list)

#in all of these conversions, the nested items will not be converted
#only hashables inside the container will can convert to the set without any error

L=["apple", "orange","banana"]
#make a single string with space in between them
joined = " ".join(L) # a single string, join() only works on the iterable of strings
splitted = joined.split(" ") #a list
print(joined, type(joined), splitted, type(splitted))

s={"1","2","3","4"}
set_joined_string=" & ".join(s)
print(set_joined_string)

tup = ("34", "45")
tuple_joined_string = " $ ".join(tup)
print(tuple_joined_string)