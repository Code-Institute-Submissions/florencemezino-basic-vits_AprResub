from django.db import models
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField 


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class HealthGoal(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Package(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    sku = models.CharField("SKU", max_length=255, blank=True, null=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    healthgoal = models.ForeignKey('HealthGoal', null=True, blank=True, on_delete=models.SET_NULL)    
    package = models.ForeignKey('Package', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description_benefits = models.CharField(max_length=800)
    style = RichTextField(null=True, blank=True) 
    quantity = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    healthgoal = TaggableManager()

    def __str__(self):
        return self.name
