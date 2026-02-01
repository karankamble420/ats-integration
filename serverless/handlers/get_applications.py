from utils.response import response


def handler(event, context):
    params = event.get("queryStringParameters") or {}
    page = int(params.get("page", 1))
    limit = int(params.get("limit", 10))

    applications = [
        {
            "application_id": "app_001",
            "candidate_id": "cand_001",
            "job_id": "job_001",
            "status": "applied"
        }
    ]

    start = (page - 1) * limit
    end = start + limit

    return response(200, {
        "success": True,
        "mode": "preview",
        "page": page,
        "limit": limit,
        "data": applications[start:end]
    })
