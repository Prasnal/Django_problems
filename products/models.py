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

    class Meta:
        verbose_name_plural = "Country"

    def __str__(self):
        return self.name


class Company(models.Model):
    name=models.CharField(max_length=255)
    country_id=models.ForeignKey(Country,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Company"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    company_id=models.ForeignKey(Company,on_delete=models.CASCADE)
    details=models.TextField()

    class Meta:
        verbose_name_plural = "Product"

    def __str__(self):
        return self.name


class Country_Products(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        verbose_name_plural = "Stock and prices"


