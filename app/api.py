from ninja import NinjaAPI
from django.urls import path
from django.contrib import admin

from dish_reservations.api import dish_reservations_router
from dishes.api import dishes_router


api = NinjaAPI()
api.add_router('/dish_reservations', dish_reservations_router)
api.add_router('/dishes', dishes_router)


urlpatterns = [
    path('food_factory/admin/', admin.site.urls),
    path('food_factory/', api.urls),
]
