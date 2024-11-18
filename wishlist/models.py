from django.db import models
from django.utils.translation import gettext_lazy as _

from customers.models import Customer
from products.models import Product


class WishList(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["customer", "product"], name='name of constraint'),
        ]
        verbose_name = _("wish list")
        verbose_name_plural = _("wish lists")
