import requests
import json

token = 'd1324f43ebb6dbcc7b29d6148afec54a'

response = requests.post('https://pokemonbattle.me:5000/pokemons/kill',
headers = {'Content-Type': 'application/json',
          'trainer_token': token},
json = {
    "pokemon_id": "3151"
})

print(response.text)



