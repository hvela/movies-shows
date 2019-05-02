#this is a file to practice unit testing
import unittest.mock
from unittest.mock import patch
from ShowsAndMovies import Flix

# get_input will return 'yes' during this test
class TestAddMovie(unittest.TestCase):
    @patch('Flix.add_show', return_value='True')
    def test_empty_show(self):
        # test_value = Flix.add_show(self)
        self.assertTrue(self, True)

