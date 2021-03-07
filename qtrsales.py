import csv
def opencsvfile(data):
	fo=None
	try:
		fo=open(data)
		data=csv.reader(fo)
		salesrecords=list(data)
		year=int(input("Enter year : "))
		return salesrecords,year
	except FileNotFoundError :
		print("File Not found !!")
	finally:
		if fo:
			fo.close()
def quaterlysalesreport(salesrecords,year):
		sums=[0.0,0.0,0.0,0.0,0.0]
		for rec in salesrecords:
			dt=rec[0].split("-")
			if(int(dt[2])==year):
				if(int(dt[1])<4):			
					sums[0]=sums[0]+float(rec[1])
				elif(int(dt[1])<7):			
					sums[1]=sums[1]+float(rec[1])
				elif(int(dt[1])<10):
					sums[2]=sums[2]+float(rec[1])
				else:
					sums[3]=sums[3]+float(rec[1])
				sums[4]=sums[4] + float(rec[1])
		for i in range(0,4):
			print("Qtr ",i+1," sales ",round(sums[i],2))
		print(year," sales amount : ",round(sums[4],2))
if __name__=="__main__":
	salesrecords, year =opencsvfile(r'C:\Users\Dileep-Pcs\OneDrive\Desktop\Python\sales.csv')
	quaterlysalesreport(salesrecords,year)