from django.db import models
from django.contrib.auth.models import User




class PCStatus(models.Model):
        # Основные параметры ПК
        pc_name = models.CharField(max_length=100, verbose_name="Имя ПК")
        ip_address = models.GenericIPAddressField(verbose_name="IP адрес")
        localhost_status = models.CharField(
            max_length=10,
            choices=[('free', 'Свободен'), ('busy', 'Занят'), ('unknown', 'Неизвестно')],
            default='unknown',
            verbose_name="Статус localhost"
        )

def __str__(self):
    return f"{self.pc_name} ({self.ip_address}) - {self.get_localhost_status_display()}"