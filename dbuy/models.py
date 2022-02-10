from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=1000)
    category = models.CharField(max_length=1000)
    image = models.TextField()
    description = models.TextField()
    location = models.CharField(max_length=1000)
    condition = models.CharField(max_length=1000)
    brand = models.CharField(max_length=1000)
    color = models.CharField(max_length=1000)
    price = models.CharField(max_length=1000)
    user_id = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class Comment(models.Model):
    username = models.CharField(max_length=1000)
    content = models.TextField()
    user_id = models.CharField(max_length=100)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="products")
