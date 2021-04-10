import re
import csv
# This function is use for cound Total no of word in text file
def wordcound(data):
    fo = None
    try:
        fo = open(data)
        data = fo.read()
        print(data)
        res= data.split()
        print("Total No of Word : ",len(res))
    except FileNotFoundError:
        print("Regarding file could not be loaded")
    finally:
        if fo:
            fo.close()
# This function is use for dispaly all parlidrom word in a text file
def parlidromdisplay(data):
    fo = None
    try:
        fo = open(data)
        data= fo.read()
        res = data.split()
        for word in res:
            rev= word[::-1]
            if word == rev:
                print(word)
    except FileNotFoundError:
        print("Required file not be exits")
    finally:
        if fo:
            fo.close()
# This function is use for count unique parlidrom word in text file
def uniqueparlidrome(data):
    fo = None
    ls=[]
    try:
        fo= open(data)
        data= fo.read()
        res=data.split()
        for word in res:
            if word==word[::-1]:
                if word not in ls:
                    ls.append(word)

        print("Unique Parlidrom Word Count in file : ",len(ls))
    except FileNotFoundError:
        print("Required file not be exits")
    finally:
        if fo:
            fo.close()
def maxparlidrome(data):
    fo = None
    ls=[]
    try:
        fo= open(data)
        data= fo.read()
        res=data.split()
        for word in res:
            if word==word[::-1]:
                if word not in ls:
                    ls.append(word)
        maxlen= sorted(map(lambda s: len(s.strip()),ls),reverse=True)      
        print("Maximum length of Parlidrom Word  : ",maxlen[0])
    except FileNotFoundError:
        print("Required file not be exits")
    finally:
        if fo:
            fo.close()
def reversestring(data):
    fo = None
    try:
        fo= open(data)
        data= fo.read()
        res=data[::-1]      
        print("Reverse of string  : ",res)
    except FileNotFoundError:
        print("Required file not be exits")
    finally:
        if fo:
            fo.close()
def removedublicate(data):
    nodublicate=""
    for ch in data:
        if ch not in nodublicate:
            nodublicate= nodublicate + ch
    print("Unique letter : ",nodublicate)
# Write a program to print all anagram word in the text file
def allanagram(data):
    fo = None
    try:
        fo= open(data)
        alldata = fo.read()
        res= alldata.split()
        mydict={}
        for word in res:
            key=''.join(sorted(word))
            if key in mydict.keys():
                mydict[key].append(word)
            else:
                mydict[key]=[]
                mydict[key].append(word)
        print("All anagram words in the text file: ")
        for key, val in mydict.items():
            if len(val)>1:
                print(val)
    except FileNotFoundError:
        print("File can't be opened !")
    finally:
        if fo:
            fo.close()
def countwordtocsv(data):
    fo = None
    try:
        fo= open(data)
        mydata= csv.reader(fo)
        res=list(mydata)
        for sentence in res:
            for word in sentence:
                words=word.split()
        print("Total words in csv file :",len(words))
    except FileNotFoundError:
        print("csv file can't be opened !")
    finally:
        if fo:
            fo.close()
def stringformat(mystr):
    nodublicate=""
    for ch in mystr:
        if ch not in nodublicate:
            nodublicate= nodublicate + ch
    print("Input :",mystr)
    print("Output : ",end=" ")
    for c in nodublicate:
        n=mystr.count(c)
        print(c+str(n),end="")
    print()    
if __name__=='__main__':
    #wordcound('data.txt') # call wordcound function
    #parlidromdisplay('data.txt') #call parlidromdisplay function
    # uniqueparlidrome('data.txt') # call unique
    # maxparlidrome('data.txt')   # call function for max length of parlidrom
    # reversestring('data.txt')  # call the function for reverse of string
    # removedublicate("Hello")   # remove dublicate value
    # stringformat("aaaaabbbbccccdd") #i/p aaaaabbbbccccdd o/p a5b4c4d2
    #allanagram('data.txt')
    countwordtocsv("mydata.csv")

    

    
    
    

        
