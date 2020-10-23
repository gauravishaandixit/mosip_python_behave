# Created by Gaurav Dixit at 23-Oct-20
Feature: Google Search Test # Enter feature name here
  # Enter feature description here

  Scenario: Test goolge search # Enter scenario name here
    # Enter steps here
    Given I am on google search page
    When I type text to search
    And I hit search button
    Then I should be on results page