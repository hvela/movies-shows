#this is a file to practice unit testing
import unittest.mock
from unittest.mock import patch, Mock
from shows_movies import Flix


import mock

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
    #         self.assertIsNotNone('builtins.input', 'the office')

class testAddMovie(unittest.TestCase):
    # basic unit tests using mock.patch...
    def test_movie_empty(self):
        with mock.patch('builtins.input', return_value=None):
            assert Flix.add_movie(self) == None

    def test_movie_not_empty(self):
        with mock.patch('builtins.input', return_value=''):
            assert Flix.add_movie(self) == ''

    def test_movie_value(self):
        with mock.patch('builtins.input', return_value='Avengers'):
            assert Flix.add_movie(self) == 'Avengers'
    #         self.assertIsNotNone('builtins.input', 'the office')

    # @mock.patch('shows_movies.Flix')
    # def test_show_not(mock_add_show):
    #         value = None
    #         mock_add_show.return_value = None
    #
    #         #assert
    #         assert None, value
    #         # self.assertIsNotNone('builtins.input', 'the office')


#
# class testAddShow(unittest.TestCase):
        # this input should return not empty
#         patch.object(__builtin__, 'add_show')
#         def test_show_not_empty(self, mock_add_show):
            # mock_shows = Mock()
            # Flix.add_show(mock_shows, "a show..")
            # self.assertIsNotNone()
#             mock_add_show.return_value = 'f'
#             self.assertEqual(add_show(), 'f')
            # test_value = return_value
            # self.assertIsNotNone(Flix.add_show(), not None)
            # print('fsdsfadfa',mock_shows)

        #
        # def test_show_not_empty(self, mock_add_show):
        #     original_raw_input = __builtins__.raw_input
        #     __builtins)__.raw_input = original_raw_input
        #



        #
        #
        # def test_show_empty(self):
        #     empty = Flix.add_show(self)
        #     self.assertIsNone(empty)





# # get_input will return 'yes' during this test
# class TestAddMovie(unittest.TestCase):
#     @patch('Flix.add_show', return_value='True')
#     def test_empty_show(self):
#         # test_value = Flix.add_show(self)
#         self.assertTrue(self, True)



# def yes_or_no():
#     answer = input("Do you want to quit? > ")
#     if answer == "yes":
#         return("Quitter!")
#     elif answer == "no":
#         return("Awesome!")
#     else:
#         return("BANG!")
#
#
# def test_quitting():
#
#     with mock.patch('builtins.input', return_value="yes"):
#         assert yes_or_no() == "Quitter!"
#
#     with mock.patch('builtins.input', return_value="no"):
#         assert yes_or_no() == "Awesome!"
#
#     with mock.patch('builtins.input', return_value="fd"):
#         assert yes_or_no() == "BANG!"
