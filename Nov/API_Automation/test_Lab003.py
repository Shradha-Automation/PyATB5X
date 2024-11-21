import pytest
import allure

@pytest.mark.smoke
def test_verify_sum():
    assert (2 + 2) == 4


@pytest.mark.smoke
def test_verify_sub():
    assert (2 - 2) == 0


@pytest.mark.skip(reason= "Not Completed, skip it")
def test_verify_mul():
    assert (2 * 2) == 4

@pytest.mark.reg
def test_verify_div():
    assert 9/2 == 4.5
