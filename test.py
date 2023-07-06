from unittest import TestCase

from app import app 
from models import db, User, Post
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



app.config["TESTING"] = True

app.config['DEBUG_TB_HOSTS']=['dont -show-debug-toolbar']
db.drop_all()
db.create_all()

class UserTestCase(TestCase): 


    def setUp(self):
        User.query.delete()
        Post.query.delete()

        user = User(first_name='Daemon', last_name ='C')
        db.session.add(user)
        db.session.commit()
        self.user_id = user.id

        post = Post(title ='Try It', content ='Touch my sister and ill kill you', user_id = user.id)
        db.session.add(post)
        db.session.commit()
        self.post_id = post.id


    def tearDown(self):
       Post.query.filter_by(user_id=self.user_id).delete()
       User.query.filter_by(id=self.user_id).delete()
       db.session.commit()
      
    
    def test_list_user(self):
        with app.test_client() as client:
            resp = client.get('/users')
            html = resp.get_data(as_text = True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Daemon', html)
    

    def test_edit_correction(self): 
        with app.test_client() as client: 
            resp = client.get(f'/users/{self.user_id}/edit')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("\n<h1>Edit user Daemon", html)



    def test_post_form(self):
        with app.test_client() as client:
            resp = client.get(f'/users/{self.post_id}/posts/new')
            html = resp.get_data(as_text = True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('\n<h1>Add a post for Daemon C</h1>', html)
    

    def test_post_details(self): 
        with app.test_client() as client: 
            resp = client.get(f'/users/{self.post_id}')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('\n<h1> Daemon\nC </h1>', html)
            






    # def test_redirect_to_add(self):
    #      with app.test_client() as client: 
            
    #         resp = client.post(
    #             "/users/new",
    #              data =  {"fname" : "Jaleel", "lname" : "W"}, 
    #              follow_redirects = True,
    #              content_type="application/x-www-form-urlencoded"
    #             )
    #         print('resp', resp)
    #         html = resp.get_data(as_text=True)
            
    #         self.assertEqual(resp.status_code, 200)
            


   
