from typing import Union


def validate_salary(salary: Union[int, str]) -> None:
    if(
        (not isinstance(salary, int) and not isinstance(salary, str))
        or (isinstance(salary, str) and not salary.isnumeric())
    ):
        raise ValueError("Invalid salary.")
