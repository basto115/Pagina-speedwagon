# Generated by Django 5.0.6 on 2024-07-04 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('user', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
