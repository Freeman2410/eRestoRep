# Generated by Django 5.1.4 on 2024-12-12 19:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie_plats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_categorie', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Categorie_plats',
                'verbose_name_plural': 'Categorie_plats',
            },
        ),
        migrations.CreateModel(
            name='FormulaireCommande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('sexe', models.CharField(max_length=250)),
                ('ville', models.CharField(max_length=250)),
                ('pays', models.CharField(max_length=250)),
                ('adresse', models.CharField(max_length=250)),
                ('tel', models.CharField(max_length=250)),
                ('zipcode', models.CharField(max_length=250)),
                ('date', models.DateTimeField(auto_now=True)),
                ('commande', models.CharField(max_length=1000)),
                ('sommeTotal', models.CharField(max_length=1000)),
                ('quantiteTotal', models.CharField(max_length=1000)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='FormulaireContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=250)),
                ('commentaire', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region_plats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_region', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Region_plats',
                'verbose_name_plural': 'Region_plats',
            },
        ),
        migrations.CreateModel(
            name='Plat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_plat', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=500)),
                ('prix', models.PositiveIntegerField()),
                ('etat', models.BooleanField(default=False)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categorie_plats')),
                ('region_de_provenance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.region_plats')),
            ],
            options={
                'verbose_name': 'Plat',
                'verbose_name_plural': 'Plats',
            },
        ),
    ]