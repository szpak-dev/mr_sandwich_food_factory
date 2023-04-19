from dish_reservations.services import Reservations


def remove_reservation_action(reservation_id: int):
    Reservations.get_reservation(reservation_id)
    Reservations.remove_reservation(reservation_id)
