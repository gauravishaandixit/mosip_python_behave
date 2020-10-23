from behave import *
import requests
use_step_matcher("re")


@given("An user with access token to API")
def setAccessToken(context):
    print("setAccessToken")
    context.header = {"Authorization" : "Bearer "+"aaabd17656571d7a3ddde9c8f3cb9c9cc7ff23d9dd5cbe2cb1f9b093f71e768e"}


@step('the user wants to create a record with first name as "Gaurav"')
def setFirstName(context):
    """
    :type context: behave.runner.Context
    """
    print("setFirstName")
    context.request_body = {"first_name" : "Gaurav"}


@step('the user record has a last name of "Dixit"')
def setLastName(context):
    """
    :type context: behave.runner.Context
    """
    print("setLastName")
    context.request_body['last_name'] = 'Dixit'
    context.request_body['name'] = 'Gaurav Dixit'

@step('the gender is "male"')
def setGender(context):
    """
    :type context: behave.runner.Context
    """
    print("setGender")
    context.request_body['gender'] = 'Male'


@step('date of birth is "1997-07-05"')
def setDOB(context):
    """
    :type context: behave.runner.Context
    """
    print("setDOB")
    context.request_body['dob'] = '1997-07-05'


@step('an email of "abcdef@gmail\.com"')
def setEmail(context):
    """
    :type context: behave.runner.Context
    """
    print("setEmail")
    context.request_body['email'] = 'abcdef@gmail.com'


@step('a phone number of "\+911234"')
def setPhoneNumber(context):
    """
    :type context: behave.runner.Context
    """
    print("setPhoneNumber")
    context.request_body['phone'] = "+911234"


@step('a website of "https://bit\.ly/IqT6zt"')
def setWebsite(context):
    """
    :type context: behave.runner.Context
    """
    print("setWebsite")
    context.request_body['website'] = "https://bit.ly/IqT6zt"


@step('the address is "Kathkuiyan, Padrauna, Kushinagar, UP"')
def setAddress(context):
    """
    :type context: behave.runner.Context
    """
    print("setAddress")
    context.request_body['address'] = 'Kathkuiyan, Padrauna, Kushinagar, UP'


@step('the user status is "active"')
def setStatus(context):
    """
    :type context: behave.runner.Context
    """
    print("setStatus")
    context.request_body['status'] = 'Active'


@when('user submits the user data in "https://gorest\.co\.in/public-api/users"')
def step_impl(context):
    print(context.header)
    print(context.request_body)
    response = requests.post("https://gorest.co.in/public-api/users", headers = context.header,
                             json = context.request_body)
    print("Submit the Data")
    print(response.json())
    context.response_body = response.json()
    context.status_code = response.status_code


@then('you should receive a "200" status code')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.status_code == 200


@step('response body must have first name as "Gaurav"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """



@step('response body must have last name as "Dixit"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """


@step('response body must have gender  as "male"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """


@step('response body must have date of birth as "1997-07-05"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """


@step('response body must have email as "dixitgaurav97@gmail\.com"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """


@step('response body must have phone number as "\+918354801670"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """


@step('response body must have website as "https://bit\.ly/IqT6zt"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """


@step('response body must have address as "Kathkuiyan, Padrauna, Kushinagar, UP"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """


@step('response body must have user status as "active"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
