from django.db import models

class Country(models.Model):

    CONTINENTS=(
        ('Asia','Asia'),
        ('Africa','Africa'),
        ('North_America','North America'),
        ('South_America','South America'),
        ('Antarctica','Antarctica'),
        ('Europe','Europe'),
        ('Australia','Australia'),
    )

    name = models.CharField(max_length=255)
    continent = models.CharField(max_length=20,choices=CONTINENTS)

    def __str__(self):
        return self.name


class Company(models.Model):
    name=models.CharField(max_length=255)
    country_id=models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    company_id=models.ForeignKey(Company,on_delete=models.CASCADE)
    details=models.TextField()

    def __str__(self):
        return self.name


class Country_Products(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name

