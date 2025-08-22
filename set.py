
#create an empty set by s=set(), s={} cannot because it then conflicts with declaring an empty dictionary

s={"apple", "banana", "orange", "pineapple","apple"}

print(s, type(s), len(s))
#not ordered in nature, the order of insertion is not maintained as the hash of the items can place them in any order
#no duplicates are there in a set

for item in s:
    print(item)

if "apple" in s: #for chcking if the item is present in the set or not 
    #internally the hash of the item is calculated and at the hash slot, its checked whether the item is present there or not 
    print("yes apple is present")

l=list(s)
t=tuple(s)
print(type(l), type(t), l, t)

print(hash(t))
print(hash("apple"))
print(hash(1))              #these all are hashable (Immutables)
print(hash(True))
print(hash(False))
print(hash(2.5))
# print(hash(l)) #lists are non hashable
    #lists and sets are mutables
# print(hash(s)) #set is also non hashable
'''
for mutables , the hash() is not defined as say if the list has some value added or removed then their hash value will keep on changing
'''
#non hashables cannot be used in set
#hashables can be used inside the set


s.add(5) #adding new element in a set
print(s)
s1={2,3,4,5}
s.update(s1) #adding all the elements of the set s1 in s
print(s,"now")

s.remove("apple") #if we try to remove an element that is not in the set then it will throw KeyError
s.discard(5) #this will not throw that error
print(s)
#s.clear() clearing out the entire set


s2={3,1,2,3,4}

union=s1.union(s2)
intersection=s1.intersection(s2)
symm_diff = s1.symmetric_difference(s2) #all elements of s1,s2 and no common elements of s1 and s2

print(union, intersection, symm_diff)
