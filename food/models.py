from django.db import models
# Create your models here.
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

