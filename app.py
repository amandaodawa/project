from flask import Flask, render_template, request, redirect, url_for , flash

#toolkit and object relational mapper for python
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'something'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True

#initiliaze the db with our app settings
db = SQLAlchemy(app)

#Create the database model
class contact(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    fname= db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(50), nullable=False)

    def __init__(self, fname, lname, email, messageitem):
      self.fname=fname
      self.lname=lname
      self.email=email
      self.message=messageitem
      
#this route is for inserting data to mysql database via html forms
@app.route('/contact', methods = ['POST','GET'])
def insert():
 
    if request.method == 'POST':
 
        contact = insert(fname= request.form['fname'], lname=  request.form['lname'] , email= request.form['email'], messageitem= request.form['message'])
        db.session.add(contact)
        db.session.commit()
        
        flash("Message sent")
        
        return render_template("contact.html")
      
      

@app.route("/")
def home():
   return redirect("/index.html")

@app.route("/index.html")
def home_1():
   return render_template("index.html")

@app.route("/portfolio-page.html")
def second():
   return render_template("portfolio-page.html")

@app.route("/portfolioII-page.html")
def third():
   return render_template("portfolioII-page.html")

@app.route("/contact.html")
def contact():
   return render_template("contact.html")


if __name__ == "__main__":
   app.run(debug=True)