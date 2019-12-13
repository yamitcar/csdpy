from app import *
from behave import *
from splinter import Browser
from expects import expect, equal, match

browser = Browser()

@given(u'I open the app')
def step_impl(context):
    browser.visit('http://localhost:5000')

@then(u'i should see "{text}"')
def step_impl(context, text):
    expect(browser.html).to(match(text))
    browser.quit()