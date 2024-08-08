from django.db import models

# Create your models here.

class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    is_reserved = models.BooleanField(default=False)

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    images = models.FileField(upload_to="images/",max_length=250,null=True, default=None)


    def __str__(self):
        return self.name

class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

   

