import csv
from django.core.management.base import BaseCommand
from jobscrape_api.models import JobSkill

class Command(BaseCommand):
    help = 'Loads job skills data from CSV file into database'

    def handle(self, *args, **kwargs):
        # if JobLanguage.objects.count() == 0:
        #     with open('./media/csv/languages.csv') as csvfile:
        #         reader = csv.DictReader(csvfile)

        #         for row in reader:
        #             language = JobLanguage(
        #                 language=row['languages']
        #             )

        #             # Save the object to the database
        #             language.save()

        #     self.stdout.write(self.style.SUCCESS('JobLanguages loaded successfully'))
        # else:
        #     self.stdout.write(self.style.WARNING('JobLanguages already exists, skipping data load'))


        # if JobFramework.objects.count() == 0:
        #     with open('./media/csv/frameworks.csv') as csvfile:
        #         reader = csv.DictReader(csvfile)

        #         for row in reader:
        #             framework = JobFramework(
        #                 framework=row['frameworks']
        #             )

        #             framework.save()

        #     self.stdout.write(self.style.SUCCESS('JobFrameworks loaded successfully'))
        # else:
        #     self.stdout.write(self.style.WARNING('JobFrameworks already exists, skipping data load'))

        
        # if JobDatabase.objects.count() == 0:
        #     with open('./media/csv/databases.csv') as csvfile:
        #         reader = csv.DictReader(csvfile)

        #         for row in reader:
        #             database = JobDatabase(
        #                 database=row['databases']
        #             )

        #             database.save()

        #     self.stdout.write(self.style.SUCCESS('JobDatabases loaded successfully'))
        # else:
        #     self.stdout.write(self.style.WARNING('JobDatabases already exists, skipping data load'))

        
        if JobSkill.objects.count() == 0:
            with open('./media/csv/skills.csv') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    skill = JobSkill(
                        skill=row['skills']
                    )

                    skill.save()

            self.stdout.write(self.style.SUCCESS('JobSkills loaded successfully'))
        else:
            self.stdout.write(self.style.WARNING('JobSkills already exists, skipping data load'))

    