import csv
from django.core.management.base import BaseCommand
from jobscrape_api.models import ScrapeJob

class Command(BaseCommand):
    help = 'Loads job names data from CSV file into database'

    def handle(self, *args, **kwargs):
        if ScrapeJob.objects.count() == 0:
            with open('./media/csv/scrapejobslist.csv') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    job = ScrapeJob(
                        job_name=row['job_names']
                    )

                    job.save()

            self.stdout.write(self.style.SUCCESS('ScrapeJob loaded successfully'))
        else:
            self.stdout.write(self.style.WARNING('ScrapeJob already exists, skipping data load'))

    