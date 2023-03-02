from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


class CustomUserManager(BaseUserManager):
    """for django CLI when creating users and superusers"""
    
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
        
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        if not extra_fields.get("is_staff"):
            raise ValueError("Superuser has to have is_staff set to True")
        
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser has to have is_superuser set to True")
        
        return self.create_user(email=email, password=password, **extra_fields)
    
class User(AbstractUser):
    email = models.CharField(max_length=80, unique=True)
    last_name = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    date_of_birth = models.DateField(null=True)
    username = None
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    
    def __str__(self) -> str:
        return self.first_name
