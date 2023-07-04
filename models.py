from flask_sqlalchemy import SQLAlchemy

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


