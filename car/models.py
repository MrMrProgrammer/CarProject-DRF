from django.db import models


# Create your models here.

class Car(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.BigIntegerField()

    class Meta:
        db_table = "Car"