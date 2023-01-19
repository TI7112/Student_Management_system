from django.db import models

# Create your models here.

CITY_OPTION = (
    ("PURNEA","PURNEA"),
    ("PATNA","PATNA"),
    ("BHOPAL","BHOPAL"),
    ("Ranchi","Ranchi"),
)

class Students(models.Model):
    name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    city = models.CharField(max_length=200, choices= CITY_OPTION)

    def __str__(self):
        return self.name