from django.db import models
# Create your models here.



class Setting(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=155)
    number_one = models.CharField(max_length=100)
    number_two = models.CharField(max_length=100)
    email = models.EmailField()
    facebook = models.URLField(null=True,blank=True)
    instagram = models.URLField(null=True,blank=True)
    schedule = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    menuObject = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    prise = models.CharField(max_length=55)
    image = models.ImageField(upload_to="image/") 
    melting = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class SliderProduct(models.Model):
    menuObject = models.ForeignKey(Menu, on_delete=models.CASCADE)


class Aboutfoot(models.Model):
    ProductObject = models.ForeignKey(Product,on_delete=models.CASCADE)
    sostav = models.CharField(max_length=255)
    gram = models.CharField(max_length=255)

    

class Discount(models.Model):
    productObject = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale = models.CharField(max_length=25)
   

class Coment(models.Model):
    name = models.CharField(max_length=100)