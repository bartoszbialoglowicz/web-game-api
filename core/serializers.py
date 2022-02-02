from asyncore import read
from rest_framework import serializers

from core import models
from user.serializers import UserSerializer
from drf_writable_nested import WritableNestedModelSerializer


class TraitSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Trait
        fields = ('id', 'name', 'description')


class StatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Stats
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):

    traits = TraitSerializer(read_only=True, many=True)

    base_stats = StatsSerializer(read_only=True)

    class Meta:
        model = models.Character
        fields = ('id', 'name', 'power', 'tier', 'base_stats', 'traits', 'image')


class CharaterDetailSerializer(CharacterSerializer):

    traits = TraitSerializer(many=True, read_only=True)
    base_stats = StatsSerializer(many=False, read_only=True)
    

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Item
        fields = '__all__'


class UserResourceSerializer(WritableNestedModelSerializer,
                                serializers.ModelSerializer):

    characters = CharacterSerializer(many=True)
    items = ItemSerializer(many=True)

    class Meta:
        model = models.UserResources
        fields = ('id', 'user', 'characters', 'items', 'lvl', 'gold', 'experience')

class UserResourceUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserResources
        fields = ('user', 'characters', 'items', 'lvl', 'gold', 'experience')


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Store
        fields = '__all__'


class ChestSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Chest
        fields = '__all__'


class ItemChestSerializer(serializers.ModelSerializer):
    
    items = ItemSerializer(many=True)

    class Meta:
        model = models.ItemChest
        fields = '__all__'


class CharacterChestSerializer(serializers.ModelSerializer):

    characters = CharacterSerializer(many=True)

    class Meta:
        model = models.CharacterChest
        fields = '__all__'
