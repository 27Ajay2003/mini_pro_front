from rest_framework import serializers

from technicalquestions_api.models import QuizQuestion
from technicalquestions_api.models import ResultTest


class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model= QuizQuestion
        fields="__all__"   

class ResultTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultTest
        fields="__all__" 