from django.db import models
from authentication.models import User



class QuizQuestion(models.Model):
    question_id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=5000)
    question = models.TextField(max_length=5000)
    option_a = models.CharField(max_length=5000)
    option_b = models.CharField(max_length=5000)
    option_c = models.CharField(max_length=5000)
    option_d = models.CharField(max_length=5000)
    correct_answer = models.CharField(max_length=5000)
    difficulty = models.CharField(max_length=5000)
    cognitive_level = models.CharField(max_length=5000)
    subject = models.CharField(max_length=5000)    

    def __str__(self):
        return self.question 


class ResultTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="results")
    test_date = models.DateTimeField(auto_now_add=True)
    results = models.JSONField()

    def __str__(self):
        return f'{self.user} {self.test_date}'