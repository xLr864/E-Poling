from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
import datetime

# Create your models here.
class Registeration(models.Model):
    Name = models.CharField(max_length=69)
    Email = models.EmailField()
    Mobile = models.CharField(max_length=13)
    Address = models.CharField(max_length=100)
    Aadhar = models.CharField(max_length=12,unique=True)
    VoterID = models.CharField(max_length=10,primary_key=True)
    DOB = models.DateField(default=datetime.datetime.now().strftime("%Y/%m/%d"))

class CustomUserManager(BaseUserManager):
    use_in_migrations=True
    def create_user(self, user_name,VoterID,DOB):
        if not VoterID:
            raise ValueError("Voter ID required")
        user = self.model(user_name=user_name,VoterID=VoterID,DOB=DOB)
        user.set_password(VoterID)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_name, password, **extra_fields): 
        extra_fields.setdefault('is_staff', True)  
        extra_fields.setdefault('is_superuser', True)  
        extra_fields.setdefault('is_active', True)  
        if extra_fields.get('is_staff') is not True:  
            raise ValueError(_('Superuser must have is_staff=True.'))  
        if extra_fields.get('is_superuser') is not True:  
            raise ValueError(_('Superuser must have is_superuser=True.'))  
        return self.create_user(user_name, password, **extra_fields)   


class User(AbstractUser):
    user_name = models.CharField(max_length=69)
    password = models.CharField(max_length=100)
    VoterID = models.CharField(max_length=10,primary_key=True)
    DOB = models.DateField(default=datetime.datetime.now().strftime("%Y/%m/%d"))
    objects = CustomUserManager()  
    USERNAME_FIELD="VoterID"
    REQUIRED_FIELDS = []
    is_staff = models.BooleanField(default=False)  
    is_active = models.BooleanField(default=True)
    def has_perm(self, perm, obj=None):  
        "Does the user have a specific permission?"  
        return True  
  
    def is_staff(self):  
        "Is the user a member of staff?"  
        return self.staff  
    
    @property  
    def is_admin(self):  
        "Is the user a admin member?"  
        return self.admin  

    def __str__(self):  
        return self.VoterID    



