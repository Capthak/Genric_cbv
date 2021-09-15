from django.db import models

# Create your models here.

class Laptop(models.Model):
    company=models.CharField(max_length=50)
    model=models.CharField(max_length=50)
    ram=models.IntegerField()
    rom=models.FloatField()
    processor=models.CharField(max_length=20)
    price=models.FloatField()

    def __str__(self) -> str:
        return self.model
