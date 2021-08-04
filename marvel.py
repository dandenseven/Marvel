import requests


# url = 'https://gateway.marvel.com/'
# data = requests.get(url).json

response = requests.get(
    'https://developer.marvel.com/docs#!/public/getComicCharacterCollection_get_8?ts=1&apikey=df9907985e1fe414d45b38743f3d5e989a27b126&hash=55952202b6ba744d18c4da43726a2c10')
if response.status_code == 200:
    print("The request was a success!")
elif response.status_code == 404:
    print("Result not found!")
