# Generated by Django 3.0.2 on 2020-06-30 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20200629_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='investment_type',
            field=models.CharField(choices=[('CH', 'Cash'), ('CI', 'Cash ISA'), ('EC', 'Equity Crowdfunding'), ('PN', 'Pension')], default='CH', max_length=2),
        ),
    ]
