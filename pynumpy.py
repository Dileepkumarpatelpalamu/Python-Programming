import numpy as np
def getdata():
    num = int(input("Number of element : "))
    arr =[]
    for item in range(num):
        val= int(input("Enter array "+str(item+1)+" element : "))
        arr.append(val)
    return arr
def getdouble():
    data=[]
    rows = int(input("Enter No of rows : "))
    cols = int(input("Enter No of cols : "))
    for i in range(rows):
        a=[]
        for j in range(cols):
            val=int(input("Enter "+str(i+1)+" row "+str(j+1)+" element :"))
            a.append(val)
        data.append(a)
    return data
def showdata(data):
    newdata=np.array(data)
    print(newdata)
    print("Dimension of array = ",newdata.ndim)
    print("Shape of array = ",newdata.shape)
if __name__=='__main__':
    data=getdouble()
    showdata(data)
