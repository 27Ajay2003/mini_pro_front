import csv
from django.core.management.base import BaseCommand
from technicalquestions_api.models import QuizQuestion

class Command(BaseCommand):
    help = 'Loads technical quiz data from CSV file into database'

    def handle(self, *args, **kwargs):
        if QuizQuestion.objects.count() == 0:
            with open('./media/csv/final_technical_q_dataset_finalized.csv') as csvfile:
                reader = csv.DictReader(csvfile)

                # Loop through the rows and create new QuizQuestion objects
                for row in reader:
                    quiz_question = QuizQuestion(
                        topic=row['Topic'],
                        question=row['Question'],
                        option_a=row['a'],
                        option_b=row['b'],
                        option_c=row['c'],
                        option_d=row['d'],
                        correct_answer=row['Correct Answer'],
                        difficulty=row['Difficulty'],
                        cognitive_level=row['Cognitive Level'],
                        subject=row['Subject']
                    )

                    # Save the object to the database
                    quiz_question.save()

            self.stdout.write(self.style.SUCCESS('Quiz data loaded successfully'))
        else:
            self.stdout.write(self.style.WARNING('Quiz data already exists, skipping data load'))