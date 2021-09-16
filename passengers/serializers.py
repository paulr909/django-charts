from rest_framework import serializers
from .models import Browser, City, Rainfall, Month, Sale


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("name", "population")


class BrowserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Browser
        fields = "__all__"


class RainfallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rainfall
        fields = ("id", "value", "month", "month_value", "city", "city_value")


class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Month
        fields = "__all__"


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ("id", "value", "month", "month_value", "team", "team_value")
