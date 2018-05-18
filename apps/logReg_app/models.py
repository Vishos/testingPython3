from django.db import models
import bcrypt


class UserManager(models.Manager):
    def validateRegistration(self, postData):
        response = {
            'status' : False,
            'errors' : []
        }
        if len(postData['name']) <3:
            response['errors'].append("name too short")
        if len(response['errors']) == 0:
            response['status'] = True
            response['user_id'] = User.objects.create(
                name = postData['name'],
                email = postData['email'],
                password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
                ).id
        return response

    def validateLogin(self, postData):
        response = {
            'status' : False,
            'errors' : []
        }
        #use email to see if it's in the database
        existing_users = User.objects.filter(email=postData['email'])
        if len(existing_users) == 0:
            response['errors'].append('invalid email / password combo')
        else:
            if bcrypt.checkpw(postData['password'].encode(), existing_users[0].password.encode()):
                response['status'] = True
                response['user_id'] = existing_users[0].id
            else:
                response['errors'].append('invalid email / password combo')
        return response

        #compare passwords
        #login
        #send errors

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()

