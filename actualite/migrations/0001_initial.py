# Generated by Django 4.2.4 on 2023-08-26 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actualite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.DateField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('photo', models.FileField(upload_to='static/images/actualite')),
                ('date_pub', models.DateField()),
                ('update_pub', models.DateField(auto_now=True)),
            ],
        ),
    ]