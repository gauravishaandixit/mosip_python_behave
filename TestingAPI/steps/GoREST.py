from behave import *
import requests
use_step_matcher("re")


@given("An user with access token to acess API")
def setAccessToken(context):
    print("setAccessToken")
    context.header = {"Authorization": "Bearer "+"aaabd17656571d7a3ddde9c8f3cb9c9cc7ff23d9dd5cbe2cb1f9b093f71e768e"}


@step('the user wants to create a record with name as "Gaurav Dixit"')
def setName(context):
    print("setName")
    context.request_body = {"name": "Gaurav Dixit"}


@step('the gender of the user is "Male"')
def setGender(context):
    print("setGender")
    context.request_body['gender'] = 'Male'


@step('the email of the user is "abcdefgh@gmail.com"')
def setEmail(context):
    print("setEmail")
    context.request_body['email'] = 'abcdefgh7@gmail.com'


@step('the status of the user is "Active"')
def setStatus(context):
    print("setStatus")
    context.request_body['status'] = 'Active'


@when('The user submits the user data in "https://gorest.co.in/public-api/users"')
def postData(context):
    response = requests.post("https://gorest.co.in/public-api/users", headers=context.header,
                             json=context.request_body)
    print("Submit the Data")
    print(response.status_code)
    context.response_body = response.json()
    context.status_code = response.status_code


@then('you must receive a "200" status code')
def checkStatusCode(context):
    assert context.status_code == 200


@step('response body must have name as "Gaurav Dixi"')
def checkName(context):
    print("checkName")
    assert context.response_body['data']['name'] == context.request_body['name']


@step('response body must have gender of user as "Male"')
def checkGender(context):
    print("checkGender")
    assert context.response_body['data']['gender'] == context.request_body['gender']


@step('response body must have email as "1234@gmail.com"')
def checkEmail(context):
    print("checkEmail")
    assert context.response_body['data']['email'] == context.request_body['email']


@step('response body must have status as "active"')
def checkStatus(context):
    print("checkStatus")
    assert context.response_body['data']['status'] == context.request_body['status']
