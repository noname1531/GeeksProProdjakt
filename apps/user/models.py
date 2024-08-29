from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя'),
    password = models.CharField(max_length=50, verbose_name='Пароль'),
    password2 = models.CharField(max_length=50, verbose_name='Подверждения пороля'),

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'