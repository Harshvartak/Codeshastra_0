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
