# Generated by Django 4.1.5 on 2023-02-22 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_jelentkezes_melleklet'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='munka',
            options={'ordering': ['-katt']},
        ),
    ]
