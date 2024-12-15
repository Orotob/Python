import random
import math
import time

class Rates():
    def __init__(self):
        self.rarity = random.randint(0,120000)

    def Single(self):
            print("Opening Lootbox...")
            time.sleep(3)
            rarity = self.rarity
            if rarity <= 120:
                print("You have obtained a Legendary item 0.1%")
            elif 120 < rarity <= 1320:
                print("You have obtained a Epic item 1%")
            elif 1320 < rarity <= 13320:
                print("You have obtained a Rare item 10%")
            elif 13320 < rarity <= 43320:
                print("You have obtained a Uncommon item 25%")
            else:
                print("You have obtained a Common item 63.9%")
    def Auto(self):
            print("Opening Lootbox...")
            rarity = self.rarity
            if rarity <= 120:
                print("You have obtained a Legendary item 0.1%")
            elif 120 < rarity <= 1320:
                print("You have obtained a Epic item 1%")
            elif 1320 < rarity <= 13320:
                print("You have obtained a Rare item 10%")
            elif 13320 < rarity <= 43320:
                print("You have obtained a Uncommon item 25%")
            else:
                print("You have obtained a Common item 63.9%")
    def Roll(self):
        while True:
            print("Menu\n")

            print("1. Auto Open")
            print("2. Single Open")
            print("3. Exit\n")
            
            menu = input("Enter Next Step: ")

            if "auto" in menu.lower():
                x = input("Enter the how many you want to open: ")
                for i in range(int(x)):
                    Rates().Auto()
            if "single" in menu.lower():
                    input("Press Enter to roll: ")
                    Rates().Single()
            if "exit" in menu.lower():
                 exit()


    def Start():
        Rates().Roll()



        