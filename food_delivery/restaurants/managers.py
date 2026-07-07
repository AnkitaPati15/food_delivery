from django.db import models


class RestaurantQuerySet(models.QuerySet):

    def active(self):
     return self.filter(
        is_active=True,
        is_deleted=False
    )

    def free_delivery(self):
        return self.filter(delivery_fee=0)

    def fast_delivery(self):
        return self.filter(delivery_time__lte=30)

    def minimum_order(self, amount):
        return self.filter(minimum_order__lte=amount)


class RestaurantManager(models.Manager):

    def get_queryset(self):
        return RestaurantQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def free_delivery(self):
        return self.get_queryset().free_delivery()

    def fast_delivery(self):
        return self.get_queryset().fast_delivery()

    def minimum_order(self, amount):
        return self.get_queryset().minimum_order(amount)