# Generated by Django 4.0.1 on 2022-02-12 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netlabv2', '0004_negativos_tvacuna2'),
    ]

    operations = [
        migrations.AddField(
            model_name='negativos',
            name='deleteAt',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='negativos',
            name='updateAt',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='negativos',
            name='createAt',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
