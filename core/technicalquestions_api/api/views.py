from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from core.getkeywords import get_top_keywords


from technicalquestions_api.models import QuizQuestion, ResultTest
from technicalquestions_api.api.serializers import QuizQuestionSerializer, ResultTestSerializer

import json
from random import sample
from collections import defaultdict

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import random
from django.http import Http404





class QuizQuestionViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated,IsAdminUser]
    serializer_class = QuizQuestionSerializer
    queryset = QuizQuestion.objects.all() 

class GenerateTechnicalQuestionsView(APIView):
    permission_classes = [IsAuthenticated,IsAdminUser]
    def get(self, request):
        # Get all questions from the database grouped by subject
        questions_by_subject = defaultdict(list)
        for question in QuizQuestion.objects.all():
            questions_by_subject[question.subject].append(question)

        # Select 10 random questions for each subject
        questions = []
        for subject, subject_questions in questions_by_subject.items():
            questions += sample(subject_questions, 10)

        # Serialize the questions data to JSON
        data = [{
            'question_id': question.question_id,
            'topic': question.topic,
            'question': question.question,
            'option_a': question.option_a,
            'option_b': question.option_b,
            'option_c': question.option_c,
            'option_d': question.option_d,
            'correct_answer': question.correct_answer,
            'difficulty': question.difficulty,
            'cognitive_level': question.cognitive_level,
            'subject': question.subject,
        } for question in questions]

        # Return the questions data in a JSON response
        return Response(data)
    

class SimilarQuestionsView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        # Get list of wrong question ids from request body
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        wrong_question_ids = body.get('ids', [])
        invalid_ids = set(wrong_question_ids) - set(QuizQuestion.objects.values_list('question_id', flat=True))
        if invalid_ids:
            raise Http404(f'Invalid question ids: {", ".join(map(str, invalid_ids))}')

        # Get all questions except the ones the user attempted wrong
        ex_questions = QuizQuestion.objects.filter(question_id__in=wrong_question_ids)
        questions = QuizQuestion.objects.exclude(question_id__in=wrong_question_ids)

        # Create a matrix of the question features (topic, subject, difficulty, cognitive level)
        feature_matrix = []
        ex_feature_matrix = []
        subjects = {}
        for question in questions:
            features = [get_top_keywords(question.question) ,get_top_keywords(question.option_a), get_top_keywords(question.option_b), get_top_keywords(question.option_c), get_top_keywords(question.option_d),
                        question.difficulty, question.cognitive_level, question.subject,question.topic]
            feature_matrix.append(features)
            subject = question.subject
            if subject not in subjects:
                subjects[subject] = [question]
            else:
                subjects[subject].append(question)

        for question in ex_questions:
            features = [get_top_keywords(question.question) ,get_top_keywords(question.option_a), get_top_keywords(question.option_b), get_top_keywords(question.option_c), get_top_keywords(question.option_d),
                        question.difficulty, question.cognitive_level, question.subject,question.topic]
            ex_feature_matrix.append(features)

        # Create a dictionary to store the most similar questions
        similar_questions_dict = {}

        # Calculate the TF-IDF matrix
        tfidf_vectorizer = TfidfVectorizer()
        feature_matrix_tfidf = tfidf_vectorizer.fit_transform([','.join(map(str, row)) for row in feature_matrix])
        ex_feature_matrix_tfidf = tfidf_vectorizer.transform([','.join(map(str, row)) for row in ex_feature_matrix])

        # Calculate the cosine similarity matrix
        similarities = cosine_similarity(ex_feature_matrix_tfidf, feature_matrix_tfidf)

        #Find the 10 most similar questions for each subject
        # for i in range(similarities.shape[0]):
        #     sorted_indices = similarities[i].argsort()[::-1][:40]
        #     for index in sorted_indices:
        #         question = questions[int(index)] 
        #         subject = question.subject
        #         if subject not in similar_questions_dict:
        #             similar_questions_dict[subject] = [question]
        #         elif len(similar_questions_dict[subject]) < 10:
        #             similar_questions_dict[subject].append(question)
                    
                    
        # for i in range(similarities.shape[0]):
        #     sorted_indices = similarities[i].argsort()[::-1][:40]
        #     for index in sorted_indices:
        #         question = questions[int(index)] 
        #         subject = question.subject
        #         if subject not in similar_questions_dict:
        #             similar_questions_dict[subject] = []
        #         if question not in similar_questions_dict[subject]:
        #             similar_questions_dict[subject].append(question)
        #             if len(similar_questions_dict[subject]) >= 10:
        #                 break            

        # Return the similar questions as JSON
        # similar_questions_data = {}
        # for subject in subjects:
        #     subject_questions = similar_questions_dict.get(subject, [])
        #     if len(subject_questions) < 10:
        #         remaining_questions = subjects[subject][:10 - len(subject_questions)]
        #         subject_questions.extend(remaining_questions)
        #     subject_data = QuizQuestionSerializer(subject_questions, many=True).data
        #     similar_questions_data[subject] = subject_data

        # return JsonResponse(similar_questions_data)
        for i in range(similarities.shape[0]):
            sorted_indices = similarities[i].argsort()[::-1][:40]
            for index in sorted_indices:
                question = questions[int(index)] 
                subject = question.subject
                if subject not in similar_questions_dict:
                    similar_questions_dict[subject] = set([question])
                elif len(similar_questions_dict[subject]) < 10:
                    similar_questions_dict[subject].add(question)

        # Create a list of 10 unique questions for each subject
        similar_questions_data = {}
        for subject in subjects:
            subject_questions = list(similar_questions_dict.get(subject, set()))
            if len(subject_questions) < 10:
                remaining_questions = list(set(subjects[subject]) - set(subject_questions))
                subject_questions.extend(remaining_questions[:10 - len(subject_questions)])
            subject_data = QuizQuestionSerializer(subject_questions, many=True).data
            similar_questions_data[subject] = subject_data

        return JsonResponse(similar_questions_data)




    

class ProvideQuestionsView(APIView):
    permission_classes = [IsAuthenticated,IsAdminUser]

    def post(self, request):
        # Get list of wrong question ids from request body
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        question_ids = body.get('ids', [])

        # Get all questions except the ones the user attempted wrong
        questions = QuizQuestion.objects.filter(question_id__in=question_ids)
        #print(questions)
        data = []
        for question in questions:
            data.append({
                'question_id': question.question_id,
                'topic': question.topic,
                'question': question.question,
                'options': [
                    question.option_a,
                    question.option_b,
                    question.option_c,
                    question.option_d,
                ],
                'correct_answer': question.correct_answer,
                'difficulty': question.difficulty,
                'cognitive_level': question.cognitive_level,
                'subject': question.subject,
            })
        return JsonResponse({'questions': data})    
        
        
class ResultTestListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated,IsAdminUser]
    serializer_class = ResultTestSerializer

    def get_queryset(self):
        # print(self.request.user)
        return ResultTest.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = ResultTestSerializer(data=request.data)
        if serializer.is_valid():
            test = serializer.save()
            serializer = ResultTestSerializer(test)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ResultTestUserView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ResultTestSerializer

    def get_queryset(self):
        print(self.request.user)
        return ResultTest.objects.filter(user=self.request.user)
    

class ResultTestUserDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ResultTestSerializer

    def get_object(self):
        queryset = ResultTest.objects.filter(user=self.request.user)
        obj = get_object_or_404(queryset, pk=self.kwargs.get('pk'))
        return obj