# from selenium.webdriver.chrome.webdriver import WebDriver
import time

import pytest
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver


@pytest.fixture(scope="session")
def webdriver_setup():
    print("### Establishing connection with the server ###")

    driver = WebDriver()
    url = "http://localhost:8000/lesson26/dz.html"
    driver.get(url)

    yield driver

    print("### Closing connection with the server ###")
    time.sleep(2)
    driver.quit()


@pytest.fixture()
def secret_key_check(webdriver_setup, request):
    frame_name, secret_phrase = request.param
    driver = webdriver_setup

    # if frame_name not in ["frame1","frame2"]:
    #     raise NoSuchFrameException("The frame does not exist.Cannot switch to it.")

    driver.switch_to.frame(driver.find_element(By.ID, frame_name))

    if frame_name == "frame1":
        frame_input = driver.find_element(By.ID, "input1")
    elif frame_name == "frame2":
        frame_input = driver.find_element(By.ID, "input2")

    frame_input.click()
    time.sleep(1)
    frame_input.send_keys(secret_phrase)

    frame_check_btn = driver.find_element(By.TAG_NAME, "button")
    time.sleep(1)
    frame_check_btn.click()

    frame_alert = Alert(driver)
    time.sleep(1)
    alert_msg = frame_alert.text

    frame_alert.accept()
    time.sleep(1)

    frame_input.clear()

    driver.switch_to.default_content()
    time.sleep(1)

    yield alert_msg
