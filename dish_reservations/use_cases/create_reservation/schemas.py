from ninja import Schema


class NewReservation(Schema):
    """Newly created Reservation"""
    id: int


class ReservationParams(Schema):
    """POST schema for reservation creation"""
    customer_id: int
    dish_id: int

