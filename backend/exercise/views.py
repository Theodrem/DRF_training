from django.views.generic import GenericViewError
from django_filters import rest_framework as filters
from rest_framework import generics, permissions

from .models import Hero
from .serializers import HeroSerializer

# Create your views here.
class HeroFilter(filters.FilterSet):
    id = filters.NumberFilter(field_name="id")
    life = filters.NumberFilter(field_name="life")
    attack = filters.NumberFilter(field_name="attack")
    origin = filters.CharFilter(field_name="origin", lookup_expr='icontains') #icontains name

class PostHeroView(generics.CreateAPIView):
    filter_backends = (filters.DjangoFilterBackend,)
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

class GetHeroView(generics.ListAPIView):
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HeroFilter
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

class UpdateHeroView(generics.UpdateAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    



    


