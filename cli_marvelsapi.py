from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json, Separator, style_from_dict, Token
import json
import requests
from requests.models import Response


style = style_from_dict({
    Token.QuestionMark: '#FF9D00 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#5F819D bold',
    Token.Separator: '#cc5454',
    # Token.Separator: '#6C6C6C',
    Token.QuestionMark: '#FF9D00 bold',
    Token.Selected: '',
    Token.Pointer: '#FF9D00 bold',
    Token.Instruction: '',  # default
    Token.Question: '',

})


class MarvelComics(object):
    def __init__(self, comics):
        self.comics = comics

    def get_new_characters(self):
        characters = self.comics
        print(characters)
        if characters:
            url = 'https://developer.marvel.com/docs#!/public/getComicCharacterCollection_get_8?ts=1&apikey=df9907985e1fe414d45b38743f3d5e989a27b126&hash=55952202b6ba744d18c4da43726a2c10='+characters+'&pageSize=10'

            call = requests.get(url)
            print('status:', call.status_code)
            response_data = call.json()

            marvel_characters = response_data['characters']

        y = marvel_characters
        for character in y:
            character_collection = {}
            result_characters = {'id': character['id'], 'Name': character['name'],
                                 'Description': character['description']}
            character_collection.update(result_characters)
            print(character_collection, "\n")
            return character_collection


if __name__ == '__main__':
    print('Welcome to Marvel Comics')
    question = [
        {
            'type': 'string',
            'name': 'comic_heroes',
            'message': 'who is your favorite comic book character',
            'choices': ['comics', 'stories', 'events', 'series']
        }
    ]

    response = prompt(question, style=style)

    user_response = response['comic_heroes']
    user_response_obj = MarvelComics(user_response)
    print(user_response_obj.get_new_characters())
