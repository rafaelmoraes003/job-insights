from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs = read(path)
    industries = {job["industry"] for job in jobs if job["industry"]}
    return industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    jobs_by_industry = [job for job in jobs if job["industry"] == industry]
    return jobs_by_industry
