from ninja import Router
from ninja.responses import codes_4xx

from app.schema import Error
from dish_reservations.errors import DishBecameUnavailable, RevisionIsOutdated, ReservationNotFound
from dish_reservations.use_cases.create_reservation.action import create_reservation_action
from dish_reservations.use_cases.create_reservation.schemas import NewReservation, ReservationParams
from dish_reservations.use_cases.get_reservation.action import get_reservation_action
from dish_reservations.use_cases.get_reservation.schemas import Reservation
from dish_reservations.use_cases.remove_reservation.action import remove_reservation_action
from dishes.errors import DishNotFound


dish_reservations_router = Router()


@dish_reservations_router.post('/', response={
    201: NewReservation,
    codes_4xx: Error,
})
def create_reservation(request, data: ReservationParams):
    try:
        return create_reservation_action(data)
    except DishNotFound:
        return 404, {'message': 'Dish not found'}
    except DishBecameUnavailable:
        return 422, {'message': 'Dish became unavailable'}
    except RevisionIsOutdated:
        return 409, {'message': 'Revision is outdated'}


@dish_reservations_router.get('{int:reservation_id}/customers/{int:customer_id}', response={
    200: Reservation,
    codes_4xx: Error,
})
def get_reservation(request, reservation_id: int, customer_id: int):
    try:
        return get_reservation_action(reservation_id, customer_id)
    except ReservationNotFound:
        return 404, {'message': 'Reservation not found'}


@dish_reservations_router.delete('/{int:reservation_id}', response={
    204: None,
    codes_4xx: Error,
})
def remove_reservation(request, reservation_id: int):
    try:
        remove_reservation_action(reservation_id)
        return 204, None
    except ReservationNotFound:
        return 404, {'message': 'Reservation not found'}
