from django.db import models
from django.core.validators import RegexValidator


class Event(models.Model):
    title = models.CharField(blank=False, null=False, max_length=150)
    text = models.TextField(blank=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    mail = models.EmailField(max_length=240)
    tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message=(
        "Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."))
    tel_number = models.CharField(
        validators=[tel_number_regex], max_length=15, verbose_name='電話番号')
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
