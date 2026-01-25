from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ats_service.ats_providers import get_ats


@api_view(["GET"])
def get_jobs(request):
    ats = get_ats()
    return Response(ats.get_jobs())


@api_view(["POST"])
def create_candidate(request):
    ats = get_ats()
    data = request.data

    required_fields = ["job_id", "name", "email"]
    missing = [f for f in required_fields if f not in data]

    if missing:
        return Response(
            {
                "success": False,
                "error": "Missing fields",
                "fields": missing
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    result = ats.create_candidate(data)
    return Response(result)
