import requests
import json

token = 'd1324f43ebb6dbcc7b29d6148afec54a'

response = requests.post('https://pokemonbattle.me:5000/pokemons',
headers = {'Content-Type': 'application/json',
          'trainer_token': token},
json = {
    "name": "Forsik",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"

})

print(response.text)

pokemon_id = response.json()['id']

response_change = requests.put('https://pokemonbattle.me:5000/pokemons',
headers = {'Content-Type': 'application/json',
           'trainer_token': token},
json = {
    "pokemon_id": pokemon_id,
    "name": "Rezeda",
    "photo": "https://e7.pngegg.com/pngimages/244/693/png-clipart-pikachu-pokemon-x-and-y-illustration-pikachu-mammal-cartoon.png"
})

print(response_change.text)

response = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball',
headers = {'Content-Type': 'application/json',
          'trainer_token': token},
json = {
    "pokemon_id": "3140"
})

print(response.text)






