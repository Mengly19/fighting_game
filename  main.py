from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

print(bcolors.FAIL + bcolors.BOLD + "\t\t\tWELCOME TO MY GAME" +bcolors.ENDC)
username = input(bcolors.OKBLUE+"\t\t\tPLEASE ENTER YOUR NAME : " + bcolors.ENDC)

# Create black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")


# Create white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")


# Create some items
potion = Item("Potion", "potion", "Heals 50 HP", 100)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 1000)
superpotion = Item("Super Potion", "potion", "Heals 1000 HP", 2000)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
# player_items = [potion, hipotion, superpotion, elixer, hielixer , grenade]

enemy_spells = [fire, meteor]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5},{"item": hielixer, "quantity": 2}, 
                {"item": grenade, "quantity": 5}]


# Instantiate people
player= Person(username,4200, 188, 311, 34, player_spells, player_items)
enemy = Person("Imp:  ",3000, 130, 560, 325,[], [])


running = True
i = 0 


while running:
    print("================================================================================================")
    print("\n")
    print ("NAME                 HP                                     MP")

    player.get_stats()
    enemy.get_enemy_stats()
    print("\n")
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) -1

    if index == 0: 
        dmg = player.genarate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "point of damage.")
    elif index == 1: 
        player.choose_magic()
        magic_choice = int(input("Choose magic: ")) - 1
        
        if magic_choice == -1 :
            continue 
            
        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()
        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)

        elif spell.type == "black":
            enemy.take_damage(magic_choice)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals ", str(magic_dmg), "points of damage." + bcolors.ENDC)
            
    elif index == 2 :
        player.choose_item()
        item_choice = int(input("Choose item: ")) -1

        if item_choice == -1 :
            continue
        
        item = player.items[item_choice] ["item"]

        if player.items[item_choice]["quantity"] == 0:
            print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
            continue
        player.items[item_choice]["quantity"] -= 1

        if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)
        elif item.type == "MegaElixer":
            player.hp = player.max_hp
            player.mp = player.max_mp
            print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)
        elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage to " + enemies[enemy].name + bcolors.ENDC)

       
    enemy_choice = 1

    enemy_dmg = enemy.genarate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

    print("========================")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
        
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "YOU ENEMY HAS DEDEATED YOU !" + bcolors.ENDC)
        print(bcolors.FAIL + "YOU LOSE :(" + bcolors.ENDC)
        running = False