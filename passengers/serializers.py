from rest_framework import serializers
from .models import City, Passenger


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("name", "population")


class PopulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = "__all__"
