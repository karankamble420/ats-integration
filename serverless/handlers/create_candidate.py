import json
from ats_providers.workable import WorkableATS
from utils.response import success, error

def handler(event, context):
    try:
        body = json.loads(event["body"])

        for field in ["job_id", "name", "email"]:
            if field not in body:
                return error(f"Missing field: {field}")

        ats = WorkableATS()
        candidate = ats.create_candidate(body)

        return success(candidate)

    except Exception as e:
        return error(str(e), 500)
