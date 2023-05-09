import json
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404
from django.http import JsonResponse



#from jobscrape_api.models import JobLanguage, JobFramework, JobDatabase, JobSkill, ScrapeJob, ScrapeResult
#from jobscrape_api.api.serializers import JobLanguageSerializer, JobFrameworkSerializer, JobDatabaseSerializer, JobSkillSerializer, ScrapeJobsListSerializer, ScrapeResultSerializer
from jobscrape_api.models import JobSkill, ScrapeJob, ScrapeResult
from jobscrape_api.api.serializers import JobSkillSerializer, ScrapeJobsListSerializer, ScrapeResultSerializer
from authentication.models import User
from core.recommendjobs import recommend_jobs

# class JobLanguageList(generics.ListAPIView):
#     serializer_class = JobLanguageSerializer
#     permission_classes = [IsAuthenticated,IsAdminUser]

#     def get_queryset(self):
#         query = self.request.query_params.get('q')
#         if query:
#             return JobLanguage.objects.filter(language__icontains=query)
#         return JobLanguage.objects.all()

#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         data = [language['language'] for language in serializer.data]
#         return Response(data)


# class JobFrameworkList(generics.ListAPIView):
#     serializer_class = JobFrameworkSerializer
#     permission_classes = [IsAuthenticated,IsAdminUser]

#     def get_queryset(self):
#         query = self.request.query_params.get('q')
#         if query:
#             return JobFramework.objects.filter(framework__icontains=query)
#         return JobFramework.objects.all()

#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         data = [framework['framework'] for framework in serializer.data]
#         return Response(data)


# class JobDatabaseList(generics.ListAPIView):
#     serializer_class = JobDatabaseSerializer
#     permission_classes = [IsAuthenticated,IsAdminUser]

#     def get_queryset(self):
#         query = self.request.query_params.get('q')
#         if query:
#             return JobDatabase.objects.filter(database__icontains=query)
#         return JobDatabase.objects.all()
    
#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         data = [database['database'] for database in serializer.data]
#         return Response(data)


class JobSkillList(generics.ListAPIView):
    serializer_class = JobSkillSerializer
    permission_classes = [IsAuthenticated,IsAdminUser]

    def get_queryset(self):
        query = self.request.query_params.get('q')
        if query:
            return JobSkill.objects.filter(skill__icontains=query)
        return JobSkill.objects.all()
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = [skill['skill'] for skill in serializer.data]
        return Response(data)
    


class ScrapeJobsList(generics.ListAPIView):
    serializer_class = ScrapeJobsListSerializer
    permission_classes = [IsAuthenticated,IsAdminUser]

    def get_queryset(self):
        query = self.request.query_params.get('q')
        if query:
            return ScrapeJob.objects.filter(job_name__icontains=query)
        return ScrapeJob.objects.all()
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = [job_name['job_name'] for job_name in serializer.data]
        return Response(data)


# add more methods - nothing for now
class ScrapeResultListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated,IsAdminUser]
    serializer_class = ScrapeResultSerializer

    def get_queryset(self):
        return ScrapeResult.objects.all()


class ScrapeResultRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]       #####permission chnages from admin only to logged in user/admin
    #serializer_class = ScrapeResultSerializer

    # IMPLEMENT COSINE
    
    def get(self, request, *args, **kwargs):
        skills_arr=[]
        job_name = self.kwargs.get('job_name')
        obj = get_object_or_404(ScrapeResult, job_name__job_name=job_name)  
        #return obj
        json_res = obj.json_resp
        print(type(json_res[job_name]))
        # for i in json_res[job_name]:
        #     del i["job_description"]
        #print(json_res[job_name])    
        # for i in range(len(json_res[job_name])):
        #     jobs_array=[]
        #     #print(json_res[job_name][i]["company_skills"])
        #     for j in json_res[job_name][i]["company_skills"].values():
                
        #         for z in j:
        #             jobs_array.append(z)
        #     skills_arr.append(jobs_array)        
        for item in json_res[job_name]:
            try:
                company_skill = []
                company_skill.extend(item['company_skills']['languages'])
                company_skill.extend(item['company_skills']['frameworks'])
                company_skill.extend(item['company_skills']['databases'])
                company_skill.extend(item['company_skills']['skills'])
                item['company_skills'] = company_skill
            except TypeError:
                pass
            # del item['company_skills']['languages']
            # del item['company_skills']['frameworks']
            # del item['company_skills']['databases']
            # del item['company_skills']['skills']    
        # print(json_res[job_name][0].keys())  
        job_opportunities=json_res[job_name]
        user = self.request.user
        print("Authenticated user details:", user.username, user.email)
        # print(type(user.languages))
        #candidate_skills=user.languages+","+user.frameworks+","+user.databases+","+user.skills
        candidate_skills=user.skills
        cleaned_skills = candidate_skills.strip(",")
        candidate_skills_list = cleaned_skills.split(',')
        print(candidate_skills_list)
        #print(json_res[job_name][6]["company_skills"])  
        #print(json_res[job_name][0]["company_skills"])
        recommended_jobs = recommend_jobs(candidate_skills_list, job_opportunities)
        print(len(recommended_jobs))

# Print the recommended jobs
        print(type(recommended_jobs))
        #print(skills_arr)
        data = {job_name: recommended_jobs}
        return JsonResponse(data)
    
    # {
    # "id": 2,
    # "json_resp": {
    #     "Data Scientist": [
    #         {


        