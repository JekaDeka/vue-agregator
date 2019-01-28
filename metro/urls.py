from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .views import TownViewSet, CountryViewSet, MetroViewSet
from .views_api import TownByCountru, MetroByTown, MetroByTownName
from .views_api import MetroFilter, TownByCountryName

router = routers.DefaultRouter()

router.register('metro', MetroViewSet)
router.register('town', TownViewSet)
router.register('country', CountryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/town_by_coutnry/<int:id>', TownByCountru.as_view()),
    path('search/metro_by_town/<int:id>', MetroByTown.as_view()),
    path('search/metro_by_town_name/<town>', MetroByTownName.as_view()),
    path('filter/metro/<name>', MetroFilter.as_view()),
    path('filter/town_by_coutnry_name/<name>', TownByCountryName.as_view()),

]
