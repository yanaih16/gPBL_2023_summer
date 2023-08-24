from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser):
    sex_data = [
        (1, '男'),
        (2, '女'),
        (3, 'その他'),
    ]
    date_joined = None
    first_name = None
    last_name = None
    sex = models.IntegerField(choices=sex_data)
    birthday = models.DateField()
    adress = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS = ["sex", "birthday"]


class Item(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.PROTECT)
    name = models.CharField(max_length=255)
    text = models.TextField()
    value = models.IntegerField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=255)

class Item_Tag(models.Model):
    item_id = models.ForeignKey(Item, on_delete = models.PROTECT)
    tag_id = models.ForeignKey(Tag, on_delete = models.PROTECT)

class Matching(models.Model):
    seller_id = models.ForeignKey(User, on_delete = models.PROTECT, related_name='seller_user')
    buyer_id = models.ForeignKey(User, on_delete = models.PROTECT, related_name='buyer_user')
    item_id = models.ForeignKey(Item, on_delete = models.PROTECT)
    matching_date = models.DateTimeField(auto_now_add=True)

class Chat(models.Model):
    matching_id = models.ForeignKey(Matching, on_delete = models.PROTECT)
    sender_id = models.ForeignKey(User, on_delete = models.PROTECT)
    text = models.TextField()
    sented_at = models.DateTimeField(auto_now_add=True)

class review(models.Model):
    rater_id = models.ForeignKey(Matching, on_delete = models.PROTECT, related_name='rater_user')
    evaluator_id = models.ForeignKey(Matching, on_delete = models.PROTECT, related_name='evaluator_user')
    score = models.IntegerField()
    text = models.TextField()
    