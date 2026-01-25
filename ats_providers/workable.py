import os
import requests


class WorkableATS:
    def __init__(self):
        self.base_url = os.getenv("ATS_BASE_URL", "https://api.workable.com/spi/v3")
        self.api_key = os.getenv("ATS_API_KEY")
        self.company = os.getenv("WORKABLE_COMPANY")

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
        }

    def get_jobs(self):
        # ✅ MOCK-SAFE MODE (no credentials)
        if not self.api_key or not self.company:
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

        # ✅ REAL MODE (SPI credentials available)
        url = f"{self.base_url}/accounts/{self.company}/jobs"
        response = requests.get(url, headers=self._headers())

        if response.status_code == 401:
            return {
                "success": False,
                "provider": "workable",
                "error": "Unauthorized",
                "message": "SPI access not enabled or API key invalid"
            }

        response.raise_for_status()

        return {
            "success": True,
            "provider": "workable",
            "mode": "live",
            "data": response.json()
        }
