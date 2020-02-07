from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    in_stock = models.PositiveIntegerField(verbose_name='Product in stock')
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    ordered_quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=7, decimal_places=2)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)

    def __str__(self):
        return self.client, self.product, self.total_price
