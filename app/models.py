from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from django.db.models.deletion import CASCADE, SET_NULL
from django.http import Http404
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    profile_pic = CloudinaryField('image',default='https://res.cloudinary.com/dz275mqsc/image/upload/v1654858776/default_nbsolf.png')
    bio = models.CharField(max_length=50)
    email =models.EmailField(max_length=20)
    location = models.CharField(max_length=20,null=True, blank=True)
    neighbourhood = models.ForeignKey('NeighbourHood', on_delete=SET_NULL,null=True, related_name='pple', blank=True)
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    # bio = models.CharField(max_length=50)
    # profile_pic = CloudinaryField('image',default='https://res.cloudinary.com/dz275mqsc/image/upload/v1654858776/default_nbsolf.png')
    # neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,blank=True)
    # email= models.EmailField(max_length=20)
    # location= models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    # @receiver(post_save,sender=User)
    # def save_user_profile(sender,instance,**kwargs):
    #         instance.profile.save()


class Neighbourhood(models.Model):
    image = CloudinaryField('image',blank=True, default='https://res.cloudinary.com/dz275mqsc/image/upload/v1654858776/default_nbsolf.png')
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    admin = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,related_name='admin')
    health_dept = PhoneNumberField(unique=True,blank=True,max_length=20,help_text='Phone Number Format: +254712345678')
    police_dept = PhoneNumberField(unique=True,blank=True,max_length=20,help_text='Phone Number Format: +254712345678')
    occupants = models.IntegerField(null = True,verbose_name='Occupants')

    def __str__(self):
        return self.name

  

    def create_neighbourhood(self):
        self.save()
        
    def delete_neighbourhood(self):
        self.delete()

    @classmethod
    def update_neighbourhood(cls,name):
        return cls.objects.filter(name=name).update(name=name)

    @classmethod
    def update_occupants(cls,occupants):
        return cls.objects.filter(occupants=occupants).update(occupants=occupants)

    @classmethod
    def find_neighbourhood(cls,neighbourhood_id):
        return cls.objects.filter(id=neighbourhood_id)



    

class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    neighbourhood = models.ForeignKey('Neighbourhood',on_delete=models.CASCADE,blank=True)
    title = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)


    def __str__(self):
        return f'{self.name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()
    
    @classmethod
    def get_all_business(cls):
        return cls.objects.all()

    @classmethod
    def find_business(cls,name):
        try:
            return cls.objects.get(pk=name)
        except Business.DoesNotExist:
            return Http404
        # return cls.objects.filter(name__icontains=name).all()
# create_business()
# delete_business()
# find_business(business_id)
# update_business()

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    title = models.CharField(max_length=20)
    context = models.TextField()
    date = models.DateField(auto_now_add=True)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,blank=True)
    

    def __str__(self):
        return f'{self.title} Post'

    def create_post(self):
        self.save()

    def delete_post(self):
        self.delete()