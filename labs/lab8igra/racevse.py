from random import *
from mobs import *

weapons = ["Меч", "Кинжал", "Рогатка", "Посох", "Сковородочаки"]
armor = ["Крутая броня", "Кольчужная броня", "Тканевая броня"]
useables = ["Малое зелье исцеления", "Среднее зелье исцеления", "Большое зелье исцеления"]

inventory = {"weapon":"", "armor":""}
for i in range(1,6): inventory [str(i)]=""

class Character:
    def __init__(self):
        print('Ваше имя:')
        self.name = input("> ")
        self.race =""
        self.max_hp = 0
        self.now_hp = 0
        self.strength = 0
        self.agility = 0
        self.defence = 0
        self.money = 0
        self.room = 0
        self.floor = 0
        self.req_exp = 5
        self.exp = 0
        self.lvl = 1
        self.stat_point = 0
        self.weight = 0
        self.height = 0

    #Статы нашего персонажа

    def char_stats(self):
        print("Ваша раса:")
        print("1 - Человек")
        print("2 - Эльф")
        print("3 - Дворф")
        self.race = input('> ')
        
        if self.race == "1":

            self.max_hp = randint(70,90)
            self.strength = randint(4,8)
            self.agility = randint(5,10)
            self.defence = randint(1,3)
            self.height = randint(150,200)
            self.weight = randint(60,90)
            
            if self.weight < 70 and self.height < 160:
                self.strength -= 1
                self.agility += 1
            
            elif self.weight > 80 and self.height > 190:
                self.strength += 1
                self.agility -= 1
            
            print("Ваш персонаж создан!")
        
        elif self.race == "2":

            self.max_hp = randint(60,80)
            self.strength = randint(4,8)
            self.agility = randint(8,14)
            self.defence = randint(1,3)
            self.height = randint(175,210)
            self.weight = randint(40,70)
            
            if self.weight < 50 and self.height < 185:
                self.strength -= 1
                self.agility += 2
            
            elif self.weight > 60 and self.height > 200:
                self.strength += 1
                self.agility -= 1
            
            print("Ваш персонаж создан!")
        
        elif self.race == "3":
            self.max_hp = randint(100,130)
            self.strength = randint(5,10)
            self.agility = randint(3,6)
            self.defence = randint(4,6)
            self.height = randint(100,130)
            self.weight = randint(70,100)
            
            if self.weight < 80 and self.height < 110:
                self.strength -= 1
                self.agility += 1
            
            elif self.weight > 90 and self.height > 120:
                self.strength += 2
                self.agility -= 1
            
            print("Ваш персонаж создан!")
        
        else:
            print("Такой расы нет!")
        
        self.now_hp = self.max_hp
        
        return self.max_hp, self.strength, self.agility, self.defence, self.weight, self.height
    
    #Показываем статы

    def show_stats(self):
        print('ВАШ ПЕРСОНАЖ:')
        print('---------')
        print(f'Name:{self.name}')
        print('---------')
        print(f'LVL:{self.lvl}')
        print(f'EXP:{self.exp}\{self.req_exp}')
        print('---------')
        print(f'Здоровье:{self.now_hp}\{self.max_hp}')
        print(f'АТК:{self.strength}')
        print(f'Ловкость:{self.agility}')
        print(f'Защита:{self.defence}') 

    #Тратим очки навыков, качаем статы

    def up_stats(self):
        while self.stat_point > 0:
            print("Что хотите прокачать?:\n1 - +2 к HP\n2 - +1 к атаке\n3 - +1 к ловкости\n4 - +1 к броне")
            num_up = input('> ')

            if num_up == "1":
                self.max_hp += 2
                self.now_hp += 2
                self.stat_point -= 1

            elif num_up == "2":
                self.strength += 1
                self.stat_point -= 1

            elif num_up == "3":
                self.agility += 1
                self.stat_point -= 1

            elif num_up == "4":
                self.defence += 1
                self.stat_point -= 1

            else:
                print("Такой опции нет")

    #Показываем наш инвентарь

    def show_inventory(self):
        
        global inventory
        print(f"Оружие - {inventory['weapon']}\nБроня - {inventory['armor']}")
        
        for i in range(1,6):
            print(f"{i} - {inventory[str(i)]}")
        print(f"money - {self.money}")

    
    #Функция для смены предметов из основных слотов и убирания статов

    def switch_main_item(self,name,category):
        print(f'\nЧто вы хотите сделать с {name}\n1 - Вернуть в инвентарь\n2 - Выкинуть\n')
        
        chosen_num = input('> ')
        
        for i in weapons:
            if i in name:
                if 'Меч' in inventory['weapon']:
                    self.strength -= 3 + int(inventory['weapon'][4:][:1])

                elif 'Кинжал' in inventory['weapon']:
                    self.strength -= 1 + int(inventory['weapon'][7:][:1])
                    self.agility -= 2 + int(inventory['weapon'][7:][:1])

                elif 'Рогатка' in inventory['weapon']:
                    self.agility -= 3 + int(inventory['weapon'][8:][:1])

                elif 'Посох' in inventory['weapon']:
                    self.strength -= 2 + int(inventory['weapon'][6:][:1])
                    self.defence -= 1 + int(inventory['weapon'][6:][:1])

                elif 'Сковородочаки' in inventory['weapon']:
                    self.agility -= 2 + int(inventory['weapon'][14:][:1])
                    self.defence -= 2 + int(inventory['weapon'][14:][:1])

        for j in armor:
            if j in name:
                if 'Крутая броня' in inventory['armor']:
                    self.defence -= 5 + int(inventory['armor'][13:][:1])

                elif 'Кольчужная броня' in inventory['armor']:
                    self.defence -= 3 + int(inventory['armor'][17:][:1])
                    self.agility -= 1 + int(inventory['armor'][17:][:1])

                elif 'Тканевая броня' in inventory['armor']:
                    self.defence -= 2 + int(inventory['armor'][15:][:1])
                    self.agility -= 3 + int(inventory['armor'][15:][:1])
                    
        if chosen_num == '1': self.add_inventory(name)

        elif chosen_num == '2': inventory[category] = ''

        else: 
            print('Такого варианта нет!')
            self.inventory_use()

    def add_inventory(self,add_item):
        global inventory

        # Добавление предмета
        for i in range(1,6):
            if inventory[str(i)] == '':
                inventory[str(i)] = add_item
                break

        # Если нет места
        else:
            print('Ваш инвентарь заполнен.\nЧто вы будете делать?\n1 - Выбросить что-то из инвентаря\n2 - Не подбирать вещь')
            chosen_num = input('> ')

            if chosen_num == '1':
                print('\nВыберите вещь, которую выкините:\n')

                for j in range(1,6):
                    print(f'{j} - {inventory[str(j)]}')
                chosen_num1 = input('> ')

                if inventory[chosen_num1] != '': inventory[chosen_num1] = add_item
                else: print('Такой ячейки нет')
            
            elif chosen_num == '2':
                pass

            else:
                print('Такого варианта нет!')

    #Использование инвентаря

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

                if any(item in inventory[choosen_num] for item in weapons):
                    print('1 - Переложить  в основную руку\n2 - Выкинуть\n3 - Ничего')
                    choosen_num1 = input('> ')
                    
                    if choosen_num1 == '1':

                        #Если в слоте оружия уже есть что-то

                        if inventory['weapon'] != '': self.switch_main_item(inventory['weapon'],'weapon')
                        inventory['weapon'] = inventory[choosen_num]
                        
                        if 'Меч' in inventory['weapon']:
                            self.strength += 3 + int(inventory['weapon'][4:][:1])
                        
                        elif 'Кинжал' in inventory['weapon']:
                            self.strength += 1 + int(inventory['weapon'][7:][:1])
                            self.agility += 2 + int(inventory['weapon'][7:][:1])
                        
                        elif 'Рогатка' in inventory['weapon']:
                            self.agility += 3 + int(inventory['weapon'][8:][:1])
                        
                        elif 'Посох' in inventory['weapon']:
                            self.strength += 2 + int(inventory['weapon'][6:][:1])
                            self.defence += 1 + int(inventory['weapon'][6:][:1])
                       
                        elif 'Сковородочаки' in inventory['weapon']:
                            self.agility += 2 + int(inventory['weapon'][14:][:1])
                            self.defence += 2 + int(inventory['weapon'][14:][:1])
                        
                        inventory[choosen_num] = ''
                    
                    elif choosen_num1 == '2':
                        inventory[choosen_num] = ''
                    
                    elif choosen_num1 == '3':
                        pass

                elif any(item in inventory[choosen_num] for item in armor):
                    print('1 - Надеть\n2 - Выкинуть\n3 - Ничего')
                    
                    choosen_num1 = input('> ')
                    
                    if choosen_num1 == '1':

                        #Если в слоте брони есть что-то

                        if inventory['armor'] != '': self.switch_main_item(inventory['armor'],'armor')
                        inventory['armor'] = inventory[choosen_num]
                        
                        if 'Крутая броня' in inventory['armor']:
                            self.defence += 5 + int(inventory['armor'][13:][:1])
                        
                        elif 'Кольучжная броня' in inventory['armor']:
                            self.defence += 3 + int(inventory['armor'][17:][:1])
                            self.agility += 1 + int(inventory['armor'][17:][:1])
                        
                        elif 'Тканевая броня' in inventory['armor']:
                            self.defence += 2 + int(inventory['armor'][15:][:1])
                            self.agility += 3 + int(inventory['armor'][15:][:1])
                        
                        inventory[choosen_num] = ''

                    
                    elif choosen_num1 == '2':
                        inventory[choosen_num] = ''
                    
                    elif choosen_num1 == '3':
                        pass
                
                elif inventory[choosen_num] in useables:
                    print('1 - Выпить\n2 - Выкинуть\n3 - Ничего')
                    choosen_num1 = input('> ')
                    
                    if choosen_num1 == '1':
                        
                        if inventory[choosen_num] == 'Малое зелье исцеления':
                            self.now_hp += 10
                        
                        elif inventory[choosen_num] == 'Среднее зелье исцеления':
                            self.now_hp += 25
                        
                        elif inventory[choosen_num] == 'Большое зелье исцеления':
                            self.now_hp += 70
                        
                        if self.now_hp > self.max_hp:
                            self.now_hp = self.max_hp
                        
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

    def lvl_up(self):
        while self.exp >= self.req_exp:
            self.req_exp += self.lvl
            self.lvl += 1
            self.exp = self.exp - self.req_exp
            self.stat_point += 1
    
    def menu(self):
        if self.now_hp <= 0:
            print("Конец игры")
            self.gameover()
            return True
        
        self.change_floor()
        self.lvl_up()

        print("\nВаше действие:\n1 - Идти дальше\n2 - Просмотреть инвентарь\n3 - Использовать предмет\n4 - Посмотреть характеристики\n")
        chosen_num = input('> ')
        
        if chosen_num == '1': self.move()
        elif chosen_num == '2': self.show_inventory()
        elif chosen_num == '3': self.inventory_use()
        elif chosen_num == '4': self.show_stats()
        else: 
            print('Такого выбора нет!')
            self.menu()

    #Движение и комнаты

    def move(self):
        room_list = []

        for i in range(1,3):
            chosen_room = randint(1,3)
            if chosen_room == 1: 
                self.random_hide('Боевая комната',i) 
                room_list.append('Боевая комната')

            elif chosen_room == 2: 
                self.random_hide('Комната с сокровищами',i)
                room_list.append('Комната с сокровищами')

            elif chosen_room == 3: 
                self.random_hide('Комната отдыха',i)
                room_list.append('Комната отдыха')

        print(f'\nКуда идем?\n1 - Налево\n2 - Направо\n')
        chosen_num = input('> ')

        if chosen_num == "1":
            if room_list[0] == 'Боевая комната': self.battle_room()

            elif room_list[0] == 'Комната с сокровищами': self.treasure_room()

            elif room_list[0] == 'Комната отдыха': self.rest_room()

        elif chosen_num == '2':
            if room_list[1] == 'Боевая комната': self.battle_room()

            elif room_list[1] == 'Комната с сокровищами': self.treasure_room()

            elif room_list[1] == 'Комната отдыха': self.rest_room()

        else:
            print('Такого выбора нет!')
            self.menu()

    #Видимость комнат 

    def random_hide(self,name_room,num_room):
        rand_num = randint(1,2)

        if num_room == 1: 
            if rand_num == 1: print(f'\nСлева: {name_room}')
            else: print("\nСлева: густой туман...")

        else:
            if rand_num == 1: print(f"Справа: {name_room}")
            else: print("Справа: густой туман...")

    #Боевая комната

    def battle_room(self):
        print("\nВы в боевой комнате.")
        self.show_stats()
        self.battle()
        self.room += 1
    
    #Комната с сокровищами

    def treasure_room(self):
        self.room += 1
        print('\nВы в комнате с сокровищами\nВыберите действие:\n1 - Открыть сундук\n2 - Уйти\n')
        chosen_num = input('> ')

        if chosen_num == '1': self.drop()

        elif chosen_num == '2': self.menu()

        else: 
            print('Такого выбора нет!')
            self.treasure_room()

    #Комната отдыха

    def rest_room(self):
        self.room += 1
        print(f'\nВы в комнате отдыха\nУ вас есть {self.stat_point} очков навыков\nВыберите действие:')

        if self.stat_point == 0:
            print('1 - Идти дальше\n')
            chosen_num = input('> ')

            if chosen_num == '1': self.menu()
            else: print('Такой опции нет!')

        else:
            print('1 - Идти дальше\n2 - Повысить характеристики\n')
            chosen_num = input('> ')

            if chosen_num == '1': self.menu()

            elif chosen_num == '2': self.up_stats()

            else: print('Такой опции нет!')

    #Механика смен этажа

    def change_floor(self):
        if self.room >= 5 * self.floor:
            self.floor += 1
            print(f'\nВы перешли на {self.floor} этаж')

    #Дроп вещей

    def drop(self):
        rand_item = randint(1, 3)
        if rand_item == 1:
            rand_item = choice(weapons)

        if rand_item == 2:
            rand_item = choice(armor)

        # Шансы дропа для зелий
        if rand_item == 3:
            choice(useables)
            rand_num1 = randint(1,10)

            if 1 <= rand_num1 < 8: rand_item = useables[0]

            elif 8 <= rand_num1 < 10: rand_item = useables[1]

            else: rand_item = useables[2]
            
        if rand_item in useables: print(f'\nВы нашли:{rand_item}')

        else: print(f'\nВы нашли:{rand_item}' + f'({self.floor})')

        print('\nВыберите действие:\n1 - Добавить в инвентарь\n2 - Выкинуть\n')
        chosen_num = input('> ')

        if rand_item in useables:
            if chosen_num == '1': self.add_inventory(rand_item)

            elif chosen_num == '2': 
                self.menu()

            else: 
                print('Такого выбора нет!')
                self.drop()
        else:
            if chosen_num == '1': self.add_inventory(rand_item + f'({self.floor})')

            elif chosen_num == '2': self.menu()

            else: 
                print('Такого выбора нет!')
                self.drop()

    #Функция для нашей атаки

    def attack(self, mob_stats):
        crit_chance = randint(1,20)

        if self.strength - mob_stats[4] < 0:
            print("\nВы нанесли 0 урона")

        else:
            # Критический удар
            if crit_chance == 1:
                mob_stats[0] -= (self.strength * 2) - mob_stats[4]

                if mob_stats[0] < 0:
                    mob_stats[0] = 0

                print(f'\nВы нанесли критический удар на {(self.strength * 2) - mob_stats[4]} урона.\nУ врага осталось {mob_stats[0]}\{mob_stats[1]} здоровья')

            else:
                mob_stats[0] -= self.strength - mob_stats[4]

                if mob_stats[0] < 0:
                    mob_stats[0] = 0

                print(f'\nВы нанесли {self.strength - mob_stats[4]} урона.\nУ врага осталось {mob_stats[0]}\{mob_stats[1]} здоровья')
    
    #Функция для атаки моба

    def mob_attack(self, mob_stats):
        crit_chance = randint(1,20)

        if mob_stats[2] - self.defence < 0:
            print("Вам нанесли 0 урона")

        else:
            # Критический удар
            if crit_chance == 1:
                self.now_hp -= (mob_stats[2] * 2) - self.defence

                if self.now_hp < 0:
                    self.now_hp = 0

                print(f'Вам нанесли критический удар на {(mob_stats[2] * 2) - self.defence} урона.\nУ вас осталось {self.now_hp}\{self.max_hp} здоровья')

            else:
                self.now_hp -= mob_stats[2] - self.defence

                if self.now_hp < 0:
                    self.now_hp = 0

                print(f'Вам нанесли {mob_stats[2] - self.defence} урона.\nУ вас осталось {self.now_hp}\{self.max_hp} здоровья')

    #Боевка

    def battle(self):
        mob = Mob(self.floor,self.room)
        mob_stats = list(mob.mob_show_stats())

        while self.now_hp > 0 and mob_stats[0] > 0:
            dodge_chance1 = False  
            print("\nВыберите действие:\n1.Нанести удар\n2.Попытаться уклониться\n3.Использовать предмет\n")
            chosen_num = input("> ")

            if chosen_num == "1":
                dodge_chance = mob_stats[3] - self.agility

                if dodge_chance <= 0:
                    self.attack(mob_stats)

                else:
                    rand_num = randint(1,20)

                    if dodge_chance > 10:
                        dodge_chance = 10

                    if dodge_chance >= rand_num:
                        dodge_chance = True

                    else:
                        dodge_chance = False

                    if dodge_chance:
                        print("Враг уклонился")

                    else:
                        self.attack(mob_stats)

            elif chosen_num == "2":
                dodge_chance1 = mob_stats[3] - self.agility

                if dodge_chance1 <= 0:
                    dodge_chance1 = 2

                rand_num = randint(1,20)

                if dodge_chance1 > 15:
                    dodge_chance1 = 15

                if dodge_chance1 >= rand_num:
                    dodge_chance1 = True

                else:
                    dodge_chance1 = False

            elif chosen_num == "3":
                self.inventory_use()

            else:
                print("Такого действия нет")
                self.battle()
            
            if mob_stats[0] <= 0: break

            print("\nВраг атакует!")

            if dodge_chance1:
                print("Вы уклонились")

            else:                
                dodge_chance = self.agility - mob_stats[3]

                if dodge_chance <= 0:
                    self.mob_attack(mob_stats)

                else:
                    rand_num = randint(1,20)

                    if dodge_chance > 10:
                        dodge_chance = 10

                    if dodge_chance >= rand_num:
                        dodge_chance = True

                    else:
                        dodge_chance = False

                    if dodge_chance:
                        print("Вы уклонились")

                    else:
                        self.mob_attack(mob_stats)

        if self.now_hp <= 0:
            print("Вы погибли")

        else:
            print("Враг повержен")
            self.exp += mob_stats[5]
            self.money += mob_stats[6]
            self.drop()

    #Экран смерти

    def gameover(self):
        print(f'\nВы находились на {self.floor} этаже в {self.room} комнате.\nУ вас было {self.money} золота.\nВы были {self.lvl} уровня')
        print("\nВыберите действие:\n1.Начать игру заново\n2.Закончить игру\n")
        chosen_num = input("> ")

        if chosen_num == "1":
            print('Who are you?')
            self.name = input("> ")
            self.race = ''
            self.money = 0
            self.floor = 0
            self.exp = 0
            self.req_exp = 5
            self.lvl = 1
            self.stat_point = 0
            self.room = 0
            self.char_stats()
            self.show_stats()
            self.menu()

        elif chosen_num == "2":
            pass

        else:
            print("Такого варианта нет!")