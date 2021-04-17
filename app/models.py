from django.db import models

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    acc_type = models.CharField(max_length=10)
    balance = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id) + self.name

class Transaction(models.Model):
    to = models.CharField(max_length=30)
    From = models.CharField(max_length=30)
    amount = models.PositiveIntegerField()
    status = models.CharField(max_length=20)
    t_id = models.PositiveIntegerField()
    time = models.DateTimeField()

    

