from django.db import models
from django.db.models.aggregates import Max

# Create your models here.
class Contact(models.Model):
    name =models.CharField(max_length=122,blank=True)
    email=models.CharField(max_length=122)
    subject=models.TextField()
    message=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
    