#How to use args and kwags
def print_intro(simple,*args,**kwargs):
	print(simple)
	for item in args:
		print(item)
	for key, value in kwargs.items():
		print(f" Id : {key} and Name : {value}")
simple = "I want to under stand Python languages:"
args = ["Dileep","Maya","Rohan","Danik","Mohit"]
kwargs = {"1":"Maya Kumari","2":"Dileep Kumar Patel","3":"Rohit Kumar"}
print_intro(simple, *args, **kwargs)