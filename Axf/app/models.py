from django.db import models


# Create your models here.

class Base(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=8)

    class Meta:
        abstract = True


class Wheel(Base):
    class Meta:
        db_table = 'axf_wheel'
