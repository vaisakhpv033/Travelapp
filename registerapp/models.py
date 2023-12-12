from django.db import models


# Create your models here.
class guides(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics')
    designation = models.TextField()

    def __str__(self):
        return self.name


class reviews(models.Model):
    client = models.CharField(max_length=250)
    profession = models.CharField(max_length=250)
    comments = models.TextField()
    image = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.client