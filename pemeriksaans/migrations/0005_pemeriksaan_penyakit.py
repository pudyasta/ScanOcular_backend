# Generated by Django 4.2.4 on 2023-09-03 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pemeriksaans', '0004_pemeriksaan_diagnosa'),
    ]

    operations = [
        migrations.AddField(
            model_name='pemeriksaan',
            name='penyakit',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
