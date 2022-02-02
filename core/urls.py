from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core import views


router = DefaultRouter()
router.register('characters', views.CharacterViewSet)
router.register('items', views.ItemViewSet)
router.register('userresources', views.UserResourcesViewSet)
router.register('resourcesupdate', views.UserResourcesPartialUpdate)
router.register('traits', views.TraitViewSet)
router.register('stats', views.StatsViewSet)
router.register('store', views.StoreViewSet)
router.register('chest', views.ChestViewSet)
router.register('itemchest', views.ItemChestViewSet)
router.register('characterchest', views.CharacterChestViewSet)

app_name = 'resources'

urlpatterns = [
    path('', include(router.urls))
]