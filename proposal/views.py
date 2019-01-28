from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from proposal.srializers import ProposalSerializer
from proposal.models import Proposal


class ProposalViewSet(viewsets.ModelViewSet):
  permission_classes = (AllowAny,)
  queryset = Proposal.objects.all()
  serializer_class = ProposalSerializer
# Create your views here.
