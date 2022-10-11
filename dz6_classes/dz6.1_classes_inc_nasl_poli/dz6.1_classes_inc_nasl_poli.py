class Pet:
    def __init__(self, name, weight, voise):
        self.name = name
        self.weight = weight
        self.voise = voise

    def eat(self, food):
            self.weight += food * 0.1

# for key_pet, val_pet in Pet.__dict__.items():
list_pet = ['Grey', 'Horns', 'Curly']
animal_pet = ''
pet_dict = {}
# oop = []

for parent_list_pet in list_pet:
    # animal_pet = Pet(parent_list_pet, 10, 'Noize')
    # oop = [Pet(parent_list_pet, 10, 'Noize')]
    print(animal_pet.__dict__)

# print(pet_dict['Grey'])

# print(animal_pet)

# oop[0].name = 'EEE'
# print(oop[0].name)

"""
list_animals = {
    'bird' : ['Grey', 8, 'GaGaGa' ],
    'milk' : ['Horns', 50, 'Mee'],
    'wool' : ['Curly', 45, 'BeBeBe']
}
"""
"""
for key_list_animals in list_animals:
    for value_list_animals in list_animals[key_list_animals]:
        val = value_list_animals
    f'{key_list_animals} = {Pet}({val})'
print(wool.__dict__)
# for key_pet, val_pet in Pet.__dict__.items():
"""


class Birds(Pet):
    def __init__(self, name, weight, voise):
        self.feed = ''
        self.amount_feed = 0
        super().__init__(name, weight, voise)
    def eggs(self):
        if self.feed == 'corn':
            print(f'Give Eggs {self.amount_feed}')
        else:
            print('Not good feed')


guse = Birds('White', 10, 'GaGa')
guse.eat(10)
guse.feed = 'corn'
guse.amount_feed = 1
print(guse.__dict__)
guse.eggs()


class Milk_Pet(Pet):
    def __init__(self, name, weight, voise):
        self.feed = ''
        self.amount_feed = 0
        super().__init__(name, weight, voise)
    def milk(self):
        if self.feed == 'grass':
            print(f'Give Milk {self.amount_feed}')
        else:
            print('Not good feed')

cow = Milk_Pet('Manyka', 100, 'Moo')
cow.eat(10)
cow.feed = 'grass'
cow.amount_feed = 10
print(cow.__dict__)
cow.milk()

class Wool_Pet(Pet):
    def __init__(self, name, weight, voise):
        self.feed = ''
        self.amount_feed = 0
        super().__init__(name, weight, voise)

    def wool(self):
        if self.feed == 'grass':
            print(f'Give Wool {self.amount_feed}')
        else:
            print('Not good feed')


sheep = Wool_Pet('Barashik', 100, 'Bee')
sheep.eat(10)
sheep.feed = 'grass'
sheep.amount_feed = 10
print(sheep.__dict__)
sheep.wool()

"""
for key, val in guse.__dict__.items():
    print(val)
"""
for key in guse.__dict__:
    print(guse.__dict__[key])