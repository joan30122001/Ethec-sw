from django.urls import path
from django.urls.conf import include
from django.urls.resolvers import URLPattern

urlpatterns=[
   path('', include('dj_rest_auth.urls')),
   path('register/', include('dj_rest_auth.registration.urls')),
]