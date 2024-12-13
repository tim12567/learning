from django.db import models # type: ignore


class Color(models.Model):
   name = models.CharField(max_length=32)

   def __repr__(self):
      return f"Color: {self.name}"

class Item(models.Model):
   name  = models.CharField(max_length=100)
   brand = models.CharField(max_length=100)
   count = models.PositiveIntegerField()
   properties = models.CharField(max_length=100, default=str)
   colors = models.ManyToManyField(to=Color)

   def __repr__(self):
      return f"Item: {self.name}"