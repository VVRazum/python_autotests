import requests
import json

token = '253aad64ae2ff7a7390f5362092b41a7'
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
       "name": "PeeMon",
    "photo": "https://www.pngkey.com/png/detail/189-1892866_http-vignette1-wikia-nocookie-net-silent-images-portable.png"
})

print(response.text)

response = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id" : 1379,
       "name": "PeeMonNew",
    "photo": ""
})

print(response.text)

response = requests.post('https://pokemonbattle.me:5000/trainers/addPokebol', headers={'trainer_token' : token}, json={
    "pokemon_id" : 1379
      })

print(response.text)