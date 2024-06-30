# Generated by Django 4.2.13 on 2024-06-25 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_color_marcarefri_modelorefri_alter_televisor_imagen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refrigeradora',
            name='costo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Costo'),
        ),
        migrations.AlterField(
            model_name='televisor',
            name='costo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Costo'),
        ),
    ]
