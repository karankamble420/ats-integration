from utils.response import success

# Same mock store
APPLICATIONS = [
    {
        "application_id": "app_1",
        "job_id": "job_063",
        "candidate_id": "cand_001",
        "status": "applied"
    }
]

def handler(event, context):
    query = event.get("queryStringParameters") or {}

    job_id = query.get("job_id")
    page = int(query.get("page", 1))
    limit = int(query.get("limit", 10))

    results = APPLICATIONS

    if job_id:
        results = [a for a in results if a["job_id"] == job_id]

    start = (page - 1) * limit
    end = start + limit

    return success(
        data=results[start:end],
        meta={
            "page": page,
            "limit": limit,
            "total": len(results)
        }
    )
