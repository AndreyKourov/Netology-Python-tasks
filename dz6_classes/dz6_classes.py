class Pet:
    name = ''
    weight = 0
    food = ''
    voice = ''
    action = ''
    give = 0
    def full_eat(self, eated):
        if self.action == 'egg':
            self.give += eated * 0.5
            self.weight += eated * 0.1
        elif self.action == 'milk':
            self.give += eated * 0.5
            self.weight += eated * 0.1
        elif self.action == 'wool':
            self.give += eated * 0.5
            self.weight += eated * 0.1


goose_grey = Pet()
goose_grey.name = 'Grey'
goose_grey.weight = 10
goose_grey.food = 'corn'
goose_grey.voice = 'quack'
goose_grey.action = 'egg'
goose_grey.full_eat(10)
print(goose_grey.__dict__)

cow = Pet()
cow.name = 'Manka'
cow.weight = 150
cow.food = 'grass'
cow.voice = 'moo'
cow.action = 'milk'
cow.full_eat(10)
print(cow.__dict__)

pet_ist = {cow.name : cow.weight, goose_grey.name : goose_grey.weight}

class Heavy:
    def heaviest_animal(self, animal):
        print('Смма массы всех животных :', end=' ')
        print(sum(animal.values()))
        # print(max(animal.values()))
        for key_animal, val_animal in animal.items():
            if val_animal == max(animal.values()):
                print(f'Самое тяжелое животное : {key_animal} - {val_animal}')

pet_heavy = Heavy()
pet_heavy.heaviest_animal(pet_ist)


