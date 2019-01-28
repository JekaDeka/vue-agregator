from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .views import ProposalViewSet
from .views_api import ProposalByMetro, ProposalByManufacture

router = routers.DefaultRouter()
router.register('proposal', ProposalViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('filter/proposals_by_metro/<int:id>', ProposalByMetro.as_view()),
    path('filter/proposal_by_manufacture/<int:id>',
         ProposalByManufacture.as_view())
]
