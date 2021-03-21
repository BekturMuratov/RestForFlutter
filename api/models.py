from django.contrib.auth.models import AbstractUser, Group
from django.db import models

from RestForFlutter.models import BaseModel
from api.provider import UserAccountManager


class User(BaseModel, AbstractUser):
    groups = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, default=1)
    email = models.EmailField(max_length=50, unique=True)

    objects = UserAccountManager()

    REQUIRED_FIELDS = ['groups_id', 'email']

    def __str__(self):
        return self.username.__str__()

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name


class Category(BaseModel):
    name = models.CharField(max_length=30, blank=True, default='category_name')
    main_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True,
                                      related_name='add_main_category')


class Advert(BaseModel):
    advert_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=300, blank=True, default='advert_name')
    description = models.TextField(max_length=5000, blank=True, default="advert_description")
    price = models.IntegerField(blank=False, default='1')
    phone = models.IntegerField(blank=False, default='+996700806860')
    whatsapp = models.CharField(max_length=300, blank=True, default='whatsapp')
