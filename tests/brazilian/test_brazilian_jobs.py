from src.pre_built.brazilian_jobs import read_brazilian_file

file = "tests/mocks/brazilians_jobs.csv"

keys_in_portuguese = ["titulo", "salario", "tipo"]
keys_in_english = ["title", "salary", "type"]


def test_brazilian_jobs():
    # VERIFICA SE, PARA CADA TRABALHO DA LISTA,
    # AS CHAVES EM INGLÊS ESTÃO PRESENTES E
    # AS CHAVES EM PORTUGUÊS NÃO

    brazilian_jobs = read_brazilian_file(file)
    for job in brazilian_jobs:
        for key_in_english in keys_in_english:
            assert(key_in_english in job) is True
        for key_in_portuguese in keys_in_portuguese:
            assert(key_in_portuguese not in job) is True
