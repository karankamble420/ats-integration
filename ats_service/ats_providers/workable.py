import os
import requests


class WorkableATS:
    def __init__(self):
        self.base_url = os.getenv("ATS_BASE_URL")
        self.api_key = os.getenv("ATS_API_KEY")
        self.company = os.getenv("WORKABLE_COMPANY")
        self.mock_mode = os.getenv("ATS_MOCK_MODE", "true").lower() == "true"

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
        }

    # -----------------------
    # GET JOBS
    # -----------------------
    def get_jobs(self):
        if self.mock_mode:
            return {
                "success": True,
                "provider": "workable",
                "mode": "mock",
                "data": [
                    {
                        "id": "job_001",
                        "title": "Backend Developer",
                        "location": "Remote",
                        "department": "Engineering"
                    },
                    {
                        "id": "job_002",
                        "title": "Frontend Developer",
                        "location": "Bangalore",
                        "department": "Engineering"
                    }
                ]
            }

        url = f"{self.base_url}/accounts/{self.company}/jobs"
        response = requests.get(url, headers=self._headers())
        response.raise_for_status()
        return response.json()

    # -----------------------
    # CREATE CANDIDATE
    # -----------------------
    def create_candidate(self, data):
        if self.mock_mode:
            return {
                "success": True,
                "provider": "workable",
                "mode": "mock",
                "candidate": {
                    "id": "cand_001",
                    "job_id": data.get("job_id"),
                    "name": data.get("name"),
                    "email": data.get("email"),
                    "status": "created"
                }
            }

        url = f"{self.base_url}/accounts/{self.company}/candidates"
        response = requests.post(url, json=data, headers=self._headers())
        response.raise_for_status()
        return response.json()
