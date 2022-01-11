from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import(
    Region,Country,State,City,LocationData
)

class RegionSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(RegionSerializer,self).__init__(*args, **kwargs)

    class Meta:
        model = Region
        fields = '__all__'

class CountrySerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(CountrySerializer,self).__init__(*args, **kwargs)

    class Meta:
        model = Country
        fields = '__all__'
        # depth = 1


class StateSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(StateSerializer,self).__init__(*args, **kwargs)

    class Meta:
        model = State
        fields = '__all__'
        # depth = 1

class CitySerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(CitySerializer,self).__init__(*args, **kwargs)

    class Meta:
        model = City
        fields = '__all__'
        # depth = 1

class LocationDataSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(LocationDataSerializer,self).__init__(*args, **kwargs)

    class Meta:
        model = LocationData
        fields = '__all__'
        # depth = 1