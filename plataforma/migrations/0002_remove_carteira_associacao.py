# Generated by Django 4.1.5 on 2023-01-15 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carteira',
            name='associacao',
        ),
    ]
