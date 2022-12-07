from typing import Union, Dict


def validate_salary(salary: Union[int, str]) -> None:
    if(
        (not isinstance(salary, int) and not isinstance(salary, str))
        or (isinstance(salary, str) and not salary.isnumeric())
    ):
        raise ValueError("Invalid salary.")


def validate_salaries_dict(job: Dict) -> None:
    max = "max_salary"
    min = "min_salary"

    if(
        (max not in job or min not in job)
        or (not str(job[max]).isnumeric() or not str(job[min]).isnumeric())
        or (int(job[min]) > int(job[max]))
    ):
        raise ValueError("Invalid salaries dict.")
