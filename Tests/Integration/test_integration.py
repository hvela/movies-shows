#this is a file to practice integration testing
import unittest.mock
from shows_movies import Flix
from Mock import mock


class testAddShow(unittest.TestCase):
    # basic unit tests using mock.patch...
    def test_show_empty(self):
        with mock.patch('builtins.input', return_value=None):
            assert Flix.add_show(self) == None

    def test_show_not_empty(self):
        with mock.patch('builtins.input', return_value=''):
            assert Flix.add_show(self) == ''

    def test_show_value(self):
        with mock.patch('builtins.input', return_value='the office'):
            assert Flix.add_show(self) == 'the office'

    def test_movie_empty(self):
        with mock.patch('builtins.input', return_value=None):
            assert Flix.add_movie(self) == None

    def test_movie_not_empty(self):
        with mock.patch('builtins.input', return_value=''):
            assert Flix.add_movie(self) == ''

    def test_movie_value(self):
        with mock.patch('builtins.input', return_value='Avengers'):
            assert Flix.add_movie(self) == 'Avengers'

