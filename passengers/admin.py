from django.contrib import admin
from .models import (
    Browser,
    City,
    Country,
    Passenger,
    Month,
    Rainfall,
    RainfallCity,
    Sale,
    Team,
)

admin.site.register(Browser)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Passenger)
admin.site.register(Month)
admin.site.register(Rainfall)
admin.site.register(RainfallCity)
admin.site.register(Sale)
admin.site.register(Team)
