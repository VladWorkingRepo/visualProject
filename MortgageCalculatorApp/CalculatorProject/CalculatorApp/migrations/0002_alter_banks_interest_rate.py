# Generated by Django 4.0.4 on 2022-05-25 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CalculatorApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banks',
            name='interest_rate',
            field=models.FloatField(),
        ),
    ]
