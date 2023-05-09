from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import viewsets, mixins
from django.shortcuts import get_object_or_404


from authentication.models import User
from authentication.api.serializers import UserSerializer


class ProfileViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        refresh = RefreshToken.for_user(user)

        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(data)


class UserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = get_object_or_404(User, username=request.user.username)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request):
        user = get_object_or_404(User, username=request.user.username)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
    
    def delete(self, request):
        user = get_object_or_404(User, username=request.user.username)
        user.delete()
        return Response(status=204)


class RefreshTokenView(TokenRefreshView):
    pass