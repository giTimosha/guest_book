from django.db import models


RECORD_STATUS_CHOICES = (
    ('active', 'Активно'),
    ('blocked', 'Заблокировано')
)

class Record(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    text = models.TextField(max_length=2000, verbose_name='Запись')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.CharField(max_length=20, verbose_name='Стратус',
                                choices=RECORD_STATUS_CHOICES, default=RECORD_STATUS_CHOICES[0][0])

    def __str__(self):
        return self.name
