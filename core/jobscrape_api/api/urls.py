from django.urls import path
from jobscrape_api.api import views

urlpatterns = [
    # format -> /api/jobs/search/skills/?q=
    #path('search/languages/', views.JobLanguageList.as_view(), name='search_job_language_list'),
    #path('search/frameworks/', views.JobFrameworkList.as_view(), name='search_job_framework_list'),
    #path('search/databases/', views.JobDatabaseList.as_view(), name='search_job_database_list'),
    path('search/skills/', views.JobSkillList.as_view(), name='search_job_skill_list'),
    path('search/scrape-jobs/', views.ScrapeJobsList.as_view(), name='search_scrape_jobs_list'),

    path('scrape-results/', views.ScrapeResultListView.as_view(), name='scrape_results_list'),
    path('scrape-result/<str:job_name>/', views.ScrapeResultRetrieveView.as_view(), name='scrape-result-detail'),
]
