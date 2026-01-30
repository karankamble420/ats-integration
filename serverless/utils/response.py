import json

def success(data=None, meta=None):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "success": True,
            "data": data,
            "meta": meta
        })
    }

def error(message, status=400):
    return {
        "statusCode": status,
        "body": json.dumps({
            "success": False,
            "error": message
        })
    }
