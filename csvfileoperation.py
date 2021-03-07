import csv
#write a function for read csv file data
def readcsvdata(data):
    fo = None
    try:
        fo=open(data)
        data=csv.reader(fo)
        for rec in list(data):
            for cols in range(len(rec)):
                print(rec[cols],end='\t')
            print()
    except FileNotFoundError:
        print("File not found!!!")
    finally:
        if fo:
            fo.close()
# Write a program for sum all employee salary in  a csv file
def calculatesumsalary(data):
    fo = None
    try:
        fo=open(data)
        data=csv.reader(fo)
        sum =0
        for rec in list(data):
            sum = sum + int(rec[2])
        print("Total Employee's Salary :",sum)
    except FileNotFoundError:
        print("File not found!!!")
    finally:
        if fo:
            fo.close()
# Write a program to calculate according to male and female employee salary
def calculatesexsalary(data):
    fo = None
    try:
        fo=open(data)
        data=csv.reader(fo)
        sum1= 0
        sum2 =0
        for rec in list(data):
            if rec[3] == 'F':
                sum1= sum1 + int(rec[2])
            else:
                sum2= sum2 + int(rec[2])
        print('Total Female Employee Salary :',sum1)
        print('Total Male Employee Salary :',sum2)
    except FileNotFoundError:
        print("File not found!!!")
    finally:
        if fo:
            fo.close()
# Write a program calculate max salary  in csv file
def calculatemaxsalary(data):
    fo = None
    try:
        fo=open(data)
        data=csv.reader(fo)
        maxsalary = 0
        for rec in list(data):
            if maxsalary < int(rec[2]):
                maxsalary = int(rec[2])
                empname= rec[1]
        print('Employee Name :',empname)
        print('Max Salary :',maxsalary)
    except FileNotFoundError:
        print("File not found!!!")
    finally:
        if fo:
            fo.close()
#Write a program to find minmum salary of employee name and salary
def calculateminsalary(data):
    fo = None
    try:
        fo=open(data)
        data=csv.reader(fo)
        result=list(data)
        minsalary = int(result[0][2])
        for rec in result:
            if minsalary > int(rec[2]):
                minsalary = int(rec[2])
                empname= rec[1]
        print(empname,' minimum salary :',minsalary)
    except FileNotFoundError:
        print("File not found!!!")
    finally:
        if fo:
            fo.close()
# Write a program to calculat average salary of emplyee in csv file
def calculateavgsalary(data):
    fo = None
    try:
        fo=open(data)
        data=csv.reader(fo)
        totalsalary = 0
        record = 0
        for rec in list(data):
            totalsalary = totalsalary + int(rec[2])
            record +=1
        print('Average Salary of employee : ',totalsalary/record)
    except FileNotFoundError:
        print("File not found!!!")
    finally:
        if fo:
            fo.close()
# Write a program whose employee salary deptno is 1002 and gender is female
def displaydepartment(data):
    fo = None
    try:
        fo=open(data)
        data=csv.reader(fo)
        res=list(data)
        for rec in res:
            if rec[4]=='1002' and rec[3]=='F':
                print(rec[1],'\t',rec[2])
    except FileNotFoundError:
        print("File not found!!!")
    finally:
        if fo:
            fo.close()
def startstring(data):
    fo = None
    try:
        fo=open(data)
        data=csv.reader(fo)
        res=list(data)
        for rec in res:
            if rec[1].startswith('S'):
                print(rec[1])
    except FileNotFoundError:
        print("File not found!!!")
    finally:
        if fo:
            fo.close()
#wirte a program to print employee name and salary greater than average salary
def displayrecord(data):
    fo = None
    try:
        fo=open(data)
        data=csv.reader(fo)
        res=list(data)
        totalsalary = 0
        totalemp = 0
        for rec in res:
            totalsalary = totalsalary + int(rec[2])
            totalemp +=1
        avg = int(totalsalary/totalemp)
        print('Average salary :',avg)
        for record in res:
            if avg <= int(record[2]):
                print(record[1],' ',record[2])
    except FileNotFoundError:
        print("File not found!!!")
    finally:
        if fo:
            fo.close()
# Write a function for dispaly to salary employee each department
def dispalytopsalary(data):
    fo= None
    try:
        fo = open(data)
        data = csv.reader(fo)
        res = list(data)
        dept1,dept2,dept3,dept4=[],[],[],[]
        for rec in res:
            if rec[4]=='1001':
                dept1.append(rec)
            elif rec[4]=='1002':
                dept2.append(rec)
            elif rec[4]=='1003':
                dept3.append(rec)
            elif rec[4]=='1004':
                dept4.append(rec)
        dept1.sort(key=lambda rec:int(rec[2]),reverse=True)
        dept2.sort(key=lambda rec:int(rec[2]),reverse=True)
        dept3.sort(key=lambda rec:int(rec[2]),reverse=True)
        dept4.sort(key=lambda rec:int(rec[2]),reverse=True)
        print('Top two Department wise salary 1001')
        print(dept1[:2])
        print('Top two Department wise salary 1002')
        print(dept2[:2])
        print('Top two Department wise salary 1003')
        print(dept3[:2])
        print('Top two Department wise salary 1004')
        print(dept4[:2])
    except FileNotFoundError:
        print("file Not found!!")
    finally:
        if fo :
            fo.close()
# Write a program to display least salary of employee from each department
def dispalyleastsalary(data):
    fo= None
    try:
        fo = open(data)
        data = csv.reader(fo)
        res = list(data)
        dept1,dept2,dept3,dept4=[],[],[],[]
        for rec in res:
            if rec[4]=='1001':
                dept1.append(rec)
            elif rec[4]=='1002':
                dept2.append(rec)
            elif rec[4]=='1003':
                dept3.append(rec)
            elif rec[4]=='1004':
                dept4.append(rec)
        dept1.sort(key=lambda rec:int(rec[2]))
        dept2.sort(key=lambda rec:int(rec[2]))
        dept3.sort(key=lambda rec:int(rec[2]))
        dept4.sort(key=lambda rec:int(rec[2]))
        print('least salary employee record two Department 1001')
        print(dept1[:2])
        print('least salary employee record two Department 1002')
        print(dept2[:2])
        print('least salary employee record two Department 1003')
        print(dept3[:2])
        print('least salary employee record two Department 1004')
        print(dept4[:2])
    except FileNotFoundError:
        print("file Not found!!")
    finally:
        if fo :
            fo.close()
# Write progam to calculate yearly report acoording to sales amount
def yearlysalesreport(data):
    fo = None
    try:
        fo= open(data)
        data = csv.reader(fo)
        res=list(data)
        dyear=input("Enter year :")
        sum=0.0
        for rec in res:
            dy=rec[0].split('-')
            if dy[2]==dyear:
                sum = sum + float(rec[1])
        print(dyear,"Yearly Sales Amount : ",round(sum,2))
    except FileNotFoundError:
        print("file not found!!")
    finally:
        if fo:
            fo.close()
## Write a program to data export in mycsv.csv file
def datatocsv(data):
    fo=None
    try:
        with open(data,'w',newline='') as fo:
            data = csv.writer(fo)
            if fo.tell()==0:
                data.writerow(['ID','Name','Salary','Sex','City'])
            while True:
                uid = input('Enter your ID :')
                name = input('Employee Name :')
                salary = float(input('enter salary :'))
                gender = input('Enter your gender :')
                city = input('Enter City Name :')
                data.writerow([uid,name,salary,gender,city])
                rows = input("Enter one more rose [Yes:No] ")
                if rows.lower() == 'no' or rows.upper()=='NO':
                    break
            print("Data writing sucessfully . ")
    except FileNotFoundError:
        print("file not found !")
    except ValueError:
        print("only numbe is allowed")
    finally:
        if fo:
            fo.close()
if __name__=='__main__':
    datatocsv('mycsv.csv')
