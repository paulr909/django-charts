from django.contrib import admin
from django.urls import path, include

from passengers import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("", include("passengers.urls")),
    path("api/users/", include("authentication.urls", namespace="authentication")),
]
