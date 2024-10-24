from datetime import datetime
import email

from time import time, timezone
from unicodedata import name
from django import db
from django.db import models


class Bb (models.Model):
    title=models.CharField(max_length=50, verbose_name='Товар')
    content=models.TextField(null=True, blank=True, verbose_name='Описание')
    price=models.FloatField(null=True, blank=True, verbose_name='Цена')
    publisched=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete = models.PROTECT, verbose_name='Рубрика')

    def __str__(self):
        return self.title

    def was_publisched_recently(self):
        return self.publisched >=(timezone.now() - datetime.timedelta(deys=7))

    class Meta:
        verbose_name_plural='Объявления'
        verbose_name='Объявление'
        ordering=['-publisched']

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name = 'Названия')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']

class Piople (models.Model):
    name = models.CharField(max_length=100, verbose_name = 'Имя')
    adress = models.EmailField(verbose_name = 'Почта')

    def __str__(self) -> str:
        return "%s %s" % (self.name, self.adress,)

    class Meta:
        verbose_name_plural = 'Имена'
        verbose_name = 'Имя'
        ordering = ['-name']
