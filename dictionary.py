"""---------------------------Dictionary---------------------------------------------------------------------
1. It is used to represent group of keys and value pair into single entity or object.
2. Insertion order is not preserved.
3. Hectrogeneous keys and values allowed.
4. Dublicate keys not allowed but values can be dublicated but not suggested.
5. Immutable object are allowed for keys
A Dictionary is a example of a keys and values store also known as Mapping in Python. It allows you to stroe and tetritive
elements by referencing a key. As dictionaries are referenced by key. They have very fast lookups. As they are primarily
used for referencing item by key they are not sorted.
They are two ways to create dictionary object.
1. By using brases {}
   Example
   d1 = {'name':'Dileep','age':45}
2. By using dict() method
   Example
   d2 =dict(name='Dileep',age=45)
Method of Dictionary
1. keys()
2. values()
3. items()
4. clear()
5. popitem()
6. get()
7. update()
"""
# d1 = {'name':'Dileep','age':45}
# print(d1['name'])
# print(d1['age'])
# print(d1.keys())
# print(d1.values())
# print(d1.items())
# Dileep
# 45
# dict_keys(['name', 'age'])
# dict_values(['Dileep', 45])
# dict_items([('name', 'Dileep'), ('age', 45)])
#d2 =dict(name='Dileep',age=45)
# print(d2['name'])
# print(d2['age'])
# print(d2.keys())
# print(d2.values())
# print(d2.items())
# Dileep
# 45
# dict_keys(['name', 'age'])
# dict_values(['Dileep', 45])
# dict_items([('name', 'Dileep'), ('age', 45)])
#print(d2.copy())
d=dict(name='Krishna',age=45,salary=35000)
# print(d.keys())
# dict_keys(['name', 'age', 'salary'])
# print(d.values())
# dict_values(['Krishna', 45, 35000])
# print(d.items())
# dict_items([('name', 'Krishna'), ('age', 45), ('salary', 35000)])
# print(d.popitem())
# ('salary', 35000)
# print(d.copy())
# {'name': 'Krishna', 'age': 45, 'salary': 35000}
# s=dict(job="Developer",sex='male',location='Hydrabad')
# d.update(s)
# print(d)
# {'name': 'Krishna', 'age': 45, 'salary': 35000, 'job': 'Developer', 'sex': 'male', 'location': 'Hydrabad'}
# print(d.get('name'))
# Krishna
# print(d.get('age'))
# 45
# d.clear()
# print(d)
# {}
table={'1975':'Holy Grail','1979':'The meaning of life','1983':'Life of Brain'}
# for year in table:
#     print(year,"\t",table[year])
# 1975     Holy Grail
# 1979     The meaning of life
# 1983     Life of Brain
# V='1975'
# print([value for key, value in table.items() if key==V])
# ['Holy Grail']
#Note keys need not always be string
# table.clear()
# d={}
# d['name']='Satya'
# d['Id']=1001
# d['age']=27
# print(d)
# Matrix={}
# Matrix[(2,3,4)]=88
# x,y,z= 2,3,4
# print(Matrix[(x,y,z)])
# 88
# Matrix[(4,5,6)]=99
# print(Matrix)
# {(2, 3, 4): 88, (4, 5, 6): 99}
# rec={}
# rec['name']='Satya'
# rec['age']='27'
# rec['job']='Developer'
# print(rec)
# {'name': 'Satya', 'age': '27', 'job': 'Developer'}
rec={
    'name':'Satya','jobs':['Developer','Manager'],
    'mailid':'satya.1234@gmail.com','home':{'state':'Hydrabad','zip':12453}
}
# print(rec['name'])
# Satya
# print(rec['jobs'])
# # ['Developer', 'Manager']
# print(rec['jobs'][1])
# Manager
# print(rec['home'])
# {'state': 'Hydrabad', 'zip': 12453}
# print(rec['home']['zip'])
# 12453
"""
----------Dictionary Comprehension--------------------------------------
"""
# print({x:x*x for x in (1,2,3,4)})
# {1: 1, 2: 4, 3: 9, 4: 16}
# Or
# print(dict((x,x*x) for x in (1,2,3,4)))
# {1: 1, 2: 4, 3: 9, 4: 16}
# Write a program to swapp key value in dictionary
# my_dict={1:'a',2:'b',3:'c'}
# print({v:k for k, v in my_dict.items()})
# {'a': 1, 'b': 2, 'c': 3}
# or
# print(dict((v,k) for k, v in my_dict.items()))
# {'a': 1, 'b': 2, 'c': 3}
"""
---------------------------Merging Dictionary-------------------------------------------
Combine dictionary and optinally override old values with a nested dictionary comprehension.
"""
# d1={'w':1,'x':1}
# d2={'x':2,'y':2,'z':2}
# print({k:v for d in [d1,d2] for k, v in d.items()})
# {'w': 1, 'x': 2, 'y': 2, 'z': 2}