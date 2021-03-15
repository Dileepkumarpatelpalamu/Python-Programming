from person import Person,Manager
import shelve
def update():
    db = shelve.open('persondb')
    for key in sorted(db):
        print(key,'\t=>',db[key])
    obj = db['Gagan Datta']
    obj.giveRaise(.10)
    db['Gagan Datta']=obj
    db.close()
def showdata():
    db = shelve.open('persondb')
    for key in sorted(db):
        print(key,'\t=>',db[key])
    db.close()
if __name__=='__main__':
    update()
    showdata()