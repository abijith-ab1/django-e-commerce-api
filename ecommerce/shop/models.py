from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SearchHistory(models.Model):
    user = models.ForeignKey(User, related_name='search_history', on_delete=models.CASCADE)
    search_term = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
