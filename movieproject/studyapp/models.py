from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='inmakes_project')
    desc = models.TextField()
    year = models.IntegerField()

    def __str__(self):
        return self.name

# class person(models.Model):
#     name1 = models.CharField(max_length=250)
#     img1 = models.ImageField(upload_to='inmakes_project1')
#     desc1 = models.TextField()
#
#     def __str__(self):
#         return self.name1
