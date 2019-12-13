from app import *
from behave import *
from splinter import Browser
from expects import expect, equal, match

browser = Browser('flask', app=app)

@given(u'I open the app')
def step_impl(context):
    browser.visit('http://localhost:5000')
    browser.find_by_tag("a").first.click() #it happens whit headless mode

@then(u'i should see "{text}"')
def step_impl(context, text):
    expect(browser.html).to(match(text))
    #browser.quit() #with headless is not necessary


# splinter examples:
# browser.fill('q', 'splinter - python')
# button = browser.find_by_css('.lsb').first
# button.first.click()
# browser.is_text_present('http://splinter.cobrateam.info')
#