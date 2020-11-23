from datetime import datetime

from django.db import models


class UserIdentifierModel(models.Model):
    id = models.IntegerField(primary_key=True)

    name = models.CharField(max_length=30, null=True, blank=True)
    second_name = models.CharField(max_length=30, null=True, blank=True)
    father_name = models.CharField(max_length=30, null=True, blank=True)
    date = models.DateField(auto_now_add = True)

    def __str__(self):
        return f'{self.id}: {self.name}'
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class AddressModel(models.Model):
    text = models.CharField(max_length=100, null=True, blank=True, unique=False)
    district = models.CharField(max_length=50, null=True, blank=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    longtitude = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    eas_address = models.IntegerField(null=True, blank=True)
    eas_bulding = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.latitude} - {self.longtitude}'
    
    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'
    

class MessageModel(models.Model):
    text = models.TextField()
    author = models.ForeignKey(UserIdentifierModel, on_delete=models.CASCADE)
    date = models.DateTimeField(default = datetime.now())

    danger_level = models.IntegerField(null=True, blank=True)
    event_class = models.CharField(max_length=30, null=True, blank=True)
    address = models.ForeignKey(AddressModel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.author} - {self.date}'
    
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'