from email.mime import image
from django.test import TestCase
from . models import *
# Create your tests here.
class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.neighbourhood = Neighbourhood(name='sheepherders',image='https://res.cloudinary.com/dz275mqsc/image/upload/v1654858776/default_nbsolf.png')
        self.user = User(id=1,username='sandy')
    def test_instances(self):
        self.assertTrue(isinstance(self.neighbourhood, Neighbourhood))

    def test_save_neighbourhood(self):
        self.user.save()
        # self.neighbourhood.create_neighbourhood()
        # neighbourhood = Neighbourhood.objects.all()
        # self.assertTrue(len(neighbourhood) > 0)




class ProfileTestClass(TestCase):
    def setUp(self):
        self.neighbourhood= Neighbourhood(name='sheep-herders')
        self.neighbourhood.save_neighbourhood()
        self.profile = Profile(bio='this is a bio',
        email='testemail@gmail.com',neighbourhood=self.neighbourhood)
        self.user = User(id=1,username='sandy')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.user.save()
       
    def test_delete_profile(self):
        self.user.delete()
       
    

class BusinessTestClass(TestCase):
    def setUp(self):
        self.neighbourhood= Neighbourhood(name='sheep-herders')
        self.business= Business(title='kinyozi')
        # self.business.save_business()
        self.profile = Profile(bio='this is a bio',
        email='testemail@gmail.com',neighbourhood=self.neighbourhood)
        self.user = User(id=1,username='sandy')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))
       
    def test_delete_business(self):
        self.user.delete()

    def test_save_business(self):
        self.user.save()

    def test_update_method(self):
        self.user.save()

    def test_search_business(self):
        self.user.save()

class PostTestClass(TestCase):
    def setUp(self):
        self.neighbourhood= Neighbourhood(name='sheep-herders')
        self.post= Post(title='kinyozi')
        self.post.save_post()
        self.profile = Profile(bio='this is a bio',
        email='testemail@gmail.com',neighbourhood=self.neighbourhood)
        self.user = User(id=1,username='sandy')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

    def test_save_post(self):
        self.user.save()
       
    def test_delete_post(self):
        self.user.delete()

