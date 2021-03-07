"""
----------Files in Python---------------------------------
Files are named locations on disk to store related information. They are used to permanently store data in a 
non-volatile memory
"""
# Write a function for  writing text file in python
def datawrite(data):
    f = None
    try:
        f= open(data,'w')
        f.write("I like python. it is power full programming language so i like it")
        print("file Name: ",f.name)
        print("file Mode :",f.mode)
        print("file type :",type(f))
        print("file Open :",f.close())
        f.close()
        print("file status: ",f.close())
    except FileNotFoundError:
        print("file Not Exits")
    finally:
        if f:
            f.close()
# Write a function for reading data in a file
def dataread(data):
    f=None
    try:
        f=open(data,'r')
        data=f.read()
        print(data)
    except FileNotFoundError:
        print("entered file not found:!!!!")
    finally:
        if f:
            f.close()
# Write a function for count all word in file
def wordcount(data):
    fo=None
    try:
        fo=open(data)
        data=fo.read().split()
        print("Total no of Words : ",len(data))
    except FileNotFoundError:
        print("Entered file not found")
    finally:
        if fo:
            fo.close()
def charcount(data):
    fo=None
    chardata=[]
    try:
        fo=open(data)
        data=fo.read()
        chardata.extend(data)
        print("Total Character With spaces : ",len(chardata))
    except:
        print("Entered file not found")
    finally:
        if fo:
            fo.close()
def removespace(data):
    fo=None
    chardata=[]
    try:
        fo=open(data)
        data=fo.read()
        for ch in data:
            if not ch.isspace():
                chardata.append(ch)
        print("Total no of Character Without space : ",len(chardata))
    except:
        print("Entered file not found")
    finally:
        if fo:
            fo.close()
def countspace(data):
    fo=None
    j=0
    try:
        fo=open(data)
        data=fo.read()
        for ch in data:
            if ch.isspace():
                j+=1 
        print("Total no of Spaces : ",j)
    except:
        print("Entered file not found")
    finally:
        if fo:
            fo.close()

def listcountchar(data):
    cnt=0
    point=''
    for i in range(len(data)):
        for j in data[i]:
            cnt+=1
            point=point+j
    print(point)
    print(cnt," characters in list:")
def removedigit(data):
    fo=None
    string=''
    try:
        fo=open(data)
        data=fo.read()
        for ch in data:
            if not ch.isdigit():
                string = string+ch
        print(string)
    except:
        print("Entered file not found")
    finally:
        if fo:
            fo.close()
def removepunc(data):
    fo=None
    string=''
    try:
        fo=open(data)
        data=fo.read()
        for ch in data:
            if ch not in """ !()-[]{};:'"\, <>./?@#$%^&*_~""" or ch.isspace():
                string=string+ch
        print(string)
    except FileNotFoundError:
        print("File No Found")
    finally:
        if fo:
            fo.close()
if __name__=='__main__':
    listcountchar(['java','python','java'])