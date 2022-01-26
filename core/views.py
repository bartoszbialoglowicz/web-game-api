import re
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core import serializers
from core.models import Character, Item, UserResources, Trait, Stats



class BaseResourcesViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin):
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
    

class TraitViewSet(BaseResourcesViewSet):
    queryset = Trait.objects.all()
    serializer_class = serializers.TraitSerializer


class StatsViewSet(BaseResourcesViewSet):
    queryset = Stats.objects.all()
    serializer_class = serializers.StatsSerializer
