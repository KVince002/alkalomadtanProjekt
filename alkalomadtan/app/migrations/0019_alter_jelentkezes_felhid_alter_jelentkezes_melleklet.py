# Generated by Django 4.1.5 on 2023-02-08 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_jelentkezes_felhid_alter_jelentkezes_melleklet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jelentkezes',
            name='felhId',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='jelentkezes',
            name='melleklet',
            field=models.FileField(upload_to='feltoltottDokumentumok/felh_<django.db.models.fields.CharField>'),
        ),
    ]
