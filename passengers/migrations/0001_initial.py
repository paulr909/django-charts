# Generated by Django 3.2 on 2021-09-04 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('sex', models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=1)),
                ('survived', models.BooleanField()),
                ('age', models.FloatField(null=True)),
                ('ticket_class', models.PositiveSmallIntegerField()),
                ('embarked', models.CharField(choices=[('C', 'Cherbourg'), ('Q', 'Queenstown'), ('S', 'Southampton')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('population', models.PositiveIntegerField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passengers.country')),
            ],
        ),
    ]
