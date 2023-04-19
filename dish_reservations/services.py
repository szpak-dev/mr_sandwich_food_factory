from dish_reservations.models import DishReservation, DishDailyAvailability
from dish_reservations.errors import DailyAvailabilityNotCreatedYet, RevisionIsOutdated, DishBecameUnavailable, \
    ReservationNotFound
from django.db import transaction
from django.db.models import F
from django.core.exceptions import ObjectDoesNotExist


class Reservations:
    @staticmethod
    def get_reservation(reservation_id: int):
        try:
            return DishReservation.objects.get(pk=reservation_id)
        except ObjectDoesNotExist:
            raise ReservationNotFound('Reservation not found')

    @staticmethod
    def get_customer_reservation(reservation_id: int, customer_id: int):
        try:
            return DishReservation.objects.get(pk=reservation_id, customer_id=customer_id)
        except ObjectDoesNotExist:
            raise ReservationNotFound('Reservation not found')

    @staticmethod
    def remove_reservation(reservation_id: int):
        DishReservation.objects.filter(pk=reservation_id).delete()

    @staticmethod
    def reserve_dish(dish_daily_availability: DishDailyAvailability, customer_id: int) -> DishReservation:
        pk = dish_daily_availability.pk
        dish_id = dish_daily_availability.dish.id
        day = dish_daily_availability.day
        revision = dish_daily_availability.revision

        with transaction.atomic():
            updated = DishDailyAvailability\
                .objects\
                .filter(pk=pk, day=day, available_count__gt=0, revision=revision)\
                .update(available_count=F('available_count') - 1)

            if updated == 1:
                dish_reservation = DishReservation(dish_id=dish_id, customer_id=customer_id)
                dish_reservation.save()
                return dish_reservation

            raise RevisionIsOutdated('Available Dishes count has changed')


class DailyAvailabilities:
    @staticmethod
    def assert_daily_availability_exists(dish_id: int, day) -> None:
        if DishDailyAvailability.objects.filter(dish_id=dish_id, day=day).count() == 0:
            raise DailyAvailabilityNotCreatedYet('Daily Availability not created for the given day yet')

    @staticmethod
    def create_daily_availability(dish_id: int, daily_limit: int, day) -> None:
        daily_availability = DishDailyAvailability(dish_id=dish_id, available_count=daily_limit, day=day)
        daily_availability.save()

    @staticmethod
    def get_daily_availability(dish_id: int, day) -> DishDailyAvailability:
        try:
            return DishDailyAvailability.objects.get(dish_id=dish_id, day=day, available_count__gt=0)
        except ObjectDoesNotExist:
            raise DishBecameUnavailable('Daily Availability with available dishes was not found')
