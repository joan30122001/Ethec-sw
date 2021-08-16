from django.shortcuts import render

# from __future__ import unicode_literals

from functools import wraps

from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.views import redirect_to_login as dj_redirect_to_login
from django.core.exceptions import PermissionDenied

from rolepermissions.checkers import has_role, has_permission
from rolepermissions.utils import user_is_authenticated

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView


def has_role_decorator(role, redirect_to_login=None):
    def request_decorator(dispatch):
        @wraps(dispatch)
        def wrapper(request, *args, **kwargs):
            user = request.user
            if user_is_authenticated(user):
                if has_role(user, role):
                    return dispatch(request, *args, **kwargs)

            redirect = redirect_to_login
            if redirect is None:
                redirect = getattr(
                    settings, 'ROLEPERMISSIONS_REDIRECT_TO_LOGIN', False)
            if redirect:
                return dj_redirect_to_login(request.get_full_path())
            raise PermissionDenied
        return wrapper
    return request_decorator


def has_permission_decorator(write_articles, redirect_to_login=None):
    def request_decorator(dispatch):
        @wraps(dispatch)
        def wrapper(request, *args, **kwargs):
            user = request.user
            if user_is_authenticated(user):
                if has_permission(user, write_articles):
                    return dispatch(request, *args, **kwargs)

            redirect = redirect_to_login
            if redirect is None:
                redirect = getattr(
                    settings, 'ROLEPERMISSIONS_REDIRECT_TO_LOGIN', False)
            if redirect:
                return dj_redirect_to_login(request.get_full_path())
            raise PermissionDenied
        return wrapper
    return request_decorator



class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter



class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = "https://github.com/login"
    client_class = OAuth2Client


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:3000"
    client_class = OAuth2Client