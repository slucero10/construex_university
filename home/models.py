from django.db import models

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.full_name