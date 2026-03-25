import time as t
import random as r
arguements = ['i', 's', 'x']
def decision(x):
    for i in range(x):
        # Convert to lower case immediately to save typing it later
        command = input("enter your command: ").lower()
        
        if command == "i":
            inv.display()
        elif command == "s":
            merch.display()
            merch.buy()
        elif command == "x":
            print("exiting menu")
            break
        elif command != '' and command not in arguments:
            print("invalid command")
            

class character:


    def __init__(self, name,charisma,strength,dexterity,wisdom,health,money,playerloc):
        self.name = name
        self.charisma = charisma
        self.strength = strength
        self.dexterity = dexterity
        self.wisdom = wisdom
        self.health = health
        self.money = money
        self.playerloc = playerloc


    def checkstats(self):

        if self.charisma + self.strength + self.dexterity + self.wisdom == 9:
            print('nice choices, lets continue')

        else:
            print('you didnt use your upgrade points correctly, re-run the game and try again')
            self.health = 0
            exit()


    def showstats(self):
        print(f"Your stats are,\nName: {self.name}    Charisma: {self.charisma}\nStrength: {self.strength}    Dextarity: {self.dexterity}\nWisdom: {self.wisdom}    Health: {self.health}\nMoney: {self.money} Location: {self.playerloc}")

class bow:
    def __init__(self,name,attack,tier):
        self.name = name
        self.attack = attack
        self.tier = tier
    def showstats(self):
        print(f"Stats for: {self.name}    Attack:{self.attack}\nTier:{self.tier}")
    def rename(self):
        self.name = input("Enter the new name: ")


class sword:


    def __init__(self,name,tier,attack):
        self.name = name
        self.tier = tier
        self.attack=attack


    def showstats(self):
        print(f"Stats for: {self.name}\nAttack:{self.attack}    Tier:{self.tier}")

    def rename(self):
        self.name = input("Enter the new name: ")


user=input("you wake up in an unfamilliar bed, you cant seem to remember anything. \nAs your vision continues to clear you see a man with a gruff beard \nstanding in front of you 'Honey! HE'S AWAKE' the man calls,\n a woman walks into the room asking your name\n\n Dear, what is your name:   ")
print('you have nine points to spend on your character')
t.sleep(.5)
print('the stats are,\ncharisma\nstrength\ndexterity\nwisdom')
t.sleep(.5)
cha=int(input('enter your charisma: '))
stren=int(input('enter your strength: '))
dex=int(input('enter your dexterity: '))
wis=int(input('enter your wisdom: '))



mychar = character(user,cha,stren,dex,wis,20,0,'mystery village')

class Inventory:

    def __init__(self,sword1,sword2,bow,arrows,shield,item1,item2,item3):
        self.sword1 = sword1
        self.sword2 = sword2
        self.bow = bow
        self.arrows = arrows
        self.shield = shield
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
    def display(self):
        mychar.showstats()
        print(f"Inventory,\n{self.sword1}    {self.sword2} <-Swords\n{self.bow}    {self.arrows} <-Bow <-Arrows\n{self.item1}    {self.item2} <-Item slots\n{self.item3}    {self.shield} <-Item slot <-Shield")

inv=Inventory('empty','empty','empty','empty','empty','empty','empty','empty')


upgradepts=0


class Shop:
    def __init__(self, item1, price1, item2, price2, item3, price3, item4, price4, item5, price5):
        self.item1 = item1
        self.price1 = price1
        self.item2 = item2
        self.price2 = price2
        self.item3 = item3
        self.price3 = price3
        self.item4 = item4
        self.price4 = price4
        self.item5 = item5
        self.price5 = price5


    def display(self):
        print('')
        print('')
        print("-{)()()()()()()()()()()()()()()()()()(}-")
        print(' ')
        print(f" {self.item1}---------- {self.price1}           Welcome to my shop!")
        print(' ')
        print(f" {self.item2} ----------{self.price2}            What would you like to buy?")
        print(' ')
        print(f" {self.item3} ----------{self.price3}")
        print(' ')
        print(f" {self.item4}----------- {self.price4}           Jangy's shop at {mychar.playerloc}")
        print(' ')
        print(f" {self.item5} -----------{self.price5}")
        print('-{)()()()()()()()()()()()()()()()()()(}- \n\n')
    def buy(self):
        item = input("Enter the name of the item you would like to buy: ")
        if item.lower() == self.item1:
            if inv.item1 == 'empty':
                inv.item1 = self.item1
                mychar.money -= self.price1
                print("item purchased successfully")
            elif inv.item2 == 'empty':
                inv.item2 = self.item1
                mychar.money -= self.price1
                print("item purchased successfully")
            elif inv.item3 == 'empty':
                inv.item3 = self.item1
                mychar.money -= self.price1
                print("item purchased successfully")
            else:
                print('Inventory is full,')
                t.sleep(.5)
                inv.display()
                t.sleep(.5)
                invreplace=input('Do you want to replace the item? (yes/no): ')
                if invreplace.lower() == 'yes':
                    invreplace = int(input('Enter the slot to replace with the item (1/2/3): '))
                    if invreplace == 1:
                        inv.item1 = self.item1
                        mychar.money = mychar.money - self.price1
                        print("item purchased successfully")
                    elif invreplace == 2:
                        inv.item2 = self.item1
                        mychar.money = mychar.money - self.price1
                        print("item purchased successfully")
                    elif invreplace == 3:
                        inv.item3 = self.item1
                        mychar.money = mychar.money - self.price1
                        print("item purchased successfully")
                    else:
                        class Shop:
                            def __init__(self, items):
                                """items: dict mapping item_name -> price (names should be lowercase)."""
                                # copy to avoid external mutation
                                self.items = {k.lower(): v for k, v in items.items()}

                            def display(self):
                                print('')
                                print('')
                                print("-{)()()()()()()()()()()()()()()()()()(}-")
                                print(' ')
                                # header
                                print('           Welcome to my shop!')
                                print(' ')
                                for name, price in self.items.items():
                                    print(f" {name} ----------- {price}")
                                print(' ')
                                print(f"           Jangy's shop at {mychar.playerloc}")
                                print('-{)()()()()()()()()()()()()()()()()()(}- \n\n')

                            def buy(self):
                                item = input("Enter the name of the item you would like to buy: ").lower().strip()
                                if item not in self.items:
                                    print("That is an invalid item")
                                    return

                                price = self.items[item]
                                if mychar.money < price:
                                    print("You're too broke for that.")
                                    return

                                # try to place in first empty slot
                                slots = ["item1", "item2", "item3"]
                                for slot in slots:
                                    if getattr(inv, slot) == 'empty':
                                        setattr(inv, slot, item)
                                        mychar.money -= price
                                        print("item purchased successfully")
                                        return

                                # inventory full
                                print('Inventory is full,')
                                t.sleep(.5)
                                inv.display()
                                t.sleep(.5)
                                invreplace = input('Do you want to replace the item? (yes/no): ').lower().strip()
                                if invreplace != 'yes':
                                    print('okay')
                                    return

                                try:
                                    slot_num = int(input('Enter the slot to replace with the item (1/2/3): '))
                                except ValueError:
                                    print('That is not a valid choice')
                                    return

                                if slot_num in (1, 2, 3):
                                    setattr(inv, f'item{slot_num}', item)
                                    mychar.money -= price
                                    print('item purchased successfully')
                                else:
                                    print('That is not a valid choice')
merch = Shop({
    'bread': 3,
    'potion': 10,
    'elixir': 25
})
def opening_dialogue():
    global fist
    mychar.showstats()
    mychar.checkstats()
    t.sleep(5)
    print("Man: You're awake now no need to thank us for the shelter, just leave")
    t.sleep(2)
    print("Woman: the boy needs food and money its the right thing to do for a traveler")
    t.sleep(2)
    print(f"Man: fine, {mychar.name} can stay to eat but after that, we send him off")
    t.sleep(2)
    print("Woman: he needs money if he is to survive")
    t.sleep(2)
    print("Woman: *hands you twenty coins*")
    t.sleep(2)
    print("[SYSTEM] You received 20 coins")
    t.sleep(2)
    print("Man: fine, but if he is ever to return to this house i will kill him")
    mychar.money += 20
    t.sleep(3)
    print('you follow the woman to the dining room')
    t.sleep(2)
    print('Woman: Sorry about my husband, he was qualified for worlds dumbest person last month, im so exited for when he wins')
    t.sleep(2)
    command = input('1. What?\n2. Huh?\nEnter your choice (default: 1): ')
    if command == command:
        pass
    t.sleep(2)
    print('Woman: yeah well it takes one to know one, i got it last year')
    t.sleep(2)
    print('weirded out you quickly finish your food and leave')
    t.sleep(2)
    print("""
------------------
|   CHAPTER ONE  |
|A NEW BEGINNING |
------------------
""")
    print("type 'i' for inventory")
    t.sleep(.5)
    command = input("enter your command: ")
    if command == 'i':
        inv.display()
        print("type 'x' to exit")
        command = input("enter your command: ")
        if command == 'x':
            print('\n')

    fist = sword('fist', 1, 3)

# Run the opening dialogue here
if mychar.name == "dev":
    pass
else:
    opening_dialogue()


class opponent:
    def __init__(self, name,hp,weapon):
        self.name = name
        self.hp = hp
        self.weapon=weapon
    def attack(self):
        mychar.health -= self.weapon.attack






def combatsys(op=None):
    """Simple turn-based combat between `mychar` and an `opponent`.

    If `op` is None a default opponent is created. Player actions:
    - attack (a): deal weapon damage + strength
    - defend (d): halve incoming damage this turn
    - run (r): 50% chance to escape
    - info (i): show stats
    """
    if op is None:
        op = opponent('Bandit', 15, fist)

    print(f"A {op.name} appears!")

    defended = False

    while mychar.health > 0 and op.hp > 0:
        print(f"\nYour HP: {mychar.health} | Enemy HP: {op.hp}")
        print("Choose: [a]ttack  [d]efend  [r]un  [i]nfo")
        action = input("Action: ").lower().strip()

        if action in ('a', 'attack'):
            weapon = inv.sword1 if hasattr(inv.sword1, 'attack') else fist
            damage = weapon.attack + (mychar.strength if isinstance(mychar.strength, int) else 0)
            op.hp -= damage
            print(f"You attack with {getattr(weapon, 'name', 'weapon')} for {damage} damage.")

        elif action in ('d', 'defend'):
            defended = True
            print("You brace yourself and prepare to take reduced damage.")

        elif action in ('r', 'run'):
            if r.random() < 0.5:
                print("You manage to escape the fight!")
                return
            else:
                print("You fail to escape!")

        elif action in ('i', 'info'):
            mychar.showstats()
            op_weapon = getattr(op.weapon, 'name', str(op.weapon))
            print(f"Enemy: {op.name} HP: {op.hp} Weapon: {op_weapon}")
            continue

        else:
            print('Invalid action, try again.')
            continue

        # Opponent's turn (if still alive)
        if op.hp > 0:
            opp_base = getattr(op.weapon, 'attack', 1)
            opp_variation = r.randint(0, 2)
            opp_damage = opp_base + opp_variation
            if defended:
                opp_damage = max(0, opp_damage // 2)
            mychar.health -= opp_damage
            print(f"{op.name} attacks you for {opp_damage} damage.")
            defended = False

    # Combat resolution
    if mychar.health <= 0:
        print("You have been defeated.")
    else:
        print(f"You defeated {op.name}!")
        reward = 5
        mychar.money += reward
        print(f"[SYSTEM] You received {reward} coins.")
def training_dialogue():
    print("A man approaches you from the distance")
    t.sleep(2)
    print('Hey there young man, i havent seen you around town')
    t.sleep(2)
    print('You tell him your story')
    t.sleep(2)
    print('interesting...')
    t.sleep(2)
    print('considering your circumstances,')
    t.sleep(2)
    print("I'll teach you for free")
    t.sleep(2)
    print("you see, im the combat academy instructor")
    t.sleep(2)
    print("For now boy go visit the shop, you can do that at anytime by typing 's'")
    t.sleep(2)
    print("Breaking the fourth wall? me? no im not doing that")
    t.sleep(2)
    decision(2)
    t.sleep(2)
    print("did the training instructor send you here?")
    t.sleep(2)
    print("here, take this crystal")
    t.sleep(2)
    print("give it to him okay")
    t.sleep(2)
    print('you walk to the training center')
    t.sleep(2)
    print('ah youre back')
    t.sleep(.5)
    print('what is that you have for me?')
    t.sleep(2)
    print('did the shopkeeper tell you to give me this?')
    t.sleep(2)
    print('thanks for getting it for me')
    t.sleep(2)
    print('it looks quite dull now but no worries')
    t.sleep(2)
    print("it will be shiny and colorful in no time")
    t.sleep(2)
    print("time to get started training no?")
    t.sleep(2)
    

# Run the instructor/training dialogue
if mychar.name == "dev":
    pass
else:
    training_dialogue()
training_sword = sword("training",1,5)
    
inv.sword1 = training_sword
print("You equip the training sword")
try:
    inv.showstats()
except Exception:
    # Inventory has no showstats; show player stats instead
    mychar.showstats()
decision(3)
