import json
from ats_providers.workable import WorkableATS
from utils.response import response


def handler(event, context):
    data = json.loads(event.get("body", "{}"))

    required = ["job_id", "name", "email"]
    missing = [f for f in required if f not in data]

    if missing:
        return response(400, {
            "success": False,
            "error": "Missing fields",
            "fields": missing
        })

    ats = WorkableATS()
    result = ats.create_candidate(data)
    return response(200, result)
