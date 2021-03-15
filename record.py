from person import Person,Manager
p1= Person('Venkat')
p2 = Person("Gagan Datta",job="Dev",pay=100000)
p3 = Manager("Pawan Kumar",50000)
import shelve
db= shelve.open('persondb')
for obj in (p1,p2,p3):
    db[obj.name]=obj
db.close()
db= shelve.open('persondb')
for key in db:
    print(key,'=>',db[key])
db.close()