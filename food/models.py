from django.db import models
# Create your models here.

class Setting(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=155)
    number_one = models.CharField(max_length=100)
    number_two = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    menuObject = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    prise = models.CharField(max_length=55)
    image = models.ImageField(upload_to="image/") 

    def __str__(self):
        return self.name
    

class Discount(models.Model):
    productObject = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale = models.CharField(max_length=25)
   

class Coment(models.Model):
    name = models.CharField(max_length=100)