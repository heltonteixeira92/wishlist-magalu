from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    """
    The product table containing all products.
    # price: preço do produto
    # image: URL da imagem do produto
    # brand: marca do produto
    # id: id do produto
    # title: nome do produto
    # reviewScore: média dos reviews para este produto
    """
    title = models.CharField(verbose_name=_("title"), max_length=128)
    brand = models.CharField(verbose_name=_("brand"), max_length=128)
    price = models.DecimalField(verbose_name=_("price"), max_digits=5, decimal_places=2)
    image = models.ImageField(verbose_name=_("image"),
                              upload_to="images/",
                              blank=True, null=True)
    reviewScore = models.FloatField(verbose_name=_("review score"), blank=True, null=True)

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def __str__(self):
        return self.title
