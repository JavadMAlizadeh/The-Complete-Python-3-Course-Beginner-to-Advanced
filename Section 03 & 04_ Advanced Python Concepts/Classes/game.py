import random

import self as self


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atakl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]
        self.name = name

    def generate_damage(self):
        return random.randrange(self.atakl, self.atkh)

    '''

    def generate_spell_damage(self, i):
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl, mgh)
        
    '''

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    '''

    def get_spell_name_magic(self, i):
        return self.magic[i]["name"]

    def get_spell_name_actions(self, i):
        return self.actions[i]

    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]
        
    '''

    def choose_action(self):
        i = 1
        print("\n" + bcolors.BOLD + self.name + bcolors.ENDC)
        print("\n" + "ACTIONS" + "\n")
        for item in self.actions:
            print("   ",str(i) + ".", item)
            i += 1
        print()

    def choose_magic(self):
        i = 1
        print("MAGIC", "\n")
        for spell in self.magic:
            print("   ",str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1
        print()

    def choose_item(self):
        i = 1

        print("ITEMS", "\n")
        for item in self.items:
            print("   ",str(i) + ".", item["item"].name + ":", item["item"].description + " (x" + str(item["quantity"])+")")
            i += 1
        print()

    def choose_target(self, enemies):
        i = 1

        print(bcolors.FAIL + bcolors.BOLD + "Target:" + bcolors.ENDC,"\n")
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("    " + str(i) + ".", enemy.name)
                i += 1
        print()
        choice = int(input("choose target:")) -1
        return choice

    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 2

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 13:
            decreased = 13 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        print("                     __________________________________________________")
        print(bcolors.BOLD + self.name + "   " + bcolors.ENDC +
              current_hp + " |" + bcolors.FAIL + hp_bar + bcolors.ENDC + "|")

    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 4

        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 100 / 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 10:
            decreased = 10 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""

        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)

            while decreased > 0:
                current_mp += " "
                decreased -= 1

            current_mp += mp_string
        else:
            current_mp = mp_string

        print("                     _________________________               __________")
        print(bcolors.BOLD + self.name + "     " + bcolors.ENDC +
              current_hp + " |" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + "|     " + bcolors.BOLD +
              current_mp + bcolors.ENDC + " |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        pct = self.hp / self.maxhp * 100

        if self.mp < spell.cost:
            self.choose_enemy_spell()

        else:
            return spell, magic_dmg


'''
# My Method:
        hp_length = self.hp
        mp_length = self.mp

        while len(str(hp_length)) == 3:
            hp_length = "0"+str(hp_length)

        while len(str(mp_length)) == 2:
            mp_length = "0"+str(mp_length)
'''




