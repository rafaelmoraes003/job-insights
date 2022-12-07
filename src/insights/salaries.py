from typing import Union, List, Dict
from src.insights.jobs import read
from src.validators import validate_salaries_dict, validate_salary


def get_salaries_set(type: str, jobs_list: list) -> set:
    salaries = {
        int(job[type])
        for job in jobs_list
        if job[type].isdigit()  # salary = str
    }

    return salaries


def get_max_salary(path: str) -> int:
    jobs = read(path)
    max_salaries = get_salaries_set("max_salary", jobs)
    return max(max_salaries)


def get_min_salary(path: str) -> int:
    jobs = read(path)
    min_salaries = get_salaries_set("min_salary", jobs)
    return min(min_salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    validate_salaries_dict(job)
    validate_salary(salary)
    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    max = "max_salary"
    min = "min_salary"
    jobs_in_range = list()

    for job in jobs:
        job_dict = {max: job[max], min: job[min]}
        try:
            if matches_salary_range(job_dict, salary) is True:
                jobs_in_range.append(job)
        except ValueError as exc:
            print(exc)

    return jobs_in_range
