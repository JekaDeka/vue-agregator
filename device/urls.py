from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .views import MarkViewSet, BrandViewSet, DeviceModelViewSet, DeviceTypeViewSet, DeviceAffiliationViewSet, SparePartViewSet
from .views_api import DeviceTypesByAffilication, BrandsByDeviceType, DeviceModelByBrandDeviceType, SparePartByDeviceModel
from .views_api import DeviceTypeFilter, BrandFilter, DeviceModelFilter, MarkByBrand

router = routers.DefaultRouter()
router.register('mark', MarkViewSet)
router.register('brand', BrandViewSet)
router.register('device_type', DeviceTypeViewSet)
router.register('device_model', DeviceModelViewSet)
router.register('device_affiliation', DeviceAffiliationViewSet)
router.register('spare_part', SparePartViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/device_type/device_affiliation/<int:id>',
         DeviceTypesByAffilication.as_view()),
    path('search/brand/device_type/<int:id>', BrandsByDeviceType.as_view()),
    path('search/device_model/device_type/brand/<int:id_device_type>/<int:id_brand>',
         DeviceModelByBrandDeviceType.as_view()),
    path('search/spare_part/device_model/<int:id>',
         SparePartByDeviceModel.as_view()),
    path('filter/device_type/<name>', DeviceTypeFilter.as_view()),
    path('filter/brand/<name>', BrandFilter.as_view()),
    path('filter/device_model/<name>', DeviceModelFilter.as_view()),
    path('filter/marks_by_brand/<int:id>', MarkByBrand.as_view())
]
