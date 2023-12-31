from django.urls import path
from passengers import views
from .views import (
    CitiesListAPIView,
    BrowserListAPIView,
    RainfallListAPIView,
    MonthListAPIView,
    SaleListAPIView,
    MultiModelView,
)

urlpatterns = [
    # highcharts data views
    path("highcharts/data/", views.chart_data, name="chart-data"),
    path("survived/data/", views.ticket_class_view, name="survived-data"),
    path("highcharts/", views.charts, name="charts"),
    # chart.js data views
    path("pie-chart/data/", views.pie_chart, name="pie-chart-data"),
    path(
        "population-chart/data/", views.population_chart, name="population-chart-data"
    ),
    path("chart-js/", views.chart_js, name="chart-js"),
    # DRF api's
    path("api/v1/cities/", CitiesListAPIView.as_view()),
    path("api/v1/browsers/", BrowserListAPIView.as_view()),
    path("api/v1/rainfall/", RainfallListAPIView.as_view()),
    path("api/v1/month/", MonthListAPIView.as_view()),
    path("api/v1/sales/", SaleListAPIView.as_view()),
    path("api/v1/multi/", MultiModelView.as_view()),
]
