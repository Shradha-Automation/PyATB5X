from functools import partial

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_webtables():
    driver = webdriver.Firefox()
    driver.get("https://awesomeqa.com/webtable.html")
    # driver.maximize_window()
    # //table[@id="customers"]/tbody/tr[2]/td
    row_elements = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr")
    row = len(row_elements)
    print(row)
    col_elements = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr[2]/td")
    col = len(col_elements)
    print(col)

    first_part = "// table[@id ='customers']/tbody/tr["
    second_part = "]/td["
    third_part = "]"

    for i in range(2, row + 1):
        for j in range(1, col + 1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            data=driver.find_element(By.XPATH, dynamic_path)
            print(data.text,end=" ")

    driver.close()