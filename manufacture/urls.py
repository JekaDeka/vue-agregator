from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .views import ManufactureViewSet, MasterViewSet, NumberViewSet
from .views_api import ManufactureFilterByLogin, MasterFilterByLogin, NumbersByManufacture, ManufactureByLoginPassword, MasterByLoginPassword, NumbersByMaster
router = routers.DefaultRouter()

router.register('manufacture', ManufactureViewSet)
router.register('master', MasterViewSet)
router.register('numbers', NumberViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('filter/numbers_by_manufacture/<int:id>',
         NumbersByManufacture.as_view()),
    path('filter/numbers_by_master/<int:id>', NumbersByMaster.as_view()),
    path('filter/manufacture_by_login/<login>',
         ManufactureFilterByLogin.as_view()),
    path('filter/master_by_login/<login>', MasterFilterByLogin.as_view()),
    path('filter/manufacture_by_login_password/<login>/<password>',
         ManufactureByLoginPassword.as_view()),
    path('filter/master_by_login_password/<login>/<password>',
         MasterByLoginPassword.as_view())
]
