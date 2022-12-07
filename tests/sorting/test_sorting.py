import pytest
from src.pre_built.sorting import sort_by


@pytest.fixture
def jobs():
    return [
        {
            "id": 1,
            "max_salary": 3000,
            "min_salary": 1000,
            "date_posted": "2022-12-07",
        },
        {
            "id": 2,
            "max_salary": 1000,
            "min_salary": 800,
            "date_posted": "2022-12-06",
        },
        {
            "id": 3,
            "max_salary": 5000,
            "min_salary": 4500,
            "date_posted": "2022-12-12",
        },
    ]


@pytest.fixture
def jobs_after_sort_by_max_salary():
    return [
        {
            "id": 3,
            "max_salary": 5000,
            "min_salary": 4500,
            "date_posted": "2022-12-12",
        },
        {
            "id": 1,
            "max_salary": 3000,
            "min_salary": 1000,
            "date_posted": "2022-12-07",
        },
        {
            "id": 2,
            "max_salary": 1000,
            "min_salary": 800,
            "date_posted": "2022-12-06",
        },
    ]


@pytest.fixture
def jobs_after_sort_by_min_salary():
    return [
        {
            "id": 2,
            "max_salary": 1000,
            "min_salary": 800,
            "date_posted": "2022-12-06",
        },
        {
            "id": 1,
            "max_salary": 3000,
            "min_salary": 1000,
            "date_posted": "2022-12-07",
        },
        {
            "id": 3,
            "max_salary": 5000,
            "min_salary": 4500,
            "date_posted": "2022-12-12",
        },
    ]


@pytest.fixture
def jobs_after_wrong_sort_by_min_salary():
    return [
        {
            "id": 3,
            "max_salary": 5000,
            "min_salary": 4500,
            "date_posted": "2022-12-12",
        },
        {
            "id": 1,
            "max_salary": 3000,
            "min_salary": 1000,
            "date_posted": "2022-12-07",
        },
        {
            "id": 2,
            "max_salary": 1000,
            "min_salary": 800,
            "date_posted": "2022-12-06",
        },
    ]


@pytest.fixture
def jobs_after_sort_by_date_posted():
    return [
        {
            "id": 3,
            "max_salary": 5000,
            "min_salary": 4500,
            "date_posted": "2022-12-12",
        },
        {
            "id": 1,
            "max_salary": 3000,
            "min_salary": 1000,
            "date_posted": "2022-12-07",
        },
        {
            "id": 2,
            "max_salary": 1000,
            "min_salary": 800,
            "date_posted": "2022-12-06",
        },
    ]


def test_sort_by_criteria(
    jobs,
    jobs_after_sort_by_max_salary,
    jobs_after_sort_by_min_salary,
    jobs_after_wrong_sort_by_min_salary,
    jobs_after_sort_by_date_posted
):
    my_jobs = jobs

    # SORT MY MAX_SALARY
    sort_by(my_jobs, "max_salary")
    assert(my_jobs) == jobs_after_sort_by_max_salary
    assert(my_jobs) != jobs_after_sort_by_min_salary

    # SORT BY MIN_SALARY
    sort_by(my_jobs, "min_salary")
    assert(my_jobs) == jobs_after_sort_by_min_salary  # CORRECT SORT
    assert(my_jobs) != jobs_after_wrong_sort_by_min_salary  # WRONG SORT

    # SORT BY DATE POSTED
    sort_by(my_jobs, "date_posted")
    assert(my_jobs) == jobs_after_sort_by_date_posted

    # CRITERIA ERROR
    with pytest.raises(ValueError):
        sort_by(my_jobs, "job_type")
