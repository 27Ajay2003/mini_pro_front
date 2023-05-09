from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):

    def handle(self, *args, **options):
        # Call the management commands you want to run
        call_command('makemigrations')
        call_command('migrate')
        call_command('initquizquestions')
        call_command('initskills')
        call_command('initscrapejobs')
        call_command('temp_init_thejsonresp')

        self.stdout.write(self.style.SUCCESS('All management commands completed.'))