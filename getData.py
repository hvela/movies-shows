import urllib.request
import json
import textwrap
import requests


# new_json = json.dumps(data, indent=3, sort_keys=True)
# print(new_json)

# main_api = 'http://www.omdbapi.com/?apikey=138e55c9&'
# main_api  = 'http://www.omdbapi.com/?apikey=138e55c9&t=guardians+of+the+galaxy'


# main_api = 'http://www.omdbapi.com/?t=alita?&apikey=138e55c9'

# pip install requests --index-url https://pypi.org//simple/

class api:
    def retrieve(self):
        movie_name = input('Enter a movie or show name: ')
        main_api = 'http://www.omdbapi.com/?t='+movie_name+'?&apikey=138e55c9'

        url = main_api + urllib.parse.urlencode({})

        print(url)

        json_data = requests.get(url).json()

        # ensure movie is in api otherwise throw error message
        if 'Error' in json_data:
            print(json_data['Error'])
        else:
            # print(json_data)

            the_title = json_data['Title']
            rating_value = json_data['Ratings'][0]
            released_year = json_data['Year']
            rated = json_data['Rated']

            # print out the information for the movie to the user
            print('\nThe title is: '+the_title)
            print('The year it came out was: '+released_year)
            print('This is rated: '+rated)
            print('Critics rating info: ',rating_value)