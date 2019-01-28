"""agregator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token, ObtainJSONWebToken


from django.contrib import admin
from django.conf.urls import url

from django.views.generic import TemplateView
from django.urls import path, include
from rest_framework import routers
# from device.views import BrandViewSet, DeviceModelViewSet, SparePartViewSet, MarkViewSet, DeviceTypeViewSet
from manufacture.views import ManufactureViewSet, MasterViewSet
from manufacture_service.views import ManufactureServiceViewSet, FaultViewSet, BreakageAtionViewSet
from metro.views import MetroViewSet
from proposal.views import ProposalViewSet


urlpatterns = [
    path('', include('core.urls')),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('api/device/', include('device.urls')),
    path('api/manufacture_service/', include('manufacture_service.urls')),
    path('api/metro/', include('metro.urls')),
    path('api/proposal/', include('proposal.urls')),
    path('api/manufacture/', include('manufacture.urls')),

]
