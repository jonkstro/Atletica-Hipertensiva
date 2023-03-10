# Generated by Django 4.1.5 on 2023-01-13 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carteira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=64)),
                ('cpf', models.IntegerField()),
                ('matricula', models.IntegerField()),
                ('associacao', models.IntegerField()),
                ('data_nasc', models.DateField()),
                ('data_exped', models.DateField()),
                ('data_valid', models.DateField()),
            ],
        ),
    ]
