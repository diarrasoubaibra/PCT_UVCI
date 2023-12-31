# Generated by Django 4.2.4 on 2023-08-30 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DemandeEmploi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auteur', models.CharField(max_length=100)),
                ('service_offert', models.CharField(max_length=200)),
                ('competences', models.TextField()),
                ('contact_tel', models.CharField(max_length=20)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='satic/image/demande_emploi/')),
                ('message', models.TextField()),
                ('prix_semaine', models.DecimalField(decimal_places=2, default=100, max_digits=10)),
                ('status', models.BooleanField(default=False)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('date_fin', models.DateTimeField()),
            ],
        ),
    ]
