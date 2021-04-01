# Generated by Django 3.0.2 on 2020-07-22 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_auto_20200630_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='investment_type',
            field=models.CharField(choices=[('CH', 'Cash'), ('CI', 'Cash ISA'), ('EC', 'Equity Crowdfunding'), ('PN', 'Pension'), ('SO', 'Stock Options')], default='CH', max_length=2),
        ),
    ]