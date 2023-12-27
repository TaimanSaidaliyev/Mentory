from django.db import models


class ContactForm (models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name='ФИО')
    title = models.CharField(max_length=100, blank=False, verbose_name='Название письма')
    email = models.EmailField(max_length=100, blank=True, verbose_name='Почта')
    text = models.TextField(max_length=100, blank=True, verbose_name='Тело письма')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Форма связи'
        verbose_name_plural = 'Форма связи'
        ordering = ['-created_at']

    def __str__(self):
        return self.title