# Generated by Django 4.2.4 on 2023-08-30 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emplois', '0002_rename_auteur_demandeemploi_nom_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demandeemploi',
            name='prix_semaine',
        ),
    ]
