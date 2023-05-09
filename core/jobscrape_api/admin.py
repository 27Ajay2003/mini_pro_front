from django.contrib import admin
# from jobscrape_api.models import JobLanguage, JobFramework, JobDatabase, JobSkill, ScrapeJob, ScrapeResult
from jobscrape_api.models import JobSkill, ScrapeJob, ScrapeResult

#admin.site.register(JobLanguage)
#admin.site.register(JobFramework)
#admin.site.register(JobDatabase)
admin.site.register(JobSkill)
admin.site.register(ScrapeJob)
admin.site.register(ScrapeResult)