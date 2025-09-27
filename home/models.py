from django.db import models

class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.Foreignkey(MenuCategory, on_delete=models.SET_NULL, null=True, related_name='items')

    def __str__(self):
        return f"{self.name} ({self.category})"