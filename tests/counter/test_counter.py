import pytest
from src.pre_built.counter import count_ocurrences

file = "data/jobs.csv"


def test_counter():
    assert (count_ocurrences(file, "javascript")) == 122
    assert (count_ocurrences(file, "python")) == 1639

    assert (count_ocurrences(file, "javascript")) != 22
    assert (count_ocurrences(file, "python")) != 140

    assert(count_ocurrences(file, "xablau")) == 0

    with pytest.raises(FileNotFoundError):
        count_ocurrences("non-existent-file.txt", "duck")
