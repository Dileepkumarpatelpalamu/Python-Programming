import csv
#Write a function for open the csv file in python.
def opencsv(data):
    fo = None
    try:
        with open(data) as fo:
            salesrecord=list(csv.reader(fo))
            year=input("Enter year : ")
            return salesrecord,year
    except FileNotFoundError:
        print('File no found !')
    finally:
        if fo:
            fo.close()
# Write a function for calculate half yearly sales report.
def calculatehalfyearlyreport(salesrecord,year):
    sums=[0.0,0.0]
    for rec in salesrecord:
        dt = rec[0].split('-')
        if int(dt[2])==int(year) :
            if int(dt[1])< 7:
                sums[0]= sums[0]+ float(rec[1])
            elif int(dt[1])< 13:
                sums[1]= sums[1]+ float(rec[1])
    for i in range(2):
        print('half ',i+1,'Sales amount :',round(sums[i],2))
    return sums
# Write a fuction for export file into pc.
def exportcsv(record):
    fo = None
    try:
        with open('file.csv','w',newline='') as fo:
            data = csv.writer(fo)
            data.writerow(['Half 1','Half 2'])
            data.writerow([round(record[0],2),round(record[1],2)])
            print('Report generated successfully.')
    except FileNotFoundError:
        print('File not found')
    finally:
        if fo :
            fo.close()
# Here is start from main function on python
if __name__=='__main__':
    salesrecord,year=opencsv('sales.csv')
    record = calculatehalfyearlyreport(salesrecord,year)
    exportcsv(record)