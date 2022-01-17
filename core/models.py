from pyexpat import model
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth import get_user_model

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that suppors using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_new = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'


TIER_LIST = [
    ("Common", 1),
    ("Rare", 2),
    ("Epic", 3),
    ("Mythic", 4),
    ("Legendary", 5),
]


class Stats(models.Model):
    """Base stats for items and Characters"""
    damage = models.IntegerField()
    health = models.IntegerField()
    armor = models.IntegerField()
    resists = models.IntegerField()
    critical_percent = models.IntegerField()
    critical_damge = models.IntegerField()


class Trait(models.Model):
    """Trait which gives bonuses to charcter. Each character can have a multiple traits"""
    name = models.CharField(max_length=128)
    description = models.TextField()


class Character(models.Model):
    """Character model which player collects during the game"""
    base_stats = models.ForeignKey(Stats, on_delete=models.CASCADE)
    traits = models.ManyToManyField(Trait)
    name = models.CharField(max_length=128)
    profession = models.CharField(max_length=64)
    power = models.IntegerField()
    tier = models.IntegerField(choices=TIER_LIST)


class Item(models.Model):
    """Item model"""
    name = models.CharField(max_length=128)
    tier = models.IntegerField(choices=TIER_LIST)
    base_stats = models.ForeignKey(Stats, on_delete=models.CASCADE)


class UserResources(models.Model):
    """Store for all items and characters collected by user"""
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    characters = models.ManyToManyField(Character)
    items = models.ManyToManyField(Item)
