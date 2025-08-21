
fn=["Yash","Ram","Harsh"]
ln=["Mundra","Lakshman"]
an=[28,29,30]

x=zip(fn,ln,an)
print(type(x))

for i in x:
    print(i, type(i))

'''
zip() can be used on any container that is iterable
it maps the elements of all the iterables according to their indices
for each of the mapped items, a new tuple is created
if there is no item which can be mapped then that is not included in the
resulting tuples
Eg: for Harsh in fn there is no item in ln, so its not included in the
resulting tuples
by zipping the elements , they can be iterated by for loop as well

output:
<class 'zip'>
('Yash', 'Mundra', 28) <class 'tuple'>
('Ram', 'Lakshman', 29) <class 'tuple'>
'''