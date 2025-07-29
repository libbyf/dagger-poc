from ..main import add
import pytest

@pytest.mark.test
def test_add():
    assert add(2, 3) == 5
