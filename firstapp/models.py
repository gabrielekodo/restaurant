from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.
class MenuItems(models.Model):
     name=models.CharField(max_length=255)
     description = models.CharField(max_length=1000,default='')
     image = models.CharField(max_length=1000,default='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDViaXlpMWc1N2ttODhqaXV2b3Z2eHgwdzdkMTVzcXduMTAyYjdzbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/84ZzhsJZWlE3e/giphy.gif')
     price=models.IntegerField()

     def __str__(self):
         return self.name


class Reservation(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    guest_count=models.IntegerField()
    reservation_time=models.DateTimeField(auto_now=True)
    comments=models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name+' '+self.last_name


class User(models.Model):
    username=models.CharField(max_length=255,unique=True)
    email=models.CharField(max_length=255,unique=True)
    password=models.CharField(max_length=1000)
    role=models.CharField(default='admin')

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']