import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search_wiki(android_mobile_management):
    with step('Tap on the skip button'):
        browser.element((AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_skip_button')).click()

    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia:id/search_src_text")).type(
            'Appium')  # org.wikipedia.alpha:id/search_src_text

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


# com.android.chrome:id/title_url_container
def test_open_some_article(android_mobile_management):
    with step('Tap on the skip button'):
        browser.element((AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_skip_button')).click()

    with step('Open wiki and search the article'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia:id/search_src_text")).type(
            'Japan')  # android.widget.TextView
        browser.element((AppiumBy.ID, "org.wikipedia:id/page_list_item_title")).click()

    with step('Verify article found'):
        browser.element((AppiumBy.XPATH,
                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[1]")).should(
            have.text('Japan'))

