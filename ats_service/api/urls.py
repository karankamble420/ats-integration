from django.urls import path
from .views import get_jobs, create_candidate

urlpatterns = [
    path("jobs/", get_jobs),
    path("candidates/", create_candidate),
]
