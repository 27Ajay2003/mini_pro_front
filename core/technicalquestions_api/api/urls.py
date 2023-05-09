from django.urls import path, include
from rest_framework import routers
from technicalquestions_api.api.views import QuizQuestionViewSet, GenerateTechnicalQuestionsView
from .views import ResultTestListCreateView, ResultTestUserView, ResultTestUserDetailView, SimilarQuestionsView, ProvideQuestionsView


router = routers.DefaultRouter()
router.register(r'questions', QuizQuestionViewSet)
# route to view the QuizQuestions

urlpatterns = [
    path('', include(router.urls)),
    path('question/generate/', GenerateTechnicalQuestionsView.as_view(), name='generate-technical-questions'), 
    # route changed from questions to question to avoid url match error

    path('question/similar/', SimilarQuestionsView.as_view(), name='generate-similar-questions'),
    path('question/provide/', ProvideQuestionsView.as_view(), name='generate-provide-questions'),
    # both these routes take in {"ids": [...]}

    path('prev-results/', ResultTestListCreateView.as_view(), name='result_test_list_create'),
    # for admin 

    path('prev-results/user/', ResultTestUserView.as_view(), name='result_test_user_list'),
    # for logged in user to view past results

    path('prev-results/user/<int:pk>/', ResultTestUserDetailView.as_view(), name='result_test_user_detail'),
    # for logged in user to view a specific past result
]