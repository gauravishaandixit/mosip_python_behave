from behave import *

use_step_matcher("re")


@given("I am on google search page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("I am on google search page")
    #raise NotImplementedError(u'STEP: Given I am on google search page')


@when("I type text to search")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("I typed text to search")
    #raise NotImplementedError(u'STEP: When I type text to search')


@step("I hit search button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("I hit the search button")
    #raise NotImplementedError(u'STEP: And I hit search button')


@then("I should be on results page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("I am on results page")
    #raise NotImplementedError(u'STEP: Then I should be on results page')