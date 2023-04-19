from django.db import models
from django.utils import timezone

from dishes.models import Dish


class DishReservation(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=64)
    ttl_minutes = models.IntegerField(default=15)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'dish_reservations'


class DishDailyAvailability(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    day = models.DateField(default=timezone.now)
    available_count = models.IntegerField()
    revision = models.IntegerField(default=1)

    class Meta:
        db_table = 'dish_daily_availabilities'
