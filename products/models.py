from django.db import models

# Create your models here.
from base.models import BaseModel


class Categories(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,null=True,blank=True)
    category_img = models.ImageField(upload_to="categories")


class Products(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,null=True,blank=True)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE,related_name="products")
    price = models.IntegerField()
    description = models.TextField()


class ProductImage(BaseModel):
    product = models.ForeignKey(Products,on_delete=models.CASCADE,related_name="product_images")
    image = models.ImageField(upload_to="products")