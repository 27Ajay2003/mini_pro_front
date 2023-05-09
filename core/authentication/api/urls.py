from django.urls import path, include
from rest_framework import routers
from authentication.api.views import RegisterView, LoginView, UserView, ProfileViewSet, RefreshTokenView

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserView.as_view(), name='user'),
    
    path('refresh/', RefreshTokenView.as_view(), name='token refresh'),  
    # send refresh token obtained after login as a post request to get new access token
    # currently the auth is not required - may need to change later
    
    path('', include(router.urls)),
]