from django.db import models
from mptt.models import MPTTModel
from ckeditor.fields import RichTextField

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
    image = models.ImageField(upload_to="image/") 
    melting = models.BooleanField(default=False)
    prise = models.FloatField()

    def __str__(self):
        return self.name
    
class SliderProduct(models.Model):
    menuObject = models.ForeignKey(Menu, on_delete=models.CASCADE)

# кылышкерек
from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    servers = models.CharField(max_length=100)
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    ingredients = models.TextField()
    directions = models.TextField()
    image = models.ImageField(upload_to='recipes/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def total_time(self):
        return self.prep_time + self.cook_time

    @property
    def formatted_prep_time(self):
        hours = self.prep_time // 60
        minutes = self.prep_time % 60
        return f"{hours}h {minutes}m"

    @property
    def formatted_cook_time(self):
        hours = self.cook_time // 60
        minutes = self.cook_time % 60
        return f"{hours}h {minutes}m"

    @property
    def formatted_total_time(self):
        hours = self.total_time // 60
        minutes = self.total_time % 60
        return f"{hours}h {minutes}m"

    

class Discount(models.Model):
    productObject = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale = models.CharField(max_length=25)
   


class Cheks(models.Model):
    humanIp = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True, blank=True)
    nomer = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    isPay = models.BooleanField(default=False, null=True, blank=True)

class CheksDetail(models.Model):
    productObject = models.ForeignKey(Product, on_delete = models.CASCADE, null=True, blank=True)
    totalSum = models.FloatField(null=True, blank=True)
    productCount = models.FloatField(default=1.0, null=True, blank=True)
    cheksObject = models.ForeignKey(Cheks, on_delete=models.CASCADE, null=True, blank=True)


#кылышкерек
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm

def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form, 'post': post})



class Stol(models.Model):
    nomer = models.CharField(max_length=20)

class Bron(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    haumany = models.CharField(max_length=15)
    dait = models.CharField(max_length=33)
    stolObject = models.ForeignKey(Stol, on_delete=models.CASCADE, blank=True, null=True)

