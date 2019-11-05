from django.db import models
from django.contrib.auth.models import (
        BaseUserManager, AbstractBaseUser,
        PermissionsMixin)

class UserManager(BaseUserManager):
    def create_user(self, email, username, password):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
                email=UserManager.normalize_email(email),
                username=username
                )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
                email=email,
                username=username,
                password=password
                )
        user.is_admin = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
            verbose_name='email',
            max_length=255,
            unique=True
            )
    username = models.CharField(
            u'닉네임',
            max_length=15,
            blank=False,
            unique=True,
            default=''
            )
    is_admin = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
