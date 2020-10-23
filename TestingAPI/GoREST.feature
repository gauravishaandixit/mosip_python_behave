# Created by Gaurav Dixit at 23-Oct-20
Feature: Create A User in GOREST DB
  Scenario: Create A User with Valid Data
    Given   An user with access token to acess API
    And     the user wants to create a record with name as "Gaurav Dixit"
    And     the gender of the user is "Male"
    And     the email of the user is "abcdefgh@gmail.com"
    And     the status of the user is "Active"

    When    The user submits the user data in "https://gorest.co.in/public-api/users"

    Then    you must receive a "200" status code

    And     response body must have name as "Gaurav Dixi"
    And     response body must have gender of user as "Male"
    And     response body must have email as "1234@gmail.com"
    And     response body must have status as "active"