# Food Factory
Food Factory is a microservice responsible for managing Dishes production and handles Reservations done via Web Store.
It uses Django because of its Admin Panel, which gives CRUD capabilities for free. It doesn't use any specific
architectural style, because Django's applications already provide high cohesion and low coupling.

## Hosts
| Hostname            | Development    | Compose/Swarm               |
|---------------------|----------------|-----------------------------|
| **food_factory**        | 127.0.0.1:8001 | mr.localhost/food_factory/* |
| **food_factory_worker** | manually       | -                           |
| **food_factory_db**     | localhost:5434 | food_factory_db:5432        |
