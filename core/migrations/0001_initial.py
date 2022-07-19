# Generated by Django 4.0.6 on 2022-07-19 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WisdomQuotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'Citação',
                'verbose_name_plural': 'Citações',
            },
        ),
        migrations.CreateModel(
            name='WorkedHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('worked_hours', models.TimeField()),
                ('description', models.CharField(max_length=200)),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Hora',
                'verbose_name_plural': 'Horas',
            },
        ),
    ]