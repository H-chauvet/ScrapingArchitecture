from django.db import models

# Create your models here.


class Article(models.Model):

    Field1 = models.CharField(max_length=100)
    Field2 = models.CharField(max_length=100)
    Field3 = models.CharField(max_length=100)
    Field4 = models.CharField(max_length=100)
    Field5 = models.CharField(max_length=100)
    Field6 = models.CharField(max_length=100)
    Field7 = models.CharField(max_length=250)

    def __str__(self):
        return self.Field1 + " " + self.Field2