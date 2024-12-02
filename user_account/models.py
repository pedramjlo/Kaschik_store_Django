from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser



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
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True) 
        extra_fields.setdefault('is_superuser', True) 
        if extra_fields.get('is_staff') is not True: 
            raise ValueError('Superuser must have is_staff=True.') 
        if extra_fields.get('is_superuser') is not True: 
            raise ValueError('Superuser must have is_superuser=True.') 
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(('email address'), unique=True) 
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50) 
    phone_number = models.CharField(max_length=11, blank=True) 
    is_active = models.BooleanField(default=True) 
    is_staff = models.BooleanField(default=False) 
    
    objects = CustomUserManager() 
    
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number'] 
    
    def __str__(self): 
        return self.email