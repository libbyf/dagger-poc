from invoke import task
import pytest

@task
def test(c):
    pytest.main(["tests/"])