from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField('Hello', max_length=50)
    task = models.TextField('say')

    def _str_(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задачи'
        verbose_name_plural = 'Задача'
