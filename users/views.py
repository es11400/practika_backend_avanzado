from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from django.views import View
from rest_auth.registration.views import SocialLoginView
from rest_auth.social_serializers import TwitterLoginSerializer
from rest_auth.views import LoginView

from django.forms.models import modelform_factory
from braces.views import LoginRequiredMixin
from django.views.generic import CreateView
from oauth2_provider.models import get_application_model

class LogoutView(View):

    def get(self, request):
        """
        Hace el logout de un usuario y redirige al login
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        if request.user.is_authenticated():
            django_logout(request)
        return redirect('/')



class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class TwitterLogin(LoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter
