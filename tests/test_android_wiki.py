import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@pytest.mark.parametrize('mobile_management', ['android'], indirect=True)
def test_search_wiki(mobile_management):
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(
            'Appium')  # org.wikipedia.alpha:id/search_src_text

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


@pytest.mark.parametrize('mobile_management', ['android'], indirect=True)
def test_open_some_article(mobile_management):
    with step('Open wiki and search the article'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(
            'Japan')  # android.widget.TextView
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")).click()

    with step('Verify article found'):
        results = browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/pcs"))
        results.should(have.text('Japan'))
