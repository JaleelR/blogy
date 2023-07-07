from app import app
from models import User, db, Tag, Post, PostTag



db.drop_all()

db.create_all()

User.query.delete()
Post.query.delete()
Tag.query.delete()
PostTag.query.delete()



sarada = User(first_name='Sarada', last_name ='Uchiha', image_url = "https://media.tenor.com/rL9NmOLAqI8AAAAC/sarada-uchiha.gif " )
mashle = User(first_name='Mashle', last_name ='Burnadead', image_url = "https://media.tenor.com/13WIZuwog7cAAAAC/mash-mashle.gif")
daemon = User(first_name='Daemon', last_name ='Cyborg', image_url = "https://media.tenor.com/d88j6aPCG3sAAAAC/daemon-boruto.gif")
tobirama = User(first_name='Tobirama', last_name ='Senju', image_url = "https://media.tenor.com/Dy5flbpDHPgAAAAC/tobirama-chakra.gif")
itachi = User(first_name='Itachi', last_name ='Uchiha', image_url = "https://gifdb.com/images/high/itachi-vs-sasuke-anime-fight-oyftbjaew7bunccb.gif")
Orochimaru = User(first_name='Orochimaru', image_url = "https://78.media.tumblr.com/0702c8d4e52ce78b46950e1f7a8bbd0a/tumblr_p9csa3Prn21s5ng6zo1_400.gif")

db.session.add_all([sarada,  mashle, daemon, tobirama, itachi])
db.session.commit() 



sarada1 = Post(title="Love",content="We\re drunk on the fact that we beleive that love and only love can bring us happiness", user_id="1")
sarada2 = Post(title="Hope",content="I'll be your light boruto", user_id="1")
mashle1 = Post(title="Creampuffs",content="Lets have a creamPuff", user_id="2")
daemon1 = Post(title="You are weak",content="Dont hurt my sister or ill kill you!", user_id="3")
tobirama1 = Post(title="Uchiha\s are evil",content="I\ll segregate them all Muhaahhaah", user_id="4")
itachi1 = Post(title="Hopeful",content="I still love you brother", user_id="5")
orochimari1= Post(content="I love science", user_id="6")


db.session.add_all([sarada1, sarada2, mashle1, daemon1, tobirama1, itachi1])
db.session.commit()




breakingcurses = Tag(name="breaking curses")
new_blood = Tag(name="new generation")
big_dog = Tag(name="Im the big dog")
fav_food= Tag(name="creampuffs")
hater = Tag(name="Uchihas must die")
goodguy = Tag(name="shadow hokage")
goodguy2 = Tag(name="chestnotcheckers")
goodguy3 = Tag(name="genius")
creep = Tag(name="science")

db.session.add_all([breakingcurses, new_blood, big_dog, fav_food, hater, goodguy, goodguy2, goodguy3, creep])
db.session.commit()


sarpt = PostTag(post_id = 1, tag_id = 1)
sarpt2 = PostTag(post_id = 1, tag_id = 2)

daept = PostTag(post_id = 4, tag_id = 3)
maspt = PostTag(post_id = 3, tag_id = 4)
tobpt = PostTag(post_id = 5, tag_id = 5)

itapt = PostTag(post_id = 6, tag_id = 6)
itapt2 = PostTag(post_id = 6, tag_id = 7)
itapt3 = PostTag(post_id = 6, tag_id = 8)

oropt = PostTag(post_id = 6, tag_id = 9)

db.session.add_all([sarpt, sarpt2, daept, maspt, tobpt, itapt, itapt2, itapt3])
db.session.commit()