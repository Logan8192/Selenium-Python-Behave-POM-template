from behave import given, when, then
from POM.pages.home_page import HomePage
from hamcrest import *


@given('I am on the home page')
def home_page_verification(context):
    home_page = HomePage(context.driver)
    context.current_page = home_page
    assert_that(home_page.is_page_loaded(), is_(equal_to(True)), reason="Home page is not loaded")


@when('I type "Python" in the search bar and press enter')
def search_website(context):
    home_page = context.current_page
    home_page.fill_search_input("Python")
    assert_that(home_page.return_search_input_text(), is_(equal_to("Python")),
                reason="Text contained in the search input was not the expected")
    search_results_page = home_page.click_search_button()
    context.current_page = search_results_page


@then('The search results page shows me a list of different websites related with the word "Python"')
def check_website_results(context):
    search_results_page = context.current_page
    assert_that(search_results_page.is_page_loaded(), equal_to(True),
                reason="Search Results Page is not loaded after clicking the search button")
    assert_that(search_results_page.return_search_input_text(), equal_to("Python"),
                reason="Text contained in the search input was not the expected")
    assert_that(search_results_page.are_page_results_displayed(), equal_to(True),
                reason="There are not page results displayed after searching for 'Python'")
