from behave import *

use_step_matcher("re")


@given("An admin with access token to API")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """



@step('the admin wants to add an user with first name as "Yogesh"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context = {'first_name' : 'Yogesh'}


@step('the user has a last name of "Meghnani"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """



@step('the gender is "male"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And     the gender is "male"')


@step('the date of the birth is "1997-07-05"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And     the date of the birth is "1997-07-05"')


@step('the email of the user is "abcdefghij@gmail\.com"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And     the email of the user is "abcdefghij@gmail.com"')


@step('the phone number of the user is "\+911234"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And     the phone number of the user is "+911234"')


@step('the website of the user is "https://bit\.ly/IqT6zt"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And     the website of the user is "https://bit.ly/IqT6zt"')


@step('the address is "india"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And     the address is "india"')


@step('the user status is "active"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And     the user status is "active"')


@when('user submits the user data in "https://gorest\.co\.in/public-api/users"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When    user submits the user data in "https://gorest.co.in/public-api/users"')


@then('you should receive a "200" status code')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then    you should receive a "200" status code')


@step('response body must have first name as "Yogesh"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And     response body must have first name as "Yogesh"')


@step('response body must have last name as "Meghnani"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And     response body must have last name as "Meghnani"')


@step('response body must have gender as "male"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And     response body must have gender as "male"')


@step('response body must have date of birth as "1997-07-05"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And     response body must have date of birth as "1997-07-05"')


@step('response body must have email as "abcdefghij@gmail\.com"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And     response body must have email as "abcdefghij@gmail.com"')


@step('response body must have phone number as "\+911234"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And     response body must have phone number as "+911234"')


@step('response body must have website as "https://bit\.ly/IqT6zt"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And     response body must have website as "https://bit.ly/IqT6zt"')


@step('response body must have address as "india"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And     response body must have address as "india"')


@step('response body must have user status as "active"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And     response body must have user status as "active"')