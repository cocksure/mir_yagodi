from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=50)


class Berries(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='berries_photos')


class Units(models.Model):
    name = models.CharField(max_length=50)


class Orders(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    berry = models.ForeignKey(Berries, on_delete=models.CASCADE)
