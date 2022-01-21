from django.db import models
from django.contrib.auth.models import AbstractUser


# Abstractuser


class User(AbstractUser):

    def get_full_name(self) -> str:
        return '{} {}'.format(self.first_name, self.last_name)
    
    
    
    


class Customer(User):
    class Meta:
        proxy = True

    def get_products(self):
        return []


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
