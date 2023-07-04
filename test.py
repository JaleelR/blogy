from unittest import TestCase

from app import app 
from models import db, User
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



app.config["TESTING"] = True

app.config['DEBUG_TB_HOSTS']=['dont -show-debug-toolbar']
db.drop_all()
db.create_all()

class UserTestCase(TestCase): 


    def setUp(self):
        User.query.delete()

        user = User(first_name='Daemon', last_name ='C')
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id


    def tearDwon(self):

        db.session.rollback()
      
    
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
            


   
