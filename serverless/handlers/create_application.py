import json
from utils.response import success, error

# Mock DB (in-memory for demo)
APPLICATIONS = []

def handler(event, context):
    try:
        body = json.loads(event["body"])

        required = ["job_id", "candidate_id"]
        for field in required:
            if field not in body:
                return error(f"Missing field: {field}")

        application = {
            "application_id": f"app_{len(APPLICATIONS) + 1}",
            "job_id": body["job_id"],
            "candidate_id": body["candidate_id"],
            "status": "applied"
        }

        APPLICATIONS.append(application)

        return success(application)

    except Exception as e:
        return error(str(e), 500)
