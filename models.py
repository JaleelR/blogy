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

  
class Tag(db.Model):
    def __repr__(self):
        t = self
        return f"Tag.id = {t.id} tag.name = {t.name} "
        
    __tablename__= 'tags'

    @classmethod
    def gettags(cls):
        tags = []
        for tag in Tag.query.all():
            tags.append(tag)
        return tags

    id = db.Column(db.Integer, 
                    primary_key=True,
                    autoincrement=True)
                
    name = db.Column(db.String(20), 
                     nullable=False,
                     unique=True)
    post = db.relationship('Post', secondary='posttags', backref='tags')

    

class PostTag(db.Model):
    def __repr__(self):
        pt = self
        return f"post_id = {pt.post_id} tag.name = {pt.tag_id} "
    __tablename__= 'posttags'

    post_id = db.Column(db.Integer,
                    db.ForeignKey('posts.id'),
                    primary_key=True,
                    nullable = False,
                    autoincrement=True)

    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'),
                     primary_key=True,
                     nullable = False,
                     unique=True)

    
                

