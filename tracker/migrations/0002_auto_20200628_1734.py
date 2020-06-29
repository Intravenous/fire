# Generated by Django 3.0.2 on 2020-06-28 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='investment_type',
            field=models.CharField(choices=[('CH', 'Cash'), ('PN', 'Cash ISA'), ('CI', 'Crowd Investment'), ('PN', 'Pension')], default='CH', max_length=2),
        ),
    ]