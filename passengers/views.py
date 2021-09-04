from django.db.models import Count, Sum, Q
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from .models import Passenger, City
from .serializers import CitiesSerializer, PopulationSerializer


def home(request):
    return render(request, "home.html")


def charts(request):
    # list items
    passengers = Passenger.objects.all().order_by("id")[:10]
    last_passengers = Passenger.objects.all().order_by("-id")[:10:-1]
    context = {"passengers": passengers, "last_passengers": last_passengers}
    return render(request, "highcharts.html", context=context)


def chart_data(request):
    dataset = (
        Passenger.objects.values("embarked")
        .exclude(embarked="")
        .annotate(total=Count("embarked"))
        .order_by("embarked")
    )

    port_name = dict()
    for port_tuple in Passenger.PORT_CHOICES:
        port_name[port_tuple[0]] = port_tuple[1]

    chart = {
        "chart": {"type": "pie"},
        "title": {"text": "Titanic's Passengers By Embarkation Port"},
        "credits": {"enabled": False},
        "series": [
            {
                "name": "Embarkation Port",
                "data": list(
                    map(
                        lambda row: {
                            "name": port_name[row["embarked"]],
                            "y": row["total"],
                        },
                        dataset,
                    )
                ),
            }
        ],
    }

    return JsonResponse(chart)


def survived(request):
    return render(request, "survived.html")


def ticket_class_view(request):
    dataset = (
        Passenger.objects.values("ticket_class")
        .annotate(
            survived_count=Count("ticket_class", filter=Q(survived=True)),
            not_survived_count=Count("ticket_class", filter=Q(survived=False)),
        )
        .order_by("ticket_class")
    )

    tickets = [i["ticket_class"] for i in dataset]
    survivors = [i["survived_count"] for i in dataset]
    not_survived = [i["not_survived_count"] for i in dataset]

    chart = {
        "chart": {"type": "column"},
        "title": {"text": "Titanic Survivors by Ticket Class"},
        "credits": {"enabled": False},
        "xAxis": {
            "categories": tickets,
            "labels": {"format": "Class {text}"},
        },
        "yAxis": {"title": None},
        "series": [
            {
                "name": "Survived",
                "data": survivors,
                "color": "#28a745",
            },
            {
                "name": "Not survived",
                "data": not_survived,
                "color": "#dc3545",
            },
        ],
        "tooltip": {
            "shared": True,
            "useHTML": True,
            "headerFormat": "<small>Class {point.key}</small><table>",
            "pointFormat": '<tr><td style="color: {series.color}">{series.name}: </td>'
            + '<td style="text-align: right"><b>{point.y}</b></td></tr>',
            "footerFormat": "</table>",
            "valueDecimals": 2,
        },
    }

    return JsonResponse(chart)


def chart_js(request):
    return render(request, "chart-js.html")


def population_chart(request):
    labels = []
    data = []

    queryset = (
        City.objects.values("country__name")
        .annotate(country_population=Sum("population"))
        .order_by("-country_population")
    )
    for entry in queryset:
        labels.append(entry["country__name"])
        data.append(entry["country_population"])

    return JsonResponse(
        data={
            "labels": labels,
            "data": data,
        }
    )


def pie_chart(request):
    labels = []
    data = []

    queryset = City.objects.order_by("-population")[:5]
    for city in queryset:
        labels.append(city.name)
        data.append(city.population)

    return JsonResponse(
        data={
            "labels": labels,
            "data": data,
        },
    )


class CitiesListAPIView(ListAPIView):
    queryset = City.objects.all()[:3]
    serializer_class = CitiesSerializer
    permission_classes = (AllowAny,)


class PopulationListAPIView(ListAPIView):
    queryset = Passenger.objects.all()[10:14]
    serializer_class = PopulationSerializer
    permission_classes = (AllowAny,)
