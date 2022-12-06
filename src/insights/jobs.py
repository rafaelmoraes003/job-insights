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
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
