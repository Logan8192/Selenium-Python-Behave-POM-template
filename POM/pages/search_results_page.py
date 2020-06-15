from selenium.webdriver.common.by import By
from ..base_page import BasePage


class SearchResultsPageLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, "#search_form_input")
    PAGE_RESULTS = (By.CSS_SELECTOR, ".result__body")


class SearchResultsPage(BasePage):

    def are_page_results_displayed(self):
        """
        Checks if the results are displayed in the 'all' tab.
        :return: True if the search displayed results.
        :rtype: bool
        """
        return self.is_element_present(SearchResultsPageLocators.PAGE_RESULTS)

    def is_page_loaded(self):
        """
        Checks if the Home page is loaded by trying to find the search input element.
        :return: True if the page is loaded.
        """
        return self.is_element_present(SearchResultsPageLocators.SEARCH_INPUT)

    def return_search_input_text(self):
        """
        Returns the text contained in the search input.
        :return: Text contained in the search input.
        :rtype: string
        """
        return self.return_text_in_input(SearchResultsPageLocators.SEARCH_INPUT)
