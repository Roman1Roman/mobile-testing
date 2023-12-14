from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be


def test_simple_app(ios_mobile_management):
    # THEN
    with step('Check the text elements'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'UI Elements')).should(be.visible)
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text')).should(be.visible)
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Alert')).should(be.visible)