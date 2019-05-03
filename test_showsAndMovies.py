#this is a file to practice unit testing
import unittest.mock
from unittest.mock import patch
from shows_movies import Flix


class testAddShow(unittest.TestCase):
        def test_show_not_empty(self):
            test_value = Flix.add_show(self)
            self.assertIsNotNone(test_value)

        def test_show_empty(self):
            empty = Flix.add_show(self)
            self.assertIsNone(empty)





# # get_input will return 'yes' during this test
# class TestAddMovie(unittest.TestCase):
#     @patch('Flix.add_show', return_value='True')
#     def test_empty_show(self):
#         # test_value = Flix.add_show(self)
#         self.assertTrue(self, True)

