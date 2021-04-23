from django.db import models
from django.contrib.auth.models import User

#Create your models here
class Tag(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    name       = models.CharField(max_length= 255)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    class Meta:
        verbose_name_plural = 'Books'
    title    = models.CharField(max_length= 255)
    category = models.ManyToManyField(Category)
    author   = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class ISBN (models.Model):
    class Meta:
        verbose_name_plural = 'ISBN'
    isbn     = models.AutoField(verbose_name='ID', 
                                serialize=False, 
                                auto_created=True, 
                                primary_key=True)
    book     = models.OneToOneField(Book, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.isbn} isbn"