"""Blogly application."""

from flask import Flask, render_template, redirect, request, url_for
from models import db, connect_db, User, Post
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










@app.route("/")
def home2():
    '''redirects to home'''
    return redirect('/users')

@app.route('/users')
def home():
    '''Shows homepage with list of users '''  
    users = User.orderby()


    return render_template("User.html", users = users )



    
@app.route('/users/new', methods=["GET", "POST"])
def add_user():
    ''' 
     - shows a frm to create user
    - If post request (hits add button), data from input fields will create user 
   
     '''
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


@app.route("/users/<int:user_id>/posts/new", methods=["GET", "POST"])
def post_form(user_id):
    """
    - Show form to add a post from that user
    - If post request (hits add button), data from input fields will create post and redirect to details page
    """
    user = User.query.get_or_404(user_id)
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        added_post = Post(title= title, content = content, user_id = user.id)
        db.session.add(added_post)
        db.session.commit()
        user.posts.append(added_post)
        return redirect(f'/users/{user.id}')
    else:
        return render_template('post.html', user = user)




@app.route("/users/<int:user_id>")   
def details(user_id):
   '''
   - Get current user instance 
   - Shows details page 
   '''
   user = User.query.get_or_404(user_id)

   return render_template('details.html', user = user) 


@app.route("/posts/<int:post_id>")
def post_details(post_id):
    '''
    - Get current user instance 
    - Shows details page 
    '''
    post = Post.query.get_or_404(post_id)
    return render_template('postdetail.html', post = post)





@app.route("/users/<int:user_id>/edit", methods = ["GET", "POST"])   
def edit(user_id):

    '''
    - Shows edit page
    - Gets current User
    if Post request(pressed save button)
    - Updates the current user with input fields filled
    - if a input field isn't filled out, it will keep the previous data it had before
    '''
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


@app.route("/posts/<int:post_id>/edit", methods=["GET", "POST"])
def post_edit(post_id):
    '''
    - Shows editpost page
    - Gets current post
    if Post request(pressed add button)
    - Updates the current post with input fields filled
    '''
    post = Post.query.get_or_404(post_id)
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        added_post = Post(title= title, content = content, user_id = post.user_id)
        db.session.add(added_post)
        db.session.commit()

        post.append(added_post)
        return redirect(f"/posts/{post.id}")
    else:
        return render_template('postedit.html', post = post)





@app.route("/users/<int:user_id>/delete", methods=["POST"])
def delete(user_id):
   """
   - Gets the current user
   - if delete button is pressed on edit page, the current user instance is deleted
   - once deleted client is moved to users.html
   """
   user = User.query.get_or_404(user_id)
   db.session.delete(user)
   db.session.commit()
   return redirect('/users')   


@app.route("/post/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
   """
   - Gets the current Post
   - if delete button is pressed on postedit page, the current post instance is deleted
   - once deleted client is moved to users.html
   """
   post = Post.query.get_or_404(post_id)
   db.session.delete(post)
   db.session.commit()
   return redirect('/users')   



  



 







