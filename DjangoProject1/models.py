from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    score = models.IntegerField(verbose_name="Очки", default=0)
    level = models.IntegerField(verbose_name="Уровень", default=1)

 # class tachka(AbstractUser):
 #     is_active = models.BooleanField(default=True)

