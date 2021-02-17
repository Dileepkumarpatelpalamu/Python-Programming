"""
    1. Set is used to represent group of elements into single entity or object.
    2. Set object are mutable that can be modify.
    3. Set insertion order not preserved.
    4. Set not allow dublicate value.
    5. Set allow hectrogenious elements.
    6. Set object not support indexing like list and tuple
    --------------------------------------------------------------------------------
    We can create set object in two ways:
    1. using set() method
       syntax- variable_name = set()
       example x= set({10,20,30})
    2. using {} brases
       syntax variable name = {10,20,30,40}
    Note :- set() method does not support multiple parameters only one parameters
         :- set object does not support indexing
"""
# x= set("python") # by using  set() method
# x={10,20,30,40}  # by using {} braces
# print(type(x))
# x = set(10,20,20) # set does not support multiple arguments only one arguments
# print(x)
# x={10,20,30,40} # set object does not support indexing
# print(x[0])
# x={True,10.23,"Ram",1256,bool} # set object suport hectrogenious element
# print(x)
"""
    There are following method to perform set operation like delete , add, update etc
    1. add() :- In set add() method is used to add a new element of set.
    2. update() :- update() method is used to add multiple element of set.
    3. discard() :- discard() method is used to remove element of set. if the specified element is not present. it
    can display error. in case of remove() method gives error()
    4. remove() :-  remove() method is used to remove element of set. if specified element is not present it gives
    error.
    5. pop() : pop() method is used remove first element of set
    6. clear(): clear() method is used to all element of set
"""
#x={12,14,20,16,18}
# x.add(20) # add() method
#x.update([20,30,40,90]) # update() method
#x.discard(10) # discard() given element not in x but does not error
#x.discard(20)  # given element in x set then it remove it
#x.pop() # it remove first element of set 
#x.clear()  # it remove all element of set
#print(x)
"""
Merge of set
1. union() or | operator- union() or | operator is used to merge two more set without dublicate value
2. intersection or & operator - intersection() or & operator return common element of two or more set
3. difference or - operator - defference or - operator is used to  difference between sets. if one set those element not
not found second then return result
4. symmetric_difference or ^ operator - symmetric_difference() or ^ operator compare both set then result display
without comman element
5. issuperset() : issuperset() method chech two or more set superset or not
6. issubset() : issubset() method is used to check two set subset or not
"""
# Merge tow set
#a = {1,2,3}
#b ={1,2,3,4,5,6}
#c = a.union(b) # union() method combine two or more set in one set dublicate value is removed
#c = a|b # result dispalyed same above above
#c = a.intersection(b) # intersection() method display comman element of set
#c= a&b # result displayed same above
#c= a.difference(b) # difference() display result element not found in set b
#c=a-b #same as  alternative of difference()
#c=b-a # display result element not found in set a
#c= a.symmetric_difference(b) # symmetric_difference() method return unique element of both set
# c=a^b # alternative of symmetric_difference() method
#print(a.issuperset(b)) # it return false
#print(b.issuperset(a)) # it return true
#print(a.issubset(b))  # It return True
#print(b.issubset(a))    # It return false
# Write a program to remove dublicate value using set
# l=[1,2,3,2,3,4,4,5,1,5]
# l = list(set(l))
# print(l)
#l1,l2=[1,2,5,3,4],[2,3,4,5,1]
#print(l1==l2) # It return False
#print(set(l1)==set(l2)) # It return True
#print(sorted(l1)==sorted(l1)) # It return True
# engineers ={'bob','sue','ann','vic'}
# managers ={'tom','sue'}
#print('bob' in engineers) # It return True
#print(engineers & managers) # It return 'sue'
#print(engineers|managers)  # It return {'bob','ann','vic','tom','sue'}
#print(managers-engineers)  # It return {'tom'}
"""==========================Set Comprehension===============================
Set comprehension is similar to list and dictionary comprehension but produces a set , which is unordered collection
 of unique element.
"""
# A set containing every value in range(5)
# print({x for x in range(5)})
# {0, 1, 2, 3, 4}
# print({x for x in range(10)})
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# print({y*2 for y in range(10)})
# {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}
# Remove dublicate value without using set
# input=[5,5,1,1,2,3,4,4,5]
# output=[]
# seen=set()
# for val in input:
#    if val not in seen:
#       output.append(val)
#       seen.add(val)
# print(output)
# [5, 1, 2, 3, 4]
# A set of even number between 1 and 10
# print({x for x in range(2,12,2)})
# {2, 4, 6, 8, 10}
# Unique alphabatic characters in string of text
# text="When in the Course of human events it becomes necessary for one people......"
# print({ch.lower() for ch in text if ch.isalpha()})
# {'u', 'r', 'b', 'c', 'i', 'n', 'v', 'p', 'y', 's', 'o', 'f', 'm', 'l', 'h', 't', 'w', 'e', 'a'}
# names ={'Fred','Wilma','Barney'}
# print({name for name in names if len(name)>5})
# {'Barney'}
# Find output
# print({i for i in [1,0,2,[],'','a'] if i})
# {1, 2, 'a'}
"""----------------Largest & Smallest items in collections----------------------
To find the largest item  in a collection heapq module has a function called nlargest, we pass it two arguments, one is
the number of items that we want to retritive, the second one is the collection name.
"""
# import heapq
# numbers=[1,4,2,100,20,50,32,200,150,80]
# # print(heapq.nlargest(5,numbers))
# # [200, 150, 100, 80, 50]
# # Similary, to find smallest item in a collection we use nsmallest function
# print(heapq.nsmallest(5,numbers))
# [1, 2, 4, 20, 32]