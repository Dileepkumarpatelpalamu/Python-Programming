"""
======================================Tuple======================================
1. Tuple is used to represent of element into single entity or object.
2. Tuple's object is immutable that means element can not be modified.
3. Tuple's insertion order is preserved.
4. Dublicate element are allowed.
5. Tuple elements is identified by +ve and -ve index number.

Tuple is similar to a list except that it is fixed length and immutable. so the value in the tuple can not be changed
nor the value be added to or remove from tuple. Tuple are commonly used for small collections of value that will not
need to change, such as IP address and port no. tuple are represented with parentheses() insteed o square bracket[].
There are two ways to create tuple
1. by using parentheses():- 
    t=()
2. by using tuple() method:- method take only one argument. It can be set,list or dictionary
    t=tuple()
"""
t=tuple([10,20,30])
#print(t)
#(10, 20, 30)
# print(type(t))
# <class 'tuple'>
# t=tuple({10,20,30})
# print(type(t))
# <class 'tuple'>
# t=tuple(10,20,30) # note tuple except one arguents
# print(type(t))
# TypeError: tuple expected at most 1 argument, got 3
# Tuple comprehension is not support in python it we use it internally create generator object
# t=(x*2 for x in range(1,10,2))
# # print(t)
# # <generator object <genexpr> at 0x0113A4C0>
# for val in t:
#     print(val,end=" ")
# print()
# 2 6 10 14 18
# t=('cc','dd','aa','bb')
# tmp = list(t)
# tmp.sort()
# print(tuple(tmp))
# #('aa', 'bb', 'cc', 'dd')
# print(tmp)
# #['aa', 'bb', 'cc', 'dd']