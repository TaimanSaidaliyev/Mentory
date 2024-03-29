# Generated by Django 4.2.8 on 2023-12-27 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название класса животных')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('photo', models.ImageField(blank=True, upload_to='media/animalClass/%Y/%m/%d', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Класс животных',
                'verbose_name_plural': 'Класс животных',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Breeds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название породы')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('photo', models.ImageField(blank=True, upload_to='media/breeds/%Y/%m/%d', verbose_name='Изображение')),
                ('animal_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.animalclass', verbose_name='Вид животных')),
            ],
            options={
                'verbose_name': 'Породы',
                'verbose_name_plural': 'Порода',
                'ordering': ['-created_at'],
            },
        ),
    ]
