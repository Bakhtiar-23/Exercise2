# File:                       coin.py
# Source                      Tony Gaddis: Strating out Python, fourth edition
# Modified by:                Sanna Maatta & Anne Jumppanen
# Developed by:               Bakhtiar Khider Ismail
# Description:                Coin object and tossing

import random

class Coin:
    def __init__(self):
        self.sideup = random.choice(['Heads', 'Tails'])

    def toss_the_coin(self):
        outcome = random.randint(0, 4)
        if outcome == 0:
            self.sideup = 'Heads'
        elif outcome == 1:
            self.sideup = 'Tails'
        elif outcome == 2:
            self.sideup = 'Table Upright'
        elif outcome == 3:
            self.sideup= 'Lost in Space'
        elif outcome == 4:
            self.sideup = 'Lost in a Rabbit hole'

    def get_sideup(self):
        return self.sideup
    
    def lost_in_space(self):
        return self.sideup
    
    def lost_in_a_rabbit_hole(self):
        return self.sideup

def main():
    my_coin = Coin()

    print("This side is up:", my_coin.get_sideup())

    print("Tossing the coin...")
    my_coin.toss_the_coin()

    if my_coin.get_sideup() not in ['Lost in Space', 'Lost in a Rabbit hole','Table Upright']:
        print("Now this side is up:", my_coin.get_sideup())
    elif my_coin.get_sideup() in ['Table Upright']:
        print("Now the coin's side is upright:", my_coin.get_sideup())
    elif my_coin.get_sideup() in ['Lost in Space']:
        print("Oh no! The coin is lost in Space.")
    else:
        print("Oh no! The coin is lost in a rabbit hole.")

        
    
              

if __name__ == "__main__":
    main()
