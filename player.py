import random

class Player:
    
    def __init__(self, name):
       
        self.name = name
        self.points = 300
        

    def choose_if_hi_lo(self):
        
        while True:
            option = input("Will the next card be higher or lower? [h/l]: ")
            if option.lower() == "h" or option.lower() == "l":
                break
            else:
                print("Please type the right option!\n")
        return option
        

    def able_to_play(self):
            
        if self.points > 0:
            return True
        else:
            return False

