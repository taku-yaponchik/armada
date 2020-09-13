from django.db import models

# Create your models here.


class Services(models.Model):
    '''Модель для наших услуг'''
    title = models.CharField(max_length=100, verbose_name='Наши услуги')
    image = models.ImageField(upload_to='services/', default='NoPhoto', verbose_name='Фото')

    class Meta:
        ordering = ('-title',)
        verbose_name = 'Наша услуга'
        verbose_name_plural = 'Наши услуги'

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    '''Модуль для наших работ'''
    title = models.CharField(max_length=100, verbose_name='Наши работы')
    image = models.ImageField(upload_to='portfolio/', default='NoPhoto', verbose_name='Фото')

    class Meta:
        ordering = ('-title',)
        verbose_name = 'Наша работа'
        verbose_name_plural = 'Наши работы'

    def __str__(self):
        return self.title


class Production(models.Model):
    '''Модуль для производство'''
    title = models.CharField(max_length=150, verbose_name='Производство')
    image = models.ImageField(upload_to='production/', default='NoPhoto', verbose_name='Фото')

    class Meta:
        ordering = ('-title',)
        verbose_name = 'Производство'
        verbose_name_plural = 'Производствы'

    def __str__(self):
        return self.title


class Price(models.Model):
    '''Модуль для прайса'''
    title = models.CharField(max_length=150, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Прайс')
    image = models.ImageField(upload_to='price/', default='NoPhoto', verbose_name='Фото')

    class Meta:
        ordering = ('-title',)
        verbose_name = 'Прайс'
        verbose_name_plural = 'Прайсы'

    def __str__(self):
        return self.title


class Customer(models.Model):
    '''Модуль для клиентов'''
    image = models.ImageField(upload_to='customer/', default='NoPhoto', verbose_name='Фото')
    name = models.CharField(max_length=100, verbose_name='Имя клиента')

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name


class Command(models.Model):
    '''Модуль для наших команд'''
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='customer/', default='NoPhoto')

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Наша команда'
        verbose_name_plural = 'Наши команды'

    def __str__(self):
        return self.name


class ContactClient(models.Model):
    '''Модуль для наших клиентов'''
    name = models.CharField(max_length=100, blank=True, verbose_name='Имя')
    phone = models.CharField(max_length=22, verbose_name='Номер телефона')

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Контакт клинта'
        verbose_name_plural = 'Контакты клиентов'

    def __str__(self):
        return self.name











