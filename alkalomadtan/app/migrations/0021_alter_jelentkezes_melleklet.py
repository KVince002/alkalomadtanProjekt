# Generated by Django 4.1.7 on 2023-03-08 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_munka_options_alter_jelentkezes_melleklet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jelentkezes',
            name='melleklet',
            field=models.FileField(upload_to='feltoltottDokumentumok/'),
        ),
    ]