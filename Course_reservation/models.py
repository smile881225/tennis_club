from django.db import models

# Create your models here.

from django.db import models

class Course_reservation(models.Model):
    Period = models.CharField(max_length=255)
    
    Course_name = models.CharField(max_length=255)