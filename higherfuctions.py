""" A function take a arguments as  another function know as higher order functions 
There are following functions
    1. sort(key=function,reverse=True/False)
    2. sorted(iterable object,key=function,reverse=True/False)
    3. map(fuction,iterable object)
    4. filter(fuction, iterable)
    5. reduce(function, iterable)
"""
# Exampple of sort function
# lst=["java","Python","C++","C"]
# lst.sort(key=lambda x:len(x),reverse=True)
# print(lst)
# Example of sorted function
# lst=['I', 'like', 'Python']
# data=sorted(lst,key=lambda s:len(s),reverse=True)
# print(data)
# fo = None
# try:
#     fo = open("data.txt")
#     data = fo.read()
#     j = 0
#     i = 0
#     mystr=""
#     for ch in data:
#         if ch.isalpha() or ch.isdigit() or ch.isspace():
#             i +=1
#             mystr = mystr + ch
#         else:
#             j +=1
#     print("file Contents :\n",mystr)
#     print("Total no of characters with spaces : ",i)
#     print("Total no of symbols : ",j)
# except FileNotFoundError:
#     print("File not found!")
# finally:
#     if fo:
#         fo.close()


test_str = "Hello"
print("The original string is : " + test_str)
res = {key : [] for key in test_str}  
for key, value in enumerate(test_str):
    res[value].append(key)
for key, value in res.items():
    count = test_str.count(key)
    print(key,count," ",value)