from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField('content')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'page'
        verbose_name_plural = 'pages'