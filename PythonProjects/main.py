import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5b9b1ce40b1e31309786700a4e8b0e30'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
body_create = {
    "name": "Эврика",
    "photo_id": 77
}

body_put = {
    
    "pokemon_id": "234270",
    "name": "New Name2222",
    "photo_id": 8
}

body_add_poketball = {
    
    "pokemon_id": "296429"
}


'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.json)
message = response_create.json()['message']
print(message)'''


'''response_put = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_put)
print(response_put.json)
message = response_put.json()['message']
print(message)'''

response_add_poketball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_poketball)
print(response_add_poketball.json)
message = response_add_poketball.json()['message']
print(message)
