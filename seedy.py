from models import User, db 
from app import app 

db.drop_all()
db.create_all()

User.query.delete()


sarada = User(first_name='Sarada', last_name ='U')
mashle = User(first_name='Mashle', last_name ='B')
daemon = User(first_name='Daemon', last_name ='C')
momoshiki = User(first_name='Momoshiki', last_name ='O')
db.session.add(momoshiki)
db.session.add(sarada)
db.session.add(mashle)
db.session.add(daemon)


db.session.commit() 