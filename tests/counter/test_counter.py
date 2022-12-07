import pytest
from src.pre_built.counter import count_ocurrences

file = "data/jobs.csv"


def test_counter():
    # LOWER CASE
    assert(count_ocurrences(file, "javascript")) == 122
    assert(count_ocurrences(file, "python")) == 1639

    # UPPER CASE
    assert(count_ocurrences(file, "JAVASCRIPT")) == 122
    assert(count_ocurrences(file, "PYTHON")) == 1639

    # SHUFFLED
    assert(count_ocurrences(file, "JavaScript")) == 122
    assert(count_ocurrences(file, "Python")) == 1639

    # WRONG ASSERTIONS
    assert(count_ocurrences(file, "javascript")) != 12345
    assert(count_ocurrences(file, "python")) != 14
    assert(count_ocurrences(file, "xablau")) == 0

    # NON-EXISTENT FILE
    with pytest.raises(FileNotFoundError):
        count_ocurrences("non-existent-file.txt", "duck")
