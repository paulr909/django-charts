from django.urls import path
from passengers import views
from .views import CitiesListAPIView, PassengerListAPIView

urlpatterns = [
    # highcharts data views
    path("highcharts/data/", views.chart_data, name="chart-data"),
    path("survived/data/", views.ticket_class_view, name="survived-data"),
    path("highcharts/", views.charts, name="charts"),
    path("survived/", views.survived, name="survived"),
    # chart.js data views
    path("pie-chart/data/", views.pie_chart, name="pie-chart-data"),
    path(
        "population-chart/data/", views.population_chart, name="population-chart-data"
    ),
    path("chart-js/", views.chart_js, name="chart-js"),
    # DRF api's
    path("api/v1/cities/", CitiesListAPIView.as_view()),
    path("api/v1/passengers/", PassengerListAPIView.as_view()),
]
