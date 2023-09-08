from requests import get


response = get('https://pokeapi.co/api/v2/pokemon/ditto/')

print(response.headers [ 'Content-Type' ])
if response.ok:
  current_poke_data = response.json() 
else:
    print(f'Bad request {response.status_code}, please choose valid pokemon')

from IPython.display import Image

display(image('https://pokeapi.co/api/v2/pokemon/132/', 75))


class Pokemon():
    
    def _init_(self, pokemon):
        self.name = pokemon
        self.weight = None
        self.abilities = []
        self.types = []
        self.sprite = None
        self.poke_api_call()
        
    def _repr_(self):
        return f'<Pokemon: {self.name}>'
    
    def poke_api_call(self):
        while True:
            res = get(f'https://pokeapi.co/api/v2/pokemon/{self.name}')
            if res.ok:
                data = res.json()
                self.name = data['name']
                self.weight = data['weight']
                self.abilities = [ability['ability']['name'] for ability in data['abilities']]
                self.types = [poke_type['type']['name'] for poke_type in data['types']]
                self.sprite = self.get_sprite(data)
                break
            else:
                print(f'Invalid Request, status code {res.status_code}, Please enter valid pokemon')
                self.update_pokemon()
            
    def update_pokemon(self):
        self.name = input('Pokemon name: ')
        
    def get_sprite(self, data):
        animated = data['sprites']['versions']['generation-v']['black-white']['animated']['front_default']
        return animated if animated else data['sprites']['front_default']
    
    def display_img(self):
        display(Image(self.sprite, width = 75))
        
    def display_info(self):
        print(f'{self.name} Weight: {self.weight}')
        print('Types: ')
        for poke_type in self.types:
            print(poke_type)
        print('Abilities: ')
        for ability in self.abilities:
            print(ability)
        self.display_img()
        
psyduck = Pokemon('pikachu')

# psyduck.poke_api_call()
print(psyduck)
print(psyduck.abilities)
print(psyduck.types)
psyduck.display_img()