# Generated by Django 4.0.3 on 2022-05-15 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0003_alter_arreglo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arreglo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
