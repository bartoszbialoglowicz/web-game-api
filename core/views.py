from cgitb import lookup
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from core import serializers
from core.models import Character, Item, Enemy, Room, Location, UserResources, Quest, AvailableQuest, Trait, Stats, Store, ItemChest, CharacterChest, Chest



class BaseResourcesViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class CharacterViewSet(BaseResourcesViewSet):
    queryset = Character.objects.all()
    serializer_class = serializers.CharacterSerializer

    def _params_to_ints(self, qs):
        """Convert a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        traits = self.request.query_params.get('traits')
        base_stats = self.request.query_params.get('base_stats')
        queryset = self.queryset
        if traits:
            trait_ids = self._params_to_ints(traits)
            queryset = queryset.filter(traits__id__in=trait_ids)
        if base_stats:
            base_stats_ids = self._params_to_ints(base_stats)
            queryset = queryset.filter(base__stats__id__in=base_stats_ids)

        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.CharaterDetailSerializer

        return self.serializer_class


class ItemViewSet(BaseResourcesViewSet):
    queryset = Item.objects.all()
    serializer_class = serializers.ItemSerializer


class UserResourcesViewSet(BaseResourcesViewSet):
    queryset = UserResources.objects.all()
    serializer_class = serializers.UserResourceSerializer

    def get_queryset(self):
        print(self.request.user.userresources)
        queryset = self.queryset.filter(user=self.request.user)
        return queryset


class UserResourcesPartialUpdate(viewsets.GenericViewSet,
                                    mixins.UpdateModelMixin):
    serializer_class = serializers.UserResourceUpdateSerializer
    queryset = UserResources.objects.all()
    lookup_field = 'user'
    

class TraitViewSet(BaseResourcesViewSet):
    queryset = Trait.objects.all()
    serializer_class = serializers.TraitSerializer


class StatsViewSet(BaseResourcesViewSet):
    queryset = Stats.objects.all()
    serializer_class = serializers.StatsSerializer


class QuestViewSet(BaseResourcesViewSet):
    queryset = Quest.objects.all()
    serializer_class = serializers.QuestSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(lvl_required__lte=self.request.user.userresources.lvl)
        return queryset

class AvailableQuestViewSet(BaseResourcesViewSet):
    queryset = AvailableQuest.objects.all()
    serializer_class = serializers.AvailableQuestSerializer

    def get_queryset(self):
        print(self.request.user.availablequest)
        queryset = self.queryset.filter(user=self.request.user)
        return queryset


class AvailableQuestUpdateViewSet(viewsets.GenericViewSet,
                                    mixins.UpdateModelMixin):
    queryset = AvailableQuest.objects.all()
    serializer_class = serializers.AvailableQuestUpdateSerializer
    lookup_field = 'id'

class StoreViewSet(BaseResourcesViewSet):
    queryset = Store.objects.all()
    serializer_class = serializers.StoreSerializer


class ChestViewSet(BaseResourcesViewSet):
    queryset = Chest.objects.all()
    serializer_class = serializers.ChestSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(owner=self.request.user)
        return queryset


class ItemChestViewSet(BaseResourcesViewSet):
    queryset = ItemChest.objects.all()
    serializer_class = serializers.ItemChestSerializer


class CharacterChestViewSet(BaseResourcesViewSet):
    queryset = CharacterChest.objects.all()
    serializer_class = serializers.CharacterChestSerializer


class EnemyViewSet(BaseResourcesViewSet):
    queryset = Enemy.objects.all()
    serializer_class = serializers.EnemySerializer


class RoomViewSet(BaseResourcesViewSet):
    queryset = Room.objects.all()
    serializer_class = serializers.RoomSerializer


class LocationViewSet(BaseResourcesViewSet):
    queryset = Location.objects.all()
    serializer_class = serializers.LocationSerializer