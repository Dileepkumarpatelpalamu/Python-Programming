# Write a program to store output of python program save into file
def findprime(num):
    try:
        print("Prime Number : ")
        prime=''
        for i in range(2,num+1):
            for j in range(2, (i//2)+1):
                if i%j == 0:
                    break
            else:
                prime = prime+ str(i) +',\t'
        print(prime)
        return prime
    except ValueError:
        print("Do not enter string or character !")
def exportoutput(output):
    fo=None
    try:
        fo = open('outfile.txt','w')
        data=fo.write(output)
        print("Output save into files :")
    except FileNotFoundError:
        print('File Not found !')
    finally:
        if fo:
            fo.close()
if __name__=='__main__':
    #num = int(input("Enter any number : "))
    #savepoint=findprime(num) 
    #exportoutput(savepoint)
    # Write a program to print unique words in paragraph 
    paragraph="""i like python python like java so we can not uderstand java"""
    unique=set()
    data=''
    for word in paragraph.split():
        if word not in unique:
            unique.add(word)
            data = data +" "+ word
    print(data)
    
    
    


