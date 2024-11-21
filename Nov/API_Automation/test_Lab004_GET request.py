# Create Booking Testcase
# Verify that Booking is not null
# Status Code

import pytest
import allure
import requests


@allure.title("Test GET Request - Restful BOOKER Project #1")
@allure.description("TC#1 -> Verify the GET Request with ID works")
# @allure.tag(*tags: "regression", "p0", "smoke")
# @allure.lebel(lebel_type: "owner",*lebels: "Shradha Priya")
@allure.testcase("TC #1")
@pytest.mark.smoke
def test_get_single_request_by_id_positive():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url)
    print(response_data.text)
    print(response_data.json())
    print(response_data.headers)
    assert response_data.status_code == 200

    @allure.title("Test GET Request - Restful BOOKER Project #2")
    @allure.description("TC#2 -> Verify the GET Request with ID works")
    # @allure.tag(*tags: "regression", "p0", "smoke")
    # @allure.lebel(lebel_type: "owner",*lebels: "Shradha Priya")
    @allure.testcase("TC #2")
    @pytest.mark.smoke
    def test_get_single_request_by_id_negative():
        url = "https://restful-booker.herokuapp.com/booking/-1"
        response_data = requests.get(url)
        print(response_data.text)
        print(response_data.json())
        print(response_data.headers)
        assert response_data.status_code == 404

        @allure.title("Test GET Request - Restful BOOKER Project #3")
        @allure.description("TC#2 -> Verify the GET Request with ID works")
        # @allure.tag(*tags: "regression", "p0", "smoke")
        # @allure.lebel(lebel_type: "owner",*lebels: "Shradha Priya")
        @allure.testcase("TC #3")
        @pytest.mark.smoke
        def test_get_single_request_by_id_negative():
            url = "https://restful-booker.herokuapp.com/booking/-1"
            response_data = requests.get(url)
            print(response_data.text)
            print(response_data.json())
            print(response_data.headers)
            assert response_data.status_code == 404
