from selene.support.shared import browser
from selene import have


def test_local_links_number():
    browser.open('https://www.ecosia.org/')

    browser.element('[name=q]').type('yashaka selene').press_enter()
    browser.all('.result').first.click()

    browser.all('[href="/yashaka/selene"]').should(have.size(3))