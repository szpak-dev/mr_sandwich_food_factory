from app.errors import FoodFactoryError


class ReservationError(FoodFactoryError):
    ...


class ReservationNotFound(ReservationError):
    ...


class DishBecameUnavailable(ReservationError):
    ...


class DailyAvailabilityNotCreatedYet(ReservationError):
    ...


class RevisionIsOutdated(ReservationError):
    ...
