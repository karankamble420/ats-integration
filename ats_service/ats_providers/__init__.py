import os
from .workable import WorkableATS


def get_ats():
    provider = os.getenv("ATS_PROVIDER", "workable")

    if provider == "workable":
        return WorkableATS()

    raise ValueError("Unsupported ATS provider")
