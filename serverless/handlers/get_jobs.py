import json
from ats_providers.workable import WorkableATS

def handler(event, context):
    try:
        # ✅ Safely read query params
        query = event.get("queryStringParameters") or {}

        page = int(query.get("page", 1))
        limit = int(query.get("limit", 10))

        if page < 1:
            page = 1
        if limit < 1:
            limit = 10

        ats = WorkableATS()
        result = ats.get_jobs()

        jobs = result.get("data", [])

        # ✅ Pagination math
        start = (page - 1) * limit
        end = start + limit

        paginated = jobs[start:end]

        return {
            "statusCode": 200,
            "body": json.dumps({
                "success": True,
                "provider": result.get("provider"),
                "mode": result.get("mode"),
                "page": page,
                "limit": limit,
                "total": len(jobs),
                "data": paginated
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "success": False,
                "error": str(e)
            })
        }
