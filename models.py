from flask_sqlalchemy import SQLAlchemy

from datetime import datetime



db = SQLAlchemy()
 
def connect_db(app):
    db.app = app 
    db.init_app(app)



"""Models for Blogly."""
class User(db.Model): 
    def __repr__(self):
        u = self
        return f"<User id ={u.id} firstname = {u.first_name} lastname = {u.last_name} img = {u.image_url}"
    __tablename__ = 'users'

    @classmethod
    def orderby(cls):
       return User.query.order_by(cls.id.asc()).all()
      
            

    id = db.Column(db.Integer, 
                   primary_key=True,
                   autoincrement=True)

    first_name = db.Column(db.String(20),
                           nullable=False,
                            unique=False)
    last_name = db.Column(db.String(20),
                           nullable=True)
    image_url = db.Column(db.Text, 
                            nullable=True)


    def getpost(self): 
        posts= []
        for post in self.posts:
            posts.append(post)   
        return posts



class Post(db.Model): 
    def __repr__(self):
        p = self
        return f"<post.id ={p.id} title = {p.title} content = {p.content} created_at= {p.created_at}"
    __tablename__ = 'posts'


    @classmethod
    def orderby(cls):
       return Post.query.order_by(cls.id.asc()).all()
   
            

    id = db.Column(db.Integer, 
                   primary_key=True,
                   autoincrement=True)

    title = db.Column(db.Text,
                           nullable=True,
                            unique=False)
    content = db.Column(db.Text,
                           nullable=False)
    created_at = db.Column(db.DateTime, 
                            nullable=False, default=datetime.utcnow)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    user = db.relationship("User", backref="posts")

  



