from django.db import models

class Person(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    image=models.ImageField(upload_to='images/needy')
    needs=models.TextField()
    location=models.CharField(max_length=200)

    def summary(self):
        return self.needs[:100]

    def __str__(self):
        return self.name

class ngo(models.Model):
    name = models.CharField(max_length = 100)
    ng_id = models.IntegerField(primary_key = True)
    location = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'images/')
    description = models.CharField(max_length=500, default = 'no description provided')
    donations = models.IntegerField(default = 0)
    email=models.CharField(max_length = 50)
    phone = models.BigIntegerField()
    website = models.CharField(max_length = 250)
    stats  = models.ImageField(upload_to = 'images/ngo')

    def __str__(self):
        return self.name
