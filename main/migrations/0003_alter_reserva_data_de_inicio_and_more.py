# Generated by Django 4.0.3 on 2022-04-27 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_reserva_hora_de_inicio_reserva_hora_de_termino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='data_de_inicio',
            field=models.DateField(blank=True, db_column='Data de inicio', null=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='data_de_termino',
            field=models.DateField(blank=True, db_column='Data de termino', null=True),
        ),
    ]