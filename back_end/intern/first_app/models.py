from django.db import models
from django.contrib.auth.models import User
# # from django.contrib.auth.models import User

# # # Create your models here.
# # class UserProfileInfo(models.Model):

# #     # create relationship (don't inherit from User!)
# #     user = models.OneToField(User)
# #     # add any additional attributes you want 

# #     def __self__(self):
# #         return self.user.username
# class Topic(models.Model):
#     top_name = models.charField(max_length = 264, unique = True)
#     number = models.IntegerField()
#     email = models.EmailField()
#     text = models.

class Post(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE, primary_key = True)
    #additional attributes
    name = models.CharField(max_length=300, unique= True,default = 'name')
    number = models.CharField(max_length = 300, unique= True, default = '9999999999')
    comments = models.CharField(max_length=300, default = "Enter comments")
    def __str__(self):
        return self.user.name


class FormSl(models.Model):
    # for signup and login
    first_name = models.CharField(max_length= 32, unique = True)
    last_name = models.CharField(max_length= 32, unique = True)
    emailid = models.EmailField()
    number = models.IntegerField()
    up = models.CharField(max_length = 32, unique = True)
    up2 = models.CharField(max_length = 32, unique = True)

class LoginMod(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length = 32)


# class UserProfileInfo(models.Model):
#     user = models.CharField(max_length = 300, unique = True)
    
#     def __str__(self):
#         return self.user.username
