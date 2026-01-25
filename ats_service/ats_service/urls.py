from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "status": "ATS Integration API running",
        "endpoints": {
            "jobs": "/api/jobs/",
            "candidates": "/api/candidates/"
        }
    })

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("api/", include("ats_service.api.urls")),
]
