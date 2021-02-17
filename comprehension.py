import itertools
#Write a program to print square of number using list comprehension
#print([x*x for x in range(1,11)])
# sentence = "Beautiful is better than ugly"
# #print(["".join(sorted(word,key = str.lower)) for word in sentence.split()])
# # ['aBefiltuu', 'is','beertt', 'ahnt', 'gluy']
# # aBefiltuu is beertt ahnt gluy ----- for manual coding
# for word in sentence.split():
#     print("".join(sorted(word,key=str.lower)),end=" ")
# print()
#'apple'= ['a', '*', '*', '*' ,'e'] by using list comprehension
#print([ch if ch in "aeiou" else "*" for ch in "apple"])
#['0', '0.5', '1', '1.5', '2', '2.5']
# def num(i):
#     return i,i+0.5
# l=[str(x) for i in range(3) for x in num(i)]
# print(l)
#print([x.sort() for x in [[2, 1], [4, 3], [0, 1]]])
#[None, None, None]
#print([sorted(x) for x in [[2, 1], [4, 3], [0, 1]]])
#[[1, 2], [3, 4], [0, 1]]
# print([i for i in range(11) if i%2==0])
# [0, 2, 4, 6, 8, 10]
# print([i for i in range(11) if i%2==1])
# [1, 3, 5, 7, 9]
# print([2 * (x if x % 2 == 0 else -1) + 1 for x in range(10)])
# [1, -1, 5, -1, 9, -1, 13, -1, 17, -1]
# print([x if x > 2 else '*' for x in range(10) if x % 2 == 0])
# ['*', '*', 4, 6, 8]
#print([x + y for x in [1, 2, 3] for y in [3, 4, 5]])
#[4,5,6,5,6,7,6,7,8]
#print([[x + y for x in [1, 2, 3]] for y in [3, 4, 5]])
#[[4,5,6],[5,6,7],[6,7,8]]
#x = [[1,2,3],[4,5,6],[7,8,9]]
# print([[x[j][i] for j in range(len(x))] for i in range(len(x))])
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
#print([[row[i] for row in x] for i in range(len(x))])
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
#print([ [ [i + j + k for k in 'cd'] for j in 'ab'] for i in '12'])
#[[['1ac','iad'],['1bc','1bd']],[['2ac,2ad'],['2bc','2bd']]]
"""
Merge list and concotinate
"""
alist=[10,20,30,40]
blist=[20]
clist=[50,30]
#mergelist = a+b
#print(mergelist)
"""2. zip returns a list of tuples, where the i-th tuple contains the i-th element from each of the
argument
"""
# for a, b in zip(alist, blist):
#     print(a,b)
# for a,b,c in itertools.zip_longest(alist, blist, clist):
#     print(a,b,c)
#write a program to print prime no using list comprehension
# noprimes=[j for i in range(2,8) for j in range(i*2,50,i)]
# print([x for x in range(2,50) if x not in noprimes])
# line="the quick brown fox jumps over the lazy dog"
# word= line.split()
# print([[w.upper(),w.lower(),len(w)] for w in word])
#Write the program print the prime no
#print([p for p in range(2,50) if 0 not in [p%d for d in range(2,p//2+1)]])

