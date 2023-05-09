from rest_framework import serializers

from authentication.models import User
from technicalquestions_api.api.serializers import ResultTestSerializer

  
class UserSerializer(serializers.ModelSerializer):
    results = ResultTestSerializer(many=True, read_only=True)
    class Meta:
        model = User
        #fields = ['username', 'email', 'password', 'languages', 'frameworks', 'databases', 'skills', 'results']
        fields = ['username', 'email', 'password', 'skills', 'results']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance