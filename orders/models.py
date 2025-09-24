from django.db import models

# Create your models here.
from whatever_app.models import OrderStatus

class Order(models.Model):
    name = models.Charfield(max_length=50, unique=True)

    class Meta:
        verbose_name = "Order Status"
        verbose_name_plural = "Order Statuses"
    
    def __str__(self):
        return self.name

class order(models.Model):
    cutomer = models.ForeignKey(
        'account.Customer',
        on_delete=models.CASCADE,
        related_name='orders'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


    status = models.ForeignKey(
        OrderStatus,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )

    def __str__(self):
        status_name = self.status.name if self.status else "No Status"
        return f"Order #{self.id} - Status: {status_name} - Customer: {self.customer} - Created: {self.created_at.strftime('%Y-%m-%d %H:%M')}"
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Order"
        verbose_name_plural = "Orders"