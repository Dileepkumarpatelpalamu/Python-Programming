"""--------------------------Pickle------------------------------------------------------------------
1. Pickling allows you to serialize and de-serializing python object structures.
2. In short, pickling is a way to convert a python object into a character stream so that this characters stream
contains all information necessary to reconstruct the object in another python script
3. To successfully reconstruct the object, the pickled byte stream contains instruction to unpickle to reconstruct the
original object structure along with instruction operands, which help in populatedd the object structure
The picle has main two methods
1. dump() The dump() is used to dump an object to a file object
syntax: pickle.dump(object,file object, protocol)
protocol is optional arguments this method takes three agruments python objects to serialize, file object in which the
 serialize python object must be sotred
 example:
 import pickle
 x,y,z = 43,44,45
 s = 'python'
 d ={'a':1,'b':2}
 l = [1,2,3]
 f=open('datafile.txt','wb')
 pickle.dump(x,f)
 pickle.dump(y,f)
 pickle.dump(z,f)
 pickle.dump(s,f)
 pickle.dump(d,f)
 pickle.dump(l,f)
 f.close()
 f.open('datafile.txt','rb')
 for i in range(6):
     e = pickle.load(f)
     print(E, type(e))
def pickle_data():
    data ={
        'name':'Dileep Kumar Patel',
        'profession':'Software Engineer',
        'country': 'India'
    }
    filename = 'personalinfo.txt'
    outfile = open(filename,'wb')
    pickle.dump(data,outfile)
    outfile.close()
To open the file we used open function the first argument should be the name of file your file and second argument is
wb, wb refers the writing in binary mode this means your file and second be written inform of byte objects.
-------------------Unpickling-----------------------------------------
example --
import pickle
def unpickling_data():
    file = open('personalinfo.txt','rb')
    newdata = pickle.load(file)
    file.close()
    return newdata
What can be pickled?
1. Booleans
2. Integers
3. Floats
4. Complex numbers
5. Normal and uni code string
6. Tuples
7. Lists
8. Set and Dictionary
9. Built-in functions defined the top level of a module
10 Classes that are defined at the top level of module
Comman uses of pickling---------------------------
---To save a program's state data to disk so that it can carry on where it left off when restarted
---Sending python data over a TCp connection in multi-core or distributed system
---Storing python object in a database
We get back an equivalent dictionary object with no manual spliting or converting required. the pickle perform what
is known as object serializtion converting object to and from string of bytes


"""
import pickle
# x,y,z = 43,44,45
# s = 'python'
# d ={'a':1,'b':2}
# l = [1,2,3]
# f=open('datafile.txt','wb')
# pickle.dump(x,f)
# pickle.dump(y,f)
# pickle.dump(z,f)
# pickle.dump(s,f)
# pickle.dump(d,f)
# pickle.dump(l,f)
# f.close()
# f=open('datafile.txt','rb')
# for i in range(6):
#     e = pickle.load(f)
#     print(e, type(e))
def pickle_data():
    data ={
        'name':'Dileep Kumar Patel',
        'profession':'Software Engineer',
        'country': 'India'
    }
    filename = 'personalinfo.txt'
    outfile = open(filename,'wb')
    pickle.dump(data,outfile)
    outfile.close()
def unpickling_data():
    file = open('personalinfo.txt','rb')
    newdata = pickle.load(file)
    file.close()
    return newdata
