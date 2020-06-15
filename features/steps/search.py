from behave import given, when, then
from POM.pages.home_page import HomePage


@given('I am on the home page')
def home_page_verification(context):
    home_page = HomePage(context.driver)
    context.current_page = home_page
    assert home_page.is_page_loaded() is True


@when('I type "Python" in the search bar and press enter')
def search_website(context):
    home_page = context.current_page
    home_page.fill_search_input("Python")
    assert home_page.return_search_input_text() == 'Python'
    search_results_page = home_page.click_search_button()
    context.current_page = search_results_page


@then('The search results page shows me a list of different websites related with the word "Python"')
def check_website_results(context):
    search_results_page = context.current_page
    assert search_results_page.is_page_loaded() is True
    assert search_results_page.return_search_input_text() == "Python"
    assert search_results_page.are_page_results_displayed() is True
