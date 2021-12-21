from django.db import models


# Create your models here.
class Book(models.Model):
    BOOKS = (
        ('HB', 'Hobbit'),
        ('LOTR', 'Lord of the rings')
    )
    title = models.CharField(blank=True)
