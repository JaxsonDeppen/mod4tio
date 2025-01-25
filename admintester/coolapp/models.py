from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=50)
    dummy_field = models.TextField(max_length=20)
    def __str__(self):
        return f"{self.category}"
class Tag(models.Model):
    barcode_num = models.IntegerField()
    test_field = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.barcode_num}"
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(decimal_places=3,max_digits=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,db_index=True)
    tag = models.ManyToManyField(Tag, editable=True)

