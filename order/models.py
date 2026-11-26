from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Status(models.TextChoices):
    PENDING = 'PND', _('Pending')
    SUCCEED = 'SCD', _('Succeed')
    CANCELLED = 'CLD', _('Cancelled')
    FAILED = 'FLD', _('Failed')


class Order(BaseModel):

    class Status(models.TextChoices):
        PENDING = 'PND', _('Pending')
        SUCCEED = 'SCD', _('Succeed')
        CANCELLED = 'CLD', _('Cancelled')
        FAILED = 'FLD', _('Failed')

    user = models.ForeignKey(to='users.User', on_delete=models.PROTECT)
    total_price = models.DecimalField(decimal_places=5, max_digits=10)
    status = models.CharField(max_length=3, choices=Status, default=Status.PENDING)


class OrderItem(BaseModel):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    unit_price = models.DecimalField(decimal_places=5, max_digits=10)

    def get_order_price(self):
        return self.unit_price * self.quantity

    def save(
        self,
        *,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        self.unit_price = self.product.price
        super().save()

class Payment(BaseModel):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=5, max_digits=10)
