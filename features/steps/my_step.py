from app import *
from behave import *
from splinter import Browser
from expects import expect, equal
browser = Browser('flask',app=app)

@given(u'i am alive')
def step_impl(context):
	browser.visit('http://localhost:5000')


@then(u'i know the answer of everything')
def step_impl(context):
	expect(browser.html).to(equal(42))