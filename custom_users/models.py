from django.db import models
from django.contrib.auth.models import User

MALE = 1
FEMALE = 2

GENDER_TYPE = (
    (MALE, "Муж"),
    (FEMALE, "Жен")
)

class CustomUser(User):
    phone_number = models.CharField(max_length=13, verbose_name='Введите номер телефона')
    date_birth = models.DateField(verbose_name='Дата рождения')
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='Выбирите пол')