from Classes.game import Person, bcolors
from Classes.magic import Spell
from Classes.inventory import Item
import random

'''
print("\n\n")
print("NAME                HP                                          MP")
print("                    ________________________________            __________")
print(bcolors.BOLD + "Valos:     " + bcolors.ENDC +
      "400/460 |" + bcolors.OKGREEN + "████████████████████████        " + bcolors.ENDC +
      "|     " + bcolors.BOLD + "10/65" + bcolors.ENDC + "|" + bcolors.OKBLUE + "██        " + bcolors.ENDC + "|")
'''


'''

magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 12, "dmg": 1240},
         {"name": "Blizzard", "cost": 10, "dmg": 100}]
         
'''

# Create Black Magic
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 32, 1500, "white")
curaga = Spell("Curaga", 50, 6000, "white")

#Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 1000)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
enemy_spells = [fire, meteor, curaga]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5}, {"item": superpotion, "quantity": 5},
                {"item": elixer, "quantity": 5}, {"item": hielixer, "quantity": 2}, {"item": grenade, "quantity": 5}]

# Instantiate People
player1 = Person("Valo", 3260, 132, 300, 34, player_spells, player_items)
player2 = Person("Nick", 4160, 188, 311, 34, player_spells, player_items)
player3 = Person("Robo", 3089, 174, 288, 34, player_spells, player_items)

enemy1 = Person("Imp", 3260, 132, 560, 325, enemy_spells, [])
enemy2 = Person("Mag", 18200, 701, 525, 25, enemy_spells, [])
enemy3 = Person("Jav", 1250, 130, 560, 325, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

'''

print(player.generate_spell_damage(0))
print(player.generate_spell_damage(1))
print(player.generate_spell_damage(2))

print (player.take_damage(459))

'''

running = True
i = 0

'''

while running:
    print("Let's overflow this stack", i)
    i += 1
    if i == 101:
        running = False
        
'''

print("\n"+bcolors.FAIL + bcolors.BOLD + "An Enemy Attack!" + bcolors.ENDC)

Round = 0

while running:
    Round += 1
    print("\n"+"=================","Round:",Round,"=================")

    print("\n")
    print("NAME                 HP                                      MP")

    for player in players:
        player.get_stats()

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        choice = input(bcolors.BOLD + "Choose action: " + bcolors.ENDC)
        index = int(choice) - 1
        print()

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target (enemies)
            enemies[enemy].take_damage(dmg)
            print("You attacked", enemies[enemy].name + " for", dmg, "points of damage.")

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name + " has died.")
                del enemies[enemy]

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input(bcolors.BOLD + "Choose magic: " + bcolors.ENDC)) - 1
            print()

            if magic_choice == -1:
                continue

            '''

            dmg = player.generate_spell_damage(magic_choice)
            spell = player.get_spell_name_magic(magic_choice)
            cost = player.get_spell_mp_cost(magic_choice)

            '''

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

        elif index == 2:
            player.choose_item()
            item_choice = int(input(bcolors.BOLD + "Choose item: " + bcolors.ENDC)) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None left!" + bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + "heals for", str(item.prop), "HP." + bcolors.ENDC)
            elif item.type == "elixer":

                if item.name == "MegaElixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                    print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP." + bcolors.ENDC)
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)

                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage to " + enemies[enemy].name + "." + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " has died.")
                    del enemies[enemy]

        # Check if battle is over
        defeated_enemies = 0
        defeated_players = 0

        for enemy in enemies:
            if enemy.get_hp() == 0:
                defeated_enemies += 1

        for player in players:
            if player.get_hp() == 0:
                defeated_players += 1

        # Check if Player won
        if defeated_enemies == 2:
            print("\n" + bcolors.OKGREEN + bcolors.BOLD + "You win! (:" + bcolors.ENDC)
            running = False

        if enemy.get_hp() == 0:
            print("\n" + bcolors.OKGREEN + bcolors.BOLD + "You win! (:" + bcolors.ENDC)
            running = False

        # Check if Enemy won
        elif defeated_players == 2:
            print("\n" + bcolors.FAIL + bcolors.BOLD + "You Lost! ):" + bcolors.ENDC)
            running = False

        # Enemy attack phase
        for enemy in enemies:
            enemy_choice = random.randrange(0, 2)

            if enemy_choice == 0:
                # Chose attack
                target = random.randrange(0, 2)
                enemy_dmg = enemy.generate_damage()

                players[target].take_damage(enemy_dmg)
                print(enemy.name.replace(" ","") + " Enemy attacks " + players[target].name.replace(" ","") + "for", enemy_dmg, "points of damage.")

            elif enemy_choice == 1:
                spell, magic_dmg = enemy.choose_enemy_spell()
                enemy.reduce_mp (spell.cost)

                if spell.type == "white":
                    enemy.heal(dmg)
                    print(bcolors.OKBLUE + "\n" + spell.name, " heals " + enemy.name + " for", str(dmg),
                          "HP." + bcolors.ENDC)
                elif spell.type == "black":
                    target = random.randrange(0, 3)
                    players[target].take_damage(magic_dmg)

                    print("You attacked for", magic_dmg, "points of damage to " + enemies[target].name + ".")
                    'print(bcolors.OKBLUE + "\n" + str(dmg) + " points of damage" + bcolors.ENDC)'

                    if players[target].get_hp() == 0:
                        print(players[target].name + " has died.")
                        del players[target]

                #print("Enemy chose", spell, "damage is", magic_dmg)


    print("\n"+"\033[93m"+"\033[1m"+"Results:"+ bcolors.ENDC + "\n")

    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)

'''
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")

    print("You have chosen", choice)
    print("You have chosen", player.get_spell_name_actions(index))
'''


