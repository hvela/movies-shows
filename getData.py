import urllib.parse
import urllib
import requests
import os
from pprint import pprint

# new_json = json.dumps(data, indent=3, sort_keys=True)
# print(new_json)

# main_api = 'http://www.omdbapi.com/?apikey=13'
# pip install requests --index-url https://pypi.org//simple/


class Api:
    @staticmethod
    def retrieve(motion_picture):
        # movie_name = input('Enter a movie or show name: ')

        key = os.environ['api_key']

        main_api = 'http://www.omdbapi.com/?t='+motion_picture+'?&apikey='+key

        url = main_api + urllib.parse.urlencode({})

        json_data = requests.get(url).json()
        # return url
        # ensure movie is in api otherwise throw error message
        if 'Error' in json_data:
            # print(json_data['Error'])
            return json_data['Error']

        else:
            # print(json_data)
            the_title = json_data['Title']
            rating_value = json_data['Ratings'][0]
            released_year = json_data['Year']
            rated = json_data['Rated']

            the_data = the_title, rating_value, released_year, rated
            return the_data
        #     # print out the information for the movie to the user
        #     print('\nThe title is: '+the_title)
        #     print('The year it came out was: '+released_year)
        #     print('This is rated: '+rated)
        #     print('Critics rating info: ', rating_value)
        #