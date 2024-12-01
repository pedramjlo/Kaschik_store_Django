from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from phonenumber_field.formfields import PhoneNumberField


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    


    """
    we are basically overriding Django's built-in createsuperuser terminal command
    and adding extra fields to create a superuser there
    """
    def create_user(self, email, password=None, **extra_fields): 
        if not email: 
            raise ValueError('The Email field must be set') 
        email = self.normalize_email(email) 
        user = self.model(email=email, **extra_fields) 
        user.set_password(password) 
        user.save(using=self._db) 
        return user


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(max_length=11, region="IR")

    objects = CustomUserManager()


    def __str__(self):
        return f"{self.first_name} {self.last_name}"