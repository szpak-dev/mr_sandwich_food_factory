from pydantic import BaseModel

from app.schema import Error


class RemoveReservationParams(BaseModel):
    """Path parameters for removing given Reservation"""
    reservation_id: int


class ReservationNotFoundResponse(Error):
    """Reservation not found"""
