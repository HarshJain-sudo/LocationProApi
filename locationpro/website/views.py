from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import*
from .serializers import*

class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_queryset(self):
        country_var = self.kwargs.get('region',None)
        queryset = self.queryset.filter(region__name = country_var)
        return queryset

class StateListAPIView(ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

    def get_queryset(self):
        region = self.kwargs.get('region',None)
        country = self.kwargs.get('country',None)
        queryset = self.queryset.filter(
            country__name =country,
            country__region__name = region )
        return queryset

class CityListAPIView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_queryset(self):
        region = self.kwargs.get('region',None)
        country = self.kwargs.get('country',None)
        state = self.kwargs.get('state',None)
        queryset = self.queryset.filter(
            state__country__name =country,
            state__country__region__name = region )
        return queryset

class LocationDataListAPIView(ListAPIView):
    queryset = LocationData.objects.all()
    serializer_class = LocationDataSerializer

    def get_queryset(self):
        region = self.kwargs.get('region',None)
        country = self.kwargs.get('country',None)
        state = self.kwargs.get('state',None)
        city =  self.kwargs.get('city',None)
        queryset = self.queryset.filter(
            city__state__country__region__name =region,
            city__state__country__name= country,
            city__state__name = state)
        return queryset
