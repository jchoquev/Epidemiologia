# Generated by Django 4.0.1 on 2022-02-09 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netlabv2', '0003_negativos_createat'),
    ]

    operations = [
        migrations.AddField(
            model_name='negativos',
            name='tvacuna2',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
