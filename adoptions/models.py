from django.db import models

class Pet(models.Model):
    SEX_CHOICES = [('M','Male'),('F','Female')]
    name = models.CharField(max_length=20)
    description = models.TextField(default="NO Decription Provided")
    submitter = models.CharField(max_length=20)
    species = models.CharField(max_length=20)
    breed = models.CharField(max_length=20)
    sex = models.CharField(choices=SEX_CHOICES,max_length=1)
    age = models.IntegerField(max_length=3)
    vaccinations = models.ManyToManyField('Vaccine')

    def __str__(self):
        return self.name

class Vaccine(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

