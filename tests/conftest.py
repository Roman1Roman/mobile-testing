import os
import allure
import utils.attach
import pytest
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(params=['android', 'ios'], scope='function', autouse=True)
def mobile_management(request):
    username = os.getenv('USER_NAME')
    access_key = os.getenv('ACCESS_KEY')
    remote_browser_url = os.getenv('REMOTE_BROWSER_URL')
    if request.param == 'android':
        options = UiAutomator2Options().load_capabilities({
            # Specify device and os_version for testing
            "platformName": "android",
            "platformVersion": "9.0",
            "deviceName": "Google Pixel 3",

            # Set URL of the application under test
            "app": "bs://sample.app",

            # Set other BrowserStack capabilities
            'bstack:options': {
                "projectName": "Android tests",
                "buildName": "browserstack-wikipedia-build",
                "sessionName": "BStack wikipedia_test",

                # Set your access credentials
                "userName": username,
                "accessKey": access_key
            }
        })

        browser.config.driver_remote_url = remote_browser_url
        browser.config.driver_options = options
        browser.config.timeout = 10.0

    elif request.param == 'ios':
        options = XCUITestOptions().load_capabilities({
            # Specify device and os_version for testing
            "platformName": "ios",
            "platformVersion": "16",
            "deviceName": "iPhone 14 Pro Max",

            # Set URL of the application under test
            "app": "bs://444bd0308813ae0dc236f8cd461c02d3afa7901d",

            # Set other BrowserStack capabilities
            'bstack:options': {
                "projectName": "Ios tests",
                "buildName": "browserstack-simple-app-build",
                "sessionName": "BStack Simple app test",

                # Set your access credentials
                "userName": username,
                "accessKey": access_key
            }
        })

        browser.config.driver_remote_url = remote_browser_url
        browser.config.driver_options = options
        browser.config.timeout = 10.0

    yield
    utils.attach.attach_bstack_screenshot()
    utils.attach.attach_bstack_page_source()

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    utils.attach.attach_bstack_video(session_id)

