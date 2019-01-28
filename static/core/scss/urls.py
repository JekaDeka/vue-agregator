from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .views import FaultViewSet,  ManufactureServiceViewSet, BreakageAtionViewSet

from .views_api import FaultByDeviceModel
router = routers.DefaultRouter()
router.register('fault', FaultViewSet)
router.register('manufacture_service', ManufactureServiceViewSet)
router.register('breakage_action', BreakageAtionViewSet)


urlpatterns = [
    path('search/fault/device_model/<int:id>', FaultByDeviceModel.as_view())
]
