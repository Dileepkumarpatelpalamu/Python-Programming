import matplotlib.pyplot as plt
x = [60,20,30,40,50]
y = ["Hindi","English","Maths","Science","Social science"]
plt.pie(x, labels=y)
plt.title("Document of Bar graph")
plt.xlabel("Subject Name")
plt.ylabel("Subject Marks")
plt.show()