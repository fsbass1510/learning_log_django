from django.urls import path
from . import views


urlpatterns = [
    path('', views.learning_logs, name='Learning_logs'),
]