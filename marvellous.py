import json
import requests
from requests.api import get
from requests.models import Response
from marvel import Marvel
from decouple import config


API_PUBLIC = config('PUBLIC')
API_PRIVATE = config('PRIVATE')
API_HASH = config('HASH')

response = requests.get(
    'http://gateway.marvel.com/v1/public/characters?ts=1629289209&apikey=API_PUBLIC&hash=API_HASH')

if response.status_code == 200:
    print("The request was a success!")
elif response.status_code == 404:

    print(response.json())
