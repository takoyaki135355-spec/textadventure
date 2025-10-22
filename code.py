import time as t

def decision(x):
    for i in range(x):
        command = input("enter your command: ")
        if command.lower() == "i":
            inv.display()
        if command.lower() == "s":
            merch.display()
            merch.buy()
        elif command.lower() != '' and command.lower() not in ['i','s']:
            print("invalid command")
            decision()

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
str=int(input('enter your strength: '))
dex=int(input('enter your dexterity: '))
wis=int(input('enter your wisdom: '))



mychar = character(user,cha,str,dex,wis,20,0,'mystery village')

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
                        print('That is not a valid choice')
                        self.buy()
                else:
                    print('okay')






        elif item.lower() == self.item2:
            if inv.item1 == 'empty':
                inv.item1 = self.item2
                mychar.money -= self.price2
                print("item purchased successfully")
            elif inv.item2 == 'empty':
                inv.item2 = self.item2
                mychar.money -= self.price2
                print("item purchased successfully")
            elif inv.item3 == 'empty':
                inv.item3 = self.item2
                mychar.money -= self.price2
                print("item purchased successfully")
            else:
                print('Inventory is full,')
                t.sleep(.5)
                inv.display()
                t.sleep(.5)
                invreplace = input('Do you want to replace the item? (yes/no): ')
                if invreplace.lower() == 'yes':
                    invreplace = int(input('Enter the slot to replace with the item (1/2/3): '))
                    if invreplace == 1:
                        inv.item1 = self.item2
                        mychar.money = mychar.money - self.price2
                        print("item purchased successfully")
                    elif invreplace == 2:
                        inv.item2 = self.item2
                        mychar.money = mychar.money - self.price2
                        print("item purchased successfully")
                    elif invreplace == 3:
                        inv.item3 = self.item2
                        mychar.money = mychar.money - self.price2
                        print("item purchased successfully")
                    else:
                        print('That is not a valid choice')
                        self.buy()
                else:
                    print('okay')

        elif item.lower() == self.item3:
            if inv.item1 == 'empty':
                inv.item1 = self.item3
                mychar.money -= self.price3
                print("item purchased successfully")
            elif inv.item2 == 'empty':
                inv.item2 = self.item3
                mychar.money -= self.price3
                print("item purchased successfully")
            elif inv.item3 == 'empty':
                inv.item3 = self.item3
                mychar.money -= self.price3
                print("item purchased successfully")
            else:
                print('Inventory is full,')
                t.sleep(.5)
                inv.display()
                t.sleep(.5)
                invreplace = input('Do you want to replace the item? (yes/no): ')
                if invreplace.lower() == 'yes':
                    invreplace = int(input('Enter the slot to replace with the item (1/2/3): '))
                    if invreplace == 1:
                        inv.item1 = self.item3
                        mychar.money = mychar.money - self.price3
                        print("item purchased successfully")
                    elif invreplace == 2:
                        inv.item2 = self.item3
                        mychar.money = mychar.money - self.price3
                        print("item purchased successfully")
                    elif invreplace == 3:
                        inv.item3 = self.item3
                        mychar.money = mychar.money - self.price3
                        print("item purchased successfully")
                    else:
                        print('That is not a valid choice')
                        self.buy()
                else:
                    print('okay')

        elif item.lower() == self.item4:
            if inv.item1 == 'empty':
                inv.item1 = self.item4
                mychar.money -= self.price4
                print("item purchased successfully")
            elif inv.item2 == 'empty':
                inv.item2 = self.item4
                mychar.money -= self.price4
                print("item purchased successfully")
            elif inv.item3 == 'empty':
                inv.item3 = self.item4
                mychar.money -= self.price4
                print("item purchased successfully")
            else:
                print('Inventory is full,')
                t.sleep(.5)
                inv.display()
                t.sleep(.5)
                invreplace = input('Do you want to replace the item? (yes/no): ')
                if invreplace.lower() == 'yes':
                    invreplace = int(input('Enter the slot to replace with the item (1/2/3): '))
                    if invreplace == 1:
                        inv.item1 = self.item4
                        mychar.money = mychar.money - self.price4
                        print("item purchased successfully")
                    elif invreplace == 2:
                        inv.item2 = self.item4
                        mychar.money = mychar.money - self.price4
                        print("item purchased successfully")
                    elif invreplace == 3:
                        inv.item3 = self.item4
                        mychar.money = mychar.money - self.price4
                        print("item purchased successfully")
                    else:
                        print('That is not a valid choice')
                        self.buy()
                else:
                    print('okay')

        elif item.lower() == self.item5:
            if inv.item1 == 'empty':
                inv.item1 = self.item5
                mychar.money -= self.price5
                print("item purchased successfully")
            elif inv.item2 == 'empty':
                inv.item2 = self.item5
                mychar.money -= self.price5
                print("item purchased successfully")
            elif inv.item3 == 'empty':
                inv.item3 = self.item5
                mychar.money -= self.price5
                print("item purchased successfully")
            else:
                print('Inventory is full,')
                t.sleep(.5)
                inv.display()
                t.sleep(.5)
                invreplace = input('Do you want to replace the item? (yes/no): ')
                if invreplace.lower() == 'yes':
                    invreplace = int(input('Enter the slot to replace with the item (1/2/3): '))
                    if invreplace == 1:
                        inv.item1 = self.item5
                        mychar.money = mychar.money - self.price5
                        print("item purchased successfully")
                    elif invreplace == 2:
                        inv.item2 = self.item5
                        mychar.money = mychar.money - self.price5
                        print("item purchased successfully")
                    elif invreplace == 3:
                        inv.item3 = self.item5
                        mychar.money = mychar.money - self.price5
                        print("item purchased successfully")
                    else:
                        print('That is not a valid choice')
                        self.buy()
                else:
                    print('okay')

        else:
            print("That is an invalid input")
            self.buy()
merch = Shop('bread', 3, 'out of stock', 0, 'out of stock', 0, 'out of stock', 0, 'out of stock', 0)


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
print("Man: fine, but if he is ever to return to this house i will kill him")
mychar.money+=20
t.sleep(3)
print('you follow the woman to the dining room')
t.sleep(2)
print('Woman: Sorry about my husband, he was qualified for worlds dumbest person last month, im so exited for when he wins')
t.sleep(2)
input('1. What?\n2. Huh?\nEnter your choice: ')
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
command=input("enter your command: ")
if command == 'i':
    inv.display()
    print("type 'x' to exit")
    command = input("enter your command: ")
    if command == 'x':
        print('\n')

fist = sword('fist',1,3)


class opponent:
    def __init__(self, name,hp,weapon):
        self.name = name
        self.hp = hp
        self.weapon=weapon
    def attack(self):
        mychar.health -= self.weapon.attack






def combatsys():



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
print("it will be shiny and colorfull in no time")
t.sleep(2)
print("time to get started training no?")
t.sleep(2)
training_sword = sword(training,1,5)
inv.sword1=training_sword


