import json
from ats_providers.workable import WorkableATS


def handler(event, context):
    ats = WorkableATS()
    result = ats.get_jobs()

    return {
        "statusCode": 200 if result.get("success") else 401,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(result),
    }
