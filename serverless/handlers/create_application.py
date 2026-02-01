import json
from utils.response import response


def handler(event, context):
    data = json.loads(event.get("body", "{}"))

    if "candidate_id" not in data or "job_id" not in data:
        return response(400, {
            "success": False,
            "error": "candidate_id and job_id required"
        })

    return response(200, {
        "success": True,
        "mode": "preview",
        "application": {
            "application_id": "app_001",
            "candidate_id": data["candidate_id"],
            "job_id": data["job_id"],
            "status": "applied"
        }
    })
