# Generated by Django 4.2.8 on 2023-12-27 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('title', models.CharField(max_length=100, verbose_name='Название письма')),
                ('email', models.EmailField(blank=True, max_length=100, verbose_name='Почта')),
                ('text', models.TextField(blank=True, max_length=100, verbose_name='Тело письма')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Форма связи',
                'verbose_name_plural': 'Форма связи',
                'ordering': ['-created_at'],
            },
        ),
    ]