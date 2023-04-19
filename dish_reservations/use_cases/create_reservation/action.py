from datetime import timedelta
from django.utils import timezone

from dish_reservations.models import DishReservation
from .schemas import ReservationParams
from dish_reservations.services import DailyAvailabilities, Reservations
from dishes.services import Dishes
from dish_reservations.errors import DailyAvailabilityNotCreatedYet


def create_reservation_action(new_reservation: ReservationParams) -> DishReservation:
    tomorrow = timezone.now() + timedelta(days=1)
    customer_id, dish_id = new_reservation.customer_id, new_reservation.dish_id

    dish = Dishes.get_dish(dish_id)

    try:
        DailyAvailabilities.assert_daily_availability_exists(dish_id, tomorrow)
        daily_availability = DailyAvailabilities.get_daily_availability(dish_id, tomorrow)
    except DailyAvailabilityNotCreatedYet:
        DailyAvailabilities.create_daily_availability(dish_id, dish.daily_limit, tomorrow)
        daily_availability = DailyAvailabilities.get_daily_availability(dish_id, tomorrow)

    return Reservations.reserve_dish(daily_availability, customer_id)
