# Generated by Django 4.1.5 on 2023-02-07 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_remove_munka_ertekeles_alter_jelentkezes_melleklet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jelentkezes',
            name='melleklet',
            field=models.FileField(upload_to='feltoltottDokumentumok/felh_<django.db.models.fields.related.ForeignKey>'),
        ),
    ]
