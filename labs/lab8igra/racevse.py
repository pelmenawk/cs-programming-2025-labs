from random import *

weapons = ["Меч", "Кинжал", "Лук", "Копье", "Сковородочаки"]
armor = ["Латная броня", "Кольчуга", "Кожаная броня"]
useables = ["Малое зелье исцеления", "Среднее зелье исцеления", "Большое зелье исцеления"]

inventory = {"weapon":"", "armor":""}
for i in range(1,6): inventory [str(i)]=""

class Character:
    def __init__(self):
        print('Who are you?')
        name = input("> ")
        print("Выберите расу:")
        print("1 - Человек")
        print("2 - Эльф")
        print("3 - Дворф")
        race = input('> ')
        print("Ваш персонаж создан!")
        self.name = name
        self.race = race
        self.max_hp = 0
        self.now_hp = 0
        self.strength = 0
        self.agility = 0
        self.defence = 0
        self.money = 0

    def char_stats(self):
        if self.race == "1":
            self.max_hp = randint(90,110)
            self.strength = randint(4,8)
            self.agility = randint(5,10)
            self.defence = randint(3,5)
            height = randint(150,200)
            weight = randint(60,90)
            if weight < 70 and height < 160:
                self.strength -= 1
                self.agility += 1
            elif weight > 80 and height > 190:
                self.strength += 1
                self.agility -= 1
        elif self.race == "2":
            self.max_hp = randint(70,90)
            self.strength = randint(4,8)
            self.agility = randint(8,14)
            self.defence = randint(3,5)
            height = randint(175,210)
            weight = randint(40,70)
            if weight < 50 and height < 185:
                self.strength -= 1
                self.agility += 2
            elif weight > 60 and height > 200:
                self.strength += 1
                self.agility -= 1
        elif self.race == "3":
            self.max_hp = randint(100,130)
            self.strength = randint(5,10)
            self.agility = randint(3,6)
            self.defence = randint(6,10)
            height = randint(100,130)
            weight = randint(70,100)
            if weight < 80 and height < 110:
                self.strength -= 1
                self.agility += 1
            elif weight > 90 and height > 120:
                self.strength += 2
                self.agility -= 1
        else:
            print("Такой расы нет!")
        self.now_hp = self.max_hp
        return self.max_hp, self.strength, self.agility, self.defence, height, weight
    
    def show_stats(self,lvl,exp,req_exp):
        print('ВАШ ПЕРСОНАЖ:')
        print('---------')
        print(f'Name:{self.name}')
        print('---------')
        print(f'LVL:{lvl}')
        print(f'EXP:{exp}\{req_exp}')
        print('---------')
        print(f'HP:{self.now_hp}\{self.max_hp}')
        print(f'STR:{self.strength}')
        print(f'AGI:{self.agility}')
        print(f'DEF:{self.defence}') 
        print('---------')

    def up_stats(self):
        print("Выберите характеристику:")
        print("1 - +2 к HP")
        print("2 - +1 к атаке")
        print("3 - +1 к ловкости")
        print("4 - +1 к броне")
        num_up = input('> ')
        if num_up == "1":
            self.max_hp += 2
        elif num_up == "2":
            self.strength += 1
        elif num_up == "3":
            self.agility += 1
        elif num_up == "4":
            self.defence += 1
        else:
            print("Такой опции нет")

    def show_inventory(self):
        global inventory
        print(f"weapon - {inventory['weapon']}\narmor - {inventory['armor']}")
        for i in range(1,6):
            print(f"{i} - {inventory[str(i)]}")

    def inventory_use(self):
        for i in range(1,6):
            if inventory[str(i)] == '':
                pass
            else:
                print("Выберите предмет, который будете использовать:")
                for j in range(1,6):
                    if inventory[str(j)] == '':
                        pass
                    else:
                        print(f'{j} - {inventory[str(j)]}')
                choosen_num = input('> ')
                print('Что вы хотите с ним сделать?')

                # Для оружия
                if any(item in inventory[choosen_num] for item in weapons):
                    print('1 - Переложить  в основную руку\n2 - Выкинуть\n3 - Ничего')
                    choosen_num1 = input('> ')
                    if choosen_num1 == '1':
                        inventory['Weapon'] = inventory[choosen_num]
                        if 'Меч' in inventory['Weapon']:
                            self.strenght += 3 + int(inventory['Weapon'][4:][:1])
                        elif 'Кинжал' in inventory['Weapon']:
                            self.strenght += 1 + int(inventory['Weapon'][7:][:1])
                            self.agility += 2 + int(inventory['Weapon'][7:][:1])
                        elif 'Лук' in inventory['Weapon']:
                            self.agility += 3 + int(inventory['Weapon'][4:][:1])
                        elif 'Копье' in inventory['Weapon']:
                            self.strenght += 2 + int(inventory['Weapon'][6:][:1])
                            self.defence += 1 + int(inventory['Weapon'][6:][:1])
                        elif 'Сковородочаки' in inventory['Weapon']:
                            self.agility += 2 + int(inventory['Weapon'][14:][:1])
                            self.defence += 2 + int(inventory['Weapon'][14:][:1])
                        inventory[choosen_num] = ''
                    elif choosen_num1 == '2':
                        inventory[choosen_num] = ''
                    elif choosen_num1 == '3':
                        pass
                
                # Для брони
                elif any(item in inventory[choosen_num] for item in armor):
                    print('1 - Надеть\n2 - Выкинуть\n3 - Ничего')
                    choosen_num1 = input('> ')
                    if choosen_num1 == '1':
                        inventory['Armor'] = inventory[choosen_num]
                        if 'Латная броня' in inventory['Armor']:
                            self.defence += 5 + int(inventory['Armor'][13:][:1])
                        elif 'Кольчуга' in inventory['Armor']:
                            self.defence += 3 + int(inventory['Armor'][9:][:1])
                            self.agility += 1 + int(inventory['Armor'][9:][:1])
                        elif 'Кожаная броня' in inventory['Armor']:
                            self.defence += 2 + int(inventory['Armor'][15:][:1])
                            self.agility += 3 + int(inventory['Armor'][15:][:1])
                        inventory[choosen_num] = ''
                    elif choosen_num1 == '2':
                        inventory[choosen_num] = ''
                    elif choosen_num1 == '3':
                        pass
                
                # Для расходников
                elif inventory[choosen_num] in useables:
                    print('1 - Выпить\n2 - Выкинуть\n3 - Ничего')
                    choosen_num1 = input('> ')
                    if choosen_num1 == '1':
                        if inventory[choosen_num] == 'Зелье здоровья(Маленькое)':
                            self.cur_hp += 10
                        elif inventory[choosen_num] == 'Зелье здоровья(Среднее)':
                            self.cur_hp += 25
                        elif inventory[choosen_num] == 'Зелье здоровья(Большое)':
                            self.cur_hp += 70
                        if self.cur_hp > self.max_hp:
                            self.cur_hp = self.max_hp
                        inventory[choosen_num] = ''
                    elif choosen_num1 == '2':
                        inventory[choosen_num] = ''
                    elif choosen_num1 == '3':
                        pass

                    elif inventory[choosen_num] == '':
                        print('Здесь нет предмета!')
                        break
        else:
            print('У вас в инвентаре ничего нет')