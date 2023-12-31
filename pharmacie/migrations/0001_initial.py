# Generated by Django 4.2.4 on 2023-08-26 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pharmacie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_phar', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('photo', models.FileField(upload_to='static/images/pharmacie')),
                ('periode_de_garde', models.CharField(blank=True, max_length=255, null=True)),
                ('localisation', models.CharField(max_length=100)),
            ],
        ),
    ]
