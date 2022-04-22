from django.core.management.base import BaseCommand, CommandError
from permissions.init.instalization import permission_instalization


class Command(BaseCommand):
    help = 'Permission configurator'

    def handle(self, *args, **options):
        permission_instalization()
        print('permissions configured...')
