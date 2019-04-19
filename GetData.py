import urllib.request
import json
import textwrap
import requests

# with urllib.request.urlopen()
#
# first_json = '''
# {
#     "firstname": "Harold",
#     "lastname": "Velasquez",
#
#     "address": [{
#         "street_address": "5502 Trin Street",
#         "state": "VA",
#         "zipcode": "22310"
#     }],
#     "phone_numbers": ["703-000-000"]
#
# }
# '''
#
# data = json.loads(first_json)
#
# print(data)
#
# for x in data["address"]:
#     del x["zipcode"]
#
# new_json = json.dumps(data, indent=3, sort_keys=True)
# print(new_json)

# main_api = 'http://www.omdbapi.com/?apikey=138e55c9&'
# main_api  = 'http://www.omdbapi.com/?apikey=138e55c9&t=guardians+of+the+galaxy'


# main_api = 'http://www.omdbapi.com/?t=alita?&apikey=138e55c9'


movie_name = input('Enter a movie name: ')
main_api = 'http://www.omdbapi.com/?t='+movie_name+'?&apikey=138e55c9'

url = main_api + urllib.parse.urlencode({})

print(url)

json_data = requests.get(url).json()

# print(json_data)

the_title = json_data['Title']
rating_value = json_data['Ratings'][1]
released_year = json_data['Year']
rated = json_data['Rated']

# print out the information for the movie to the user
print('The title of this movie is: '+the_title)
print('The year this movie came out was: '+released_year)
print('This movie is rated: '+rated)
print('The rating of this movie is: ',rating_value)