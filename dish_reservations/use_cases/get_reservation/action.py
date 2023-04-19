from dish_reservations.services import Reservations


def get_reservation_action(reservation_id: int, customer_id: int):
    return Reservations.get_customer_reservation(reservation_id, customer_id)
