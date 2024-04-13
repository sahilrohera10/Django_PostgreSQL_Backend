from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=10)
    user_email = models.EmailField(unique=True)
    user_pass = models.CharField(max_length=10)

    def __str__(self):
        return self.user_name
    

    