# Created by Gaurav Dixit at 23-Oct-20
Feature: Create A User in GOREST DB
  Scenario: Create A User with Valid Data
    Given   An user with access token to API
    And     the user wants to create a record with first name as "Gaurav"
    And     the user record has a last name of "Dixit"
    And     the gender is "male"
    And     date of birth is "1997-07-05"
    And     an email of "dixitgaurav97@gmail.com"
    And     a phone number of "+918354801670"
    And     a website of "https://bit.ly/IqT6zt"
    And     the address is "Kathkuiyan, Padrauna, Kushinagar, UP"
    And     the user status is "active"
    When    user submits the user data in "https://gorest.co.in/public-api/users"

    Then    you should receive a "200" status code

    And     response body must have first name as "Gaurav"
    And     response body must have last name as "Dixit"
    And     response body must have gender  as "male"
    And     response body must have date of birth as "1997-07-05"
    And     response body must have email as "dixitgaurav97@gmail.com"
    And     response body must have phone number as "+918354801670"
    And     response body must have website as "https://bit.ly/IqT6zt"
    And     response body must have address as "Kathkuiyan, Padrauna, Kushinagar, UP"
    And     response body must have user status as "active"