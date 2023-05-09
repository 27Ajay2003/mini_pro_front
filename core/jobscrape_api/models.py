from django.db import models


# class JobLanguage(models.Model):
#     language = models.CharField(max_length=500)

#     def __str__(self):
#         return f'{self.language}'

# class JobFramework(models.Model):
#     framework = models.CharField(max_length=500)

#     def __str__(self):
#         return f'{self.framework}'

# class JobDatabase(models.Model):
#     database = models.CharField(max_length=500)

#     def __str__(self):
#         return f'{self.database}'

class JobSkill(models.Model):
    skill = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.skill}'
    

    
class ScrapeJob(models.Model):
    job_name = models.CharField(max_length=500, primary_key=True)

    def __str__(self):
        return f'{self.job_name}'

class ScrapeResult(models.Model):
    job_name = models.ForeignKey(ScrapeJob, on_delete=models.CASCADE, related_name="responses")
    json_resp = models.JSONField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.job_name} {self.date_created}'