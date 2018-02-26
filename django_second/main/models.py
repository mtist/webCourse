from django.db import models


class Person(models.Model):
    name = models.CharField('Имя', max_length=30)
    surname = models.CharField('Фамилия', max_length=30)
    about = models.TextField('О персоне')
    weight = models.PositiveSmallIntegerField('Вес')
    birth = models.DateField('Дата рождения')

    class Meta:
        verbose_name = 'Персона'
        verbose_name_plural = 'Персоны'
        ordering = ['name']

    def __str__(self):
        return self.surname + ' ' + self.name
