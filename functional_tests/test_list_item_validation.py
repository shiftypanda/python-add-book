from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest

MAX_WAIT = 10

"""
 If running test on staging server use
 STAGING_SERVER=superlists-staging.sendiary.org ./manage.py test functional_tests --failfast
"""

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty liste item. SHe hits Enter on the empty input box

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank

        # SHe tries again with some text for the item, which works now

        # Perversely, she now decides to submit a second blank list item

        # SHee receives a similar warnign on the list page

        # And she can correct it by filling some text in
        self.fail('write me!')
