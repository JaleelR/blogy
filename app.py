"""Blogly application."""

from flask import Flask, render_template, redirect, request, url_for
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

ctx = app.app_context()
ctx.push()
app.config['WTF_CSRF_ENABLED'] = False
app.config['SECRET_KEY'] = 'Naruto7'
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False







app.route("/")
def home2():
    return redirect('/users')

@app.route('/users')
def home():
    '''Shows homepage with list of users '''  
    users = User.orderby()

   

    return render_template("User.html", users = users )




    

    
@app.route('/users/new', methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        first_name = request.form["fname"]
        last_name = request.form["lname"]
        img = request.form["img"]

        print(f"Received form data: first_name={first_name}, last_name={last_name}, img={img}")

        new_user = User(first_name = first_name, last_name = last_name, image_url= img)   
        db.session.add(new_user)
        db.session.commit()


        return redirect("/users")

    else:
     return render_template("create.html")      



@app.route("/users/<int:user_id>")   
def details(user_id):
   user = User.query.get_or_404(user_id)

   return render_template('details.html', user = user) 




@app.route("/users/<int:user_id>/edit", methods = ["GET", "POST"])   
def edit(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == "POST":
        first_name = request.form.get("fname", user.first_name)
        last_name = request.form.get("lname", user.last_name)
        image_url = request.form.get("img", user.image_url)

        user.first_name = first_name if first_name else user.first_name
        user.last_name = last_name if last_name else user.last_name
        user.image_url = image_url if image_url else user.image_url

        db.session.commit()
        return redirect('/users')
        
    else:
        user = User.query.get_or_404(user_id)
        return render_template("edit.html", user=user)



@app.route("/users/<int:user_id>/delete", methods=["POST"])
def delete(user_id):
   user = User.query.get_or_404(user_id)
   db.session.delete(user)
   db.session.commit()
   return redirect('/users')   



  



 







