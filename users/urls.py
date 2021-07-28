from django.urls import path
from django.urls.conf import include
from django.urls.resolvers import URLPattern
from .views import FacebookLogin
from rest_auth.registration.views import (
    SocialAccountListView, SocialAccountDisconnectView
)

urlpatterns=[
   path('', include('dj_rest_auth.urls')),
   path('register/', include('dj_rest_auth.registration.urls')),
   path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
   # path(r'^rest-auth/github/$', GithubLogin.as_view(), name='github_login'),
   path(
      'socialaccounts/',
      SocialAccountListView.as_view(),
      name='social_account_list'
   ),
   path(
      'socialaccounts/(?P<pk>\d+)/disconnect/',
      SocialAccountDisconnectView.as_view(),
      name='social_account_disconnect'
   )
]