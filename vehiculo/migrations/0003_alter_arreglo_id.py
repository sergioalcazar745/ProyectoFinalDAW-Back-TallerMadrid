# Generated by Django 4.0.3 on 2022-05-15 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0002_vehiculo_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arreglo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
