from typing import List

from django.contrib.auth.models import AbstractUser
from django.db import models

class Permission(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def get_permissions(self):
        return [p.permission for p in self.permissions.all()]

class RolePermission(models.Model):
    role = models.ForeignKey(Role,on_delete=models.CASCADE, related_name='permissions')
    permission = models.ForeignKey(Permission,on_delete=models.CASCADE,related_name='roles')

class User(AbstractUser):
    GENDER_CHOICE = (
        ('MALE','male'),
        ('FAMALE','famale'),
    )
    phone_number = models.CharField(
        max_length=150,
        unique=True
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        null=True
    )
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    middle_name = models.CharField(max_length=100,null=True,blank=True)
    gender = models.CharField(max_length=10,null=True,choices=GENDER_CHOICE)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,unique=True,null=True,blank=True)
    is_verified = models.BooleanField(default=False)
    image = models.ImageField(null=True,blank=True)

    def has_tag(self,tag):
        tags_str = [ut.tag.name for ut in self.usertags.all()]
        return tag in tags_str

    def get_tags(self):
        return [ut.tag for ut in self.usertags.all()]

    def has_permissions(self,permissions):
        return all(rperm in self.get_permissions_str()  for rperm in permissions)

    def get_permissions(self):
        result: List[Permission] = []
        for r in self.roles.all():
            result += r.role.get_permissions()
        return result

    def get_permissions_str(self):
        return [p.name for p in self.get_permissions()]


    @classmethod
    def create_user(cls, phone_number, password=None, **extra_fields):
        user: cls = cls.objects.filter(phone_number=phone_number)
        if user:
            return 'This phone number is busy!'
        else:
            user = User.objects.create(
                phone_number=phone_number,
                password=password
            )
            user.set_password(password)
            user.save()
        return user

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username','email']

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return self.phone_number

class UserRole(models.Model):
    role = models.ForeignKey(Role,on_delete=models.CASCADE, related_name='users')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='roles')

class Tag(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField(null=True)
    priority = models.FloatField(default=0)

    def __str__(self):
        return self.name

class UserTag(models.Model):
    user = models.ForeignKey('account.User',on_delete=models.CASCADE,related_name='usertags')
    tag = models.ForeignKey('account.Tag',on_delete=models.CASCADE,related_name='usertags')



