from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import models
from django.urls import reverse
from GameGym import settings

class Pc(models.Model):
    Time_busy = models.TimeField(null=True, blank=True)
    busy = models.BooleanField()
    tech_ac = models.BooleanField()


# class Clients(models.Model):
#     FIO = models.TextField(max_length=120)
#     email = models.TextField(max_length=60)
#     number = models.IntegerField()
#     password = models.TextField(max_length=60)
#     def __str__(self):
#         return self.FIO

class Type_pc(models.Model):
    PC_id = models.ForeignKey(
        Pc,
        on_delete=models.CASCADE,
    )
    price = models.IntegerField()
    type = models.TextField(max_length=20)

class Time_base(models.Model):
    PC_id = models.ForeignKey(
        Type_pc,
        on_delete=models.CASCADE,
    )
    ID_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name = "Имя",
        on_delete=models.CASCADE,
    )
    ID_pc = models.ForeignKey(
        Pc,
        on_delete=models.CASCADE,
    )

class back_connection(models.Model):
    FIO = models.TextField(max_length=120)
    number = models.IntegerField()
    Convenient_time = models.TimeField(null=True, blank=True)

class customuser(AbstractUser):
    FIO = models.TextField(max_length=120)
    email = models.TextField(max_length=60)
    number = models.IntegerField(null = True)

    CHOICE_GROUP = {
        (FIO, 'c'),
        (email, 'u@'),
        (number, '89')
    }
