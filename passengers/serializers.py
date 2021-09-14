from rest_framework import serializers
from .models import Browser, City, Passenger


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("name", "population")


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = "__all__"


class BrowserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Browser
        fields = "__all__"
