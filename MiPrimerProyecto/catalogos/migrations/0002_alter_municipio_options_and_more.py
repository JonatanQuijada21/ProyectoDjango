# Generated by Django 4.2.5 on 2023-09-22 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='municipio',
            options={'verbose_name': 'Municipio', 'verbose_name_plural': 'Municipios'},
        ),
        migrations.RenameField(
            model_name='municipio',
            old_name='Departamento',
            new_name='departamento',
        ),
    ]
