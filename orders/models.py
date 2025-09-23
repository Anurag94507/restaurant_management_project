from django.db import models

# Create your models here.
from whatever_app.models import OrderStatus

class Order(models.Model):

    status = models.ForeignKey(
        OrderStatus,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )

    def __str__(self):
        status_name = self.status.name if self.status else "No Status"
        return f"Order #{self.id} - Status: {self.status}"