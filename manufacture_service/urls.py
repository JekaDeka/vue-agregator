from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .views import FaultViewSet,  ManufactureServiceViewSet, BreakageAtionViewSet

from .views_api import FaultByDeviceModel, ManufactureServiceByDeviceModel,  BreakageAtionByDeviceModel, FaultsBySparePart, BreakageActionByFault
from .views_api import FaultFilter, BreakageAtionByMark, ManufactureServiceByManufacture

router = routers.DefaultRouter()
router.register('fault', FaultViewSet)
router.register('manufacture_service', ManufactureServiceViewSet)
router.register('breakage_action', BreakageAtionViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('search/fault/device_model/<int:id>', FaultByDeviceModel.as_view()),
    path('search/manufacture_service/device_model/<int:id>',
         ManufactureServiceByDeviceModel.as_view()),
    path('search/breakage_action/device_modele/<int:id>',
         BreakageAtionByDeviceModel.as_view()),
    path('search/fault/spare_part/<int:id>', FaultsBySparePart.as_view()),
    path('search/breakage_action/fault/<int:id>',
         BreakageActionByFault.as_view()),
    path('filter/fault/<name>', FaultFilter.as_view()),
    path('filter/breakage_actions_by_mark/<int:id>',
         BreakageAtionByMark.as_view()),
    path('filter/manufacture_services_by_manufacture/<int:id>',
         ManufactureServiceByManufacture.as_view())


]
