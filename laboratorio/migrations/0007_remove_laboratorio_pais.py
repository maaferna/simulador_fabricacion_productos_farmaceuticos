# Generated by Django 4.1.1 on 2023-07-19 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0006_alter_laboratorio_pais'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laboratorio',
            name='pais',
        ),
    ]
