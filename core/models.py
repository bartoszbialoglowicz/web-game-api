from distutils.command.upload import upload
import uuid
import os

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth import get_user_model
from annoying.fields import AutoOneToOneField


def character_image_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/characters/', filename)

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
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_new = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'


TIER_LIST = [
    (1, "Common"),
    (2, "Rare"),
    (3, "Epic"),
    (4, "Mythic"),
    (5, "Legendary"),
]


class Stats(models.Model):
    """Base stats for items and Characters"""
    damage = models.IntegerField()
    health = models.IntegerField()
    armor = models.IntegerField()
    resists = models.IntegerField()
    critical_percent = models.IntegerField()
    critical_damge = models.IntegerField()

    def __str__(self):
        return str(self.damage) + ' ' + str(self.health) + ' ' + str(self.armor)


class Trait(models.Model):
    """Trait which gives bonuses to charcter. Each character can have a multiple traits"""
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.name


class Character(models.Model):
    """Character model which player collects during the game"""
    base_stats = models.OneToOneField(Stats, on_delete=models.CASCADE, unique=False)
    traits = models.ManyToManyField(Trait)
    name = models.CharField(max_length=128)
    power = models.IntegerField()
    tier = models.IntegerField(choices=TIER_LIST)
    image = models.ImageField(null=True, upload_to=character_image_file_path)

    class Meta:
        ordering = ['-power']

    def __str__(self):
        return self.name + ' ' + str(self.power)


class Item(models.Model):
    """Item model"""
    name = models.CharField(max_length=128)
    tier = models.IntegerField(choices=TIER_LIST)
    base_stats = models.ForeignKey(Stats, on_delete=models.CASCADE, unique=False)


class UserResources(models.Model):
    """Store for all items and characters collected by user"""
    user = AutoOneToOneField(get_user_model(), on_delete=models.CASCADE)
    characters = models.ManyToManyField(Character, blank=True)
    items = models.ManyToManyField(Item, blank=True)
    gold = models.IntegerField(default=100)
    experience = models.IntegerField(default=0)
    lvl = models.IntegerField(default=1)

    def __str__(self):
	    return str(self.user)


class Store(models.Model):
    """Model available chest in store"""
    name = models.CharField(max_length=128)
    quantity = models.IntegerField()
    price = models.IntegerField()
    common_chance = models.IntegerField()
    rare_chance = models.IntegerField()
    epic_chance = models.IntegerField()
    mythic_chance = models.IntegerField()
    legendary_chance = models.IntegerField()


class Chest(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class CharacterChest(Chest):
    characters = models.ManyToManyField(Character)


class ItemChest(Chest):
    items = models.ManyToManyField(Item)



