# Generated by Django 3.0.2 on 2020-06-29 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_investment_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]
