# Generated by Django 4.0.2 on 2022-04-07 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parque', '0011_alter_parque_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parque',
            name='nome',
            field=models.CharField(blank=True, db_column='Nome', max_length=255, null=True),
        ),
    ]
