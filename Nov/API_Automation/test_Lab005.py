import pytest
import allure


@allure.title("TC #1 - verify that  2-2 is equal to 0")
@allure.description("This is a smoke testcase with  check")
@pytest.mark.smoke
def test_sub0():
    assert 2 - 2 == 0

    @allure.title("TC #2 - verify that  2-2 is equal to 0")
    @allure.description("This is a smoke testcase with  check")
    @pytest.mark.smoke
    def test_sub1():
        assert 2 - 2 == 0

        @allure.title("TC #3 - verify that  2-2 is equal to 0")
        @allure.description("This is a smoke testcase with  check")
        @pytest.mark.smoke
        def test_sub3():
            assert 2 - 2 == 0

            @allure.title("TC #4 - verify that  2-2 is equal to 0")
            @allure.description("This is a smoke testcase with  check")
            @pytest.mark.smoke
            def test_sub4():
                assert 0 - 0 != 0
