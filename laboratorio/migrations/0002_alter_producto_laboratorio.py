# Generated by Django 4.1.1 on 2023-07-19 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='laboratorio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='laboratorio.laboratorio'),
        ),
    ]