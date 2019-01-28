from rest_framework import generics
from .srializers import ProposalSerializer
from .models import Proposal
from metro.models import Metro


class ProposalByMetro(generics.ListAPIView):
  serializer_class = ProposalSerializer

  def get_queryset(self):
    id = self.kwargs['id']

    return Proposal.objects.filter(metro_id=id)


class ProposalByManufacture (generics.ListAPIView):
  serializer_class = ProposalSerializer

  def get_queryset(self):
    id = self.kwargs['id']

    return Proposal.objects.filter(manufacture_id=id)
