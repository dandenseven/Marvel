import json
import requests


# url = 'https://gateway.marvel.com/'
# data = requests.get(url).json
# class MarvelComics(object):
#     def __init__(self, comics):
#         self.comics = comics

#     def get_new_characters(self):
#         characters = self.comics
#         print(characters)
#         if characters:
#             url = ('https://developer.marvel.com/docs#!/public/getComicCharacterCollection_get_8?ts=1&apikey=df9907985e1fe414d45b38743f3d5e989a27b126&hash=55952202b6ba744d18c4da43726a2c10')

#             response = requests.get(url)
#             data = response.json()

#             marvel_characters = data['characters']

#         y = marvel_characters
#         for character in y:
#             character_collection = {}
#             result_characters = request.json.get{'id': character['id'], 'Name': character['name'],
#                                                  'Description': character['description']}
#             character_collection.update(result_characters)
#             print(character_collection)
#             return jsonify({"success": True}), 200
#             pass
#             except Exception as e:
#             return f"An Error Occured: {e}"


# result_characters = {'id': character['id'], 'Name': character['name'],
#                      'Description': character['description']}
# query = {'id': character['id'], 'name': 'cyclops'}
response = requests.get(
    'https://developer.marvel.com/docs#!/public/getComicCharacterCollection_get_8?ts=1&apikey=df9907985e1fe414d45b38743f3d5e989a27b126&hash=55952202b6ba744d18c4da43726a2c10')
if response.status_code == 200:
    print("The request was a success!")
elif response.status_code == 404:

    print(response.json())
