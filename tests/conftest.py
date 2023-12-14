import os
import allure
import allure_commons
from appium import webdriver

import utils.attach
import pytest
import config
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selene import browser, support


@pytest.fixture(scope='function')
def android_mobile_management():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "android",
        "platformVersion": "13.0",
        "deviceName": "Samsung Galaxy S23 Ultra",

        # Set URL of the application under test
        "app": "bs://c1c52615799e5efca0852cc5e27e222eb04bb041",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "Android tests",
            "buildName": "browserstack-wikipedia-build",
            "sessionName": "BStack wikipedia_test",

            # Set your access credentials
            "userName": config.username,
            "accessKey": config.access_key
        }
    })

    browser.config.driver = webdriver.Remote(
        config.remote_browser_url,
        options=options
    )
    browser.config.timeout = 10.0

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext)

    yield
    utils.attach.attach_bstack_screenshot()
    utils.attach.attach_bstack_page_source()

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    utils.attach.attach_bstack_video(session_id)


@pytest.fixture(scope='function')
def ios_mobile_management():
    options = XCUITestOptions().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "ios",
        "platformVersion": "16",
        "deviceName": "iPhone 14",

        # Set URL of the application under test
        "app": "bs://444bd0308813ae0dc236f8cd461c02d3afa7901d",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "Ios tests",
            "buildName": "browserstack-simple-app-build",
            "sessionName": "BStack Simple app test",

            # Set your access credentials
            "userName": config.username,
            "accessKey": config.access_key
        }
    })

    browser.config.driver = webdriver.Remote(
        config.remote_browser_url,
        options=options
    )
    browser.config.timeout = 10.0

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext)

    yield

    utils.attach.attach_bstack_screenshot()
    utils.attach.attach_bstack_page_source()

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    utils.attach.attach_bstack_video(session_id)


