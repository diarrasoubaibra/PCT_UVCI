# Generated by Django 4.2.4 on 2023-09-04 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emplois', '0004_offreemploi_alter_demandeemploi_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offreemploi',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/offre_emplois'),
        ),
    ]
