# Generated by Django 4.1.5 on 2023-01-15 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0003_carteira_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carteira',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='carteiras'),
        ),
    ]