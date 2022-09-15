from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

class UserManager(BaseUserManager):
    def create_user(self, username, mobile, password=None):
        """
        Creates and saves a User with the given mobile and password.
        """
        if not username:
            raise ValueError("User must have an username")

        if not mobile:
            raise ValueError('Users must have an mobile number')

        user = self.model(
            username = username,
            mobile = mobile,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, mobile, password):
        """
        Creates and saves a superuser with the given mobile and password.
        """
        user = self.create_user(
            username = username,
            mobile = mobile,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.is_verified = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):

    username  =models.CharField(max_length=55, unique=True)
    mobile = models.CharField(max_length=10, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)  # a admin user; non super-user
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False) # a superuser
    is_admin_request = models.BooleanField(default=False)

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ['username'] # Password are required by default.

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    qty = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name
    @property
    def is_available(self):
        if self.qty ==0:
            return False
        else:
            return True

class CheckOut(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
