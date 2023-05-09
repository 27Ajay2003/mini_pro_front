import json
from datetime import datetime
from django.core.management.base import BaseCommand
from jobscrape_api.models import ScrapeResult, ScrapeJob

class Command(BaseCommand):
    help = 'temporarily initializes the ScrapeResult object'

    def handle(self, *args, **kwargs):
        try:
            ScrapeResult.objects.all().delete()

            with open('./media/temp_json_response.json') as f:
                data = json.load(f)

            for job_name in data.keys():
                scrape_job = ScrapeJob.objects.get(job_name=job_name)
                json_resp = {job_name: data[job_name]}
                scrape_result = ScrapeResult(job_name=scrape_job, json_resp=json_resp, date_created=datetime.now())
                scrape_result.save()

            self.stdout.write(self.style.SUCCESS('TEMP ScrapeResult loaded successfully'))
        except:
            self.stdout.write(self.style.ERROR('TEMP ScrapeResult loading FAILED!'))


        # if ScrapeResult.objects.count() == 0:
        #     with open('./media/temp_json_response.json') as f:
        #         data = json.load(f)

        #     for job_name in data.keys():
        #         scrape_job = ScrapeJob.objects.get(job_name=job_name)
        #         json_resp = {job_name: data[job_name]}
        #         scrape_result = ScrapeResult(job_name=scrape_job, json_resp=json_resp, date_created=datetime.now())
        #         scrape_result.save()

        #     self.stdout.write(self.style.SUCCESS('TEMP ScrapeResult loaded successfully'))
        # else:
        #     self.stdout.write(self.style.WARNING('TEMP ScrapeResult already exists, skipping data load'))

    