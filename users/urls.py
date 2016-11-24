
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from users.api import UserModelViewSet
from users.views import LogoutView, FacebookLogin, TwitterLogin

router = DefaultRouter()
router.register('/1.0/users', UserModelViewSet, base_name='api_users_')

urlpatterns = [
    # Web URLS
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),

    # API URLS
    url(r'api', include(router.urls)),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^rest-auth/twitter/$', TwitterLogin.as_view(), name='twitter_login'),

    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^accounts/', include('allauth.urls')),

]