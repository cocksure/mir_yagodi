from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Berries(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, default=None)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='berries_photos')

    def __str__(self):
        return self.name


class Units(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Orders(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    berry = models.ForeignKey(Berries, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    address = models.CharField(max_length=250)
    comment = models.TextField(max_length=5000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.berry)
