from django.db import models
from datetime import datetime


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, null=True, blank=True)
    price = models.FloatField()
    count = models.IntegerField()
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " " + str(self.price)

    class Meta:
        ordering = ['-created_at']


class MyProduct(Product):
    class Meta:
        proxy = True
        ordering = ['-updated_at']

class Category(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name
