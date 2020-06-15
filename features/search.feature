Feature: Page Search

  Scenario: Search from home page.
    Given I am on the home page
    When I type "Python" in the search bar and press enter
    Then The search results page shows me a list of different websites related with the word "Python"
