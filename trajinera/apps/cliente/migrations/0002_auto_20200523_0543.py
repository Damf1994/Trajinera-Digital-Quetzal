# Generated by Django 3.0.3 on 2020-05-23 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercliente',
            name='direccion',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='usercliente',
            name='telefono',
            field=models.IntegerField(default=0),
        ),
    ]