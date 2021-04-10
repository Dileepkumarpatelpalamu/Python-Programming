from flask_sqlalchemy import SQLAlchemy
from flask import Flask,session
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ="mysql://root:@localhost:3307/flaskblog"
db = SQLAlchemy(app)
class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    def __repr__(self):
        return f"Sno :{self.sno} Name :{self.name} Phone: {self.phone_num} Message :{self.msg} date {self.date}"
class Post(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(12), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=False)
    def __repr__(self):
        return f"{self.sno,self.title,self.slug,self.content,self.date}"
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(12), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=False)
    def __repr__(self):
        return f"{self.id,self.name,self.email,self.password,self.date}"
if __name__=="__main__":
    eid=int(input("Enter user id : "))
    contact=Contacts.query.first()
    post= Post.query.first()
    user= User.query.filter_by(id=eid).first()
    print(user)

    

    