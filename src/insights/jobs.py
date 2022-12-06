from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    try:
        with open(path, mode="r", encoding="utf-8") as file:
            content = csv.DictReader(file, delimiter=",", quotechar='"')
            content_list = [row for row in content]
        return content_list
    except OSError:
        raise FileNotFoundError("File not found")


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    job_types = {job["job_type"] for job in jobs}
    return job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    jobs_by_type = [job for job in jobs if job["job_type"] == job_type]
    return jobs_by_type
