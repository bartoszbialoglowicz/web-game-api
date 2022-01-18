from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core import views


router = DefaultRouter()
router.register('characters', views.CharacterViewSet)
router.register('items', views.ItemViewSet)
router.register('userresources', views.UserResourcesViewSet)
router.register('traits', views.TraitViewSet)
router.register('stats', views.StatsViewSet)

app_name = 'resources'

urlpatterns = [
    path('', include(router.urls))
]