# Generated by Django 5.0 on 2023-12-05 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='estado_hab',
            field=models.CharField(max_length=25, verbose_name='Estado da Habilitação'),
        ),
    ]