# create an empty dictionary by d=dict() or d={}

dict = {
    "name":"Yash Mundra",
    "hobbies":["music", "coding","travelling"],
    1:{
        "nested_key":"nested_value"
    },
    1:"new value",  #this will override the value for the key:1
    (1,2):"hashable"
}

#like set, keys here also needs to be hashable(all immutables can be the key)

print(dict, type(dict))
'''
hash value for each key is calculated and a value is stored in the mapped slot to that hash value
'''
print(dict["name"], dict.get("name")) # to access the value corresponding to a key
#diff between the two:if the key is not there then [] will throw keyError and get() will simply return None

print("name" in dict) #to check if the key exists in the dictionary
#DICTIONARY IS AN ORDERED CONTAINER IN THE ORDER OF THE INSERTION OF KEYS

#dictionary is a mutable container, mapped values to the keys can be changed
dict["name"]="ram"
print(dict)

dict["new_key"]="ram"
print(dict)
'''
if the key we are trying to update DNE in the dictionary then a new key value pair is created with that key
if it exists then the value is simply changed with the new value that we are using
'''

dict.pop("name") #remove the key name from the dictionary
print(dict)

dict.popitem() #removes the last added key value pair
print(dict)

# dict.clear()#empties the entire the dictionary


d={
    "name":"yash",
    "age":28,
    1:"number",
    2.5:"floating value",
    True:"boolean",
    False:"boolean",
    (1,2,"tuple"):"tuple"
}

#iterating without using any internal methods of the dictionary
for key in d:
    print(key, d[key])

#iterate on only the keys: d.keys() returns a list of the keys of the dictionary
for key in d.keys():
    print(key)

#iterate on only the values: d.values() returns a list of the values of the dictionary
for value in d.values():
    print(value)

#d.items() returns the tuple of the key:value  pair
for item in d.items():
    print(item, item[0], item[1]) #since item is a tuple, item[0] is the key and item[1] is the value