from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(editable=False, null=True)
    updated = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        ''' On save update timestamps '''
        if not self.id:
            self.create = timezone.now()
        self.modified = timezone.now()
        return super(Product, self).save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=200)
    
