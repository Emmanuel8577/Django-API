from django.db import models

# Create your models here.

class Book(models.Model):

    name = models.CharField(max_length = 150, null = False, blank = False)
    Author = models.CharField(max_length = 50, null = False, blank = False)
    price = models.DecimalField(max_digits = 6, decimal_places=4, null = False, blank= False)
    category = models.CharField(max_length= 100, null = False, blank= False)
    description = models.TextField()
    star = models.IntegerField()


    def __str__(self):
        return self.name + " - " + self.Author
    

    