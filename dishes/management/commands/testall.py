from django.core.management.base import BaseCommand, CommandError
from dishes.producers import publish_dish_created, publish_dish_updated


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        print('producing...')
        for i in range(2, 7):
            publish_dish_updated(i)
        quit(0)
