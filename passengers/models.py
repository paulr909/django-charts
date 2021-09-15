from django.db import models


class Passenger(models.Model):
    MALE = "M"
    FEMALE = "F"
    SEX_CHOICES = ((MALE, "male"), (FEMALE, "female"))
    CHERBOURG = "C"
    QUEENSTOWN = "Q"
    SOUTHAMPTON = "S"
    PORT_CHOICES = (
        (CHERBOURG, "Cherbourg"),
        (QUEENSTOWN, "Queenstown"),
        (SOUTHAMPTON, "Southampton"),
    )
    name = models.CharField(max_length=100, blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    survived = models.BooleanField()
    age = models.FloatField(null=True)
    ticket_class = models.PositiveSmallIntegerField()
    embarked = models.CharField(max_length=1, choices=PORT_CHOICES)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Country"

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "City"

    def __str__(self):
        return self.name


class Browser(models.Model):
    name = models.CharField(max_length=100)
    y = models.FloatField()

    def __str__(self):
        return self.name


class Month(models.Model):
    month = models.CharField(max_length=3)

    class Meta:
        verbose_name_plural = "Month"

    def __str__(self):
        return self.month


class RainfallCity(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Rainfall City"

    def __str__(self):
        return self.name


class Rainfall(models.Model):
    value = models.FloatField()
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    city = models.ForeignKey(RainfallCity, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Rainfall"

    @property
    def month_value(self):
        return self.month.month

    @property
    def city_value(self):
        return self.city.name

    def __str__(self):
        return f"{self.city} - {self.month} - {self.value}"
