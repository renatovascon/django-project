from django.urls import path
from blog_api.views import index

urlpatterns = [
    path('', index),
]
