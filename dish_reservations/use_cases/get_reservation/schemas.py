from ninja import Schema


class GetReservationParams(Schema):
    """Request path parameters"""
    customer_id: int


class Reservation(Schema):
    """Current Reservation of the Customer"""
    id: int

