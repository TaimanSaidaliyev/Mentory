# Generated by Django 4.2.8 on 2023-12-28 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='breeds',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
    ]