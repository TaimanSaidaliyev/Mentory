from django.db import models


class Breeds (models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name='Название породы')
    animal_type = models.ForeignKey('AnimalClass', on_delete=models.CASCADE, blank=False, verbose_name='Вид животных')
    description = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='media/breeds/%Y/%m/%d', verbose_name='Изображение', blank=True)

    class Meta:
        verbose_name = 'Породы'
        verbose_name_plural = 'Порода'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class AnimalClass (models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name='Название класса животных')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='media/animalClass/%Y/%m/%d', verbose_name='Изображение', blank=True)

    class Meta:
        verbose_name = 'Класс животных'
        verbose_name_plural = 'Класс животных'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
