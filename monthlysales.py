import csv
def monthlyreport(salesrecords,year):
	sums=[0,0,0,0,0,0,0,0,0,0,0,0]
	for rec in salesrecords:
		dt=rec[0].split("-")
		if(int(dt[2])==year):
			sums[int(dt[1])-1]=sums[int(dt[1])-1]+float(rec[1])
	months=["Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec"]
	for i in range(0,12):
		print(months[i]," sales ",round(sums[i],2))
def opencsvfile(data):
	fo=None
	try:
		fo=open(data)
		data=csv.reader(fo)
		salesrecords=list(data)
		year=int(input("enter year"))
		return salesrecords,year
	except  FileNotFoundError:
		print("File Not found !")
	finally:
		if fo:
			fo.close()
if __name__=='__main__':
	salesrecords,year=opencsvfile(r'C:\Users\Dileep-Pcs\OneDrive\Desktop\Python\sales.csv')
	monthlyreport(salesrecords,year)