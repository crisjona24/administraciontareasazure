# Generated by Django 4.0.1 on 2022-10-30 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPAdministrarTareas', '0006_alter_estudiantecarrera_cedula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiantecarrera',
            name='carreraUniversitaria',
            field=models.CharField(max_length=30),
        ),
    ]
