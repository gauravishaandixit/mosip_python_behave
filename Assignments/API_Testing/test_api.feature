# Created by Gaurav Dixit at 24-Oct-20
Feature: Create A User in mysql database
  Scenario: Create A User with Valid Data
    Given   An admin with access token to API
    And     the admin wants to add an user with first name as "Yogesh"
    And     the user has a last name of "Meghnani"
    And     the gender is "male"
    And     the date of the birth is "1997-07-05"
    And     the email of the user is "abcdefghij@gmail.com"
    And     the phone number of the user is "+911234"
    And     the website of the user is "https://bit.ly/IqT6zt"
    And     the address is "india"
    And     the user status is "active"
    When    user submits the user data in "https://gorest.co.in/public-api/users"

    Then    you should receive a "200" status code

    And     response body must have first name as "Yogesh"
    And     response body must have last name as "Meghnani"
    And     response body must have gender as "male"
    And     response body must have date of birth as "1997-07-05"
    And     response body must have email as "abcdefghij@gmail.com"
    And     response body must have phone number as "+911234"
    And     response body must have website as "https://bit.ly/IqT6zt"
    And     response body must have address as "india"
    And     response body must have user status as "active"