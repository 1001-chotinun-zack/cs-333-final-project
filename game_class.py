from character_class import Character
from roll_class import Roll
    
class Game:
    def __init__(self):
        self.character_roster_dict = {} 
        self.select_list = []
        self.result_dict = {}
        
    def get_roster(self):
        return list(self.character_roster_dict.keys())
        
    def add_character_to_game(self, character):
        char_name = character.get_name()
        self.character_roster_dict[char_name] = character
    
    def delete_character_from_game(self, char_name):
        if char_name in self.character_roster_dict:
            self.character_roster_dict.pop(char_name)
            return True
        else:
            return False

    def select_character_for_roll(self, char_name):
        if char_name not in self.select_list:
            self.select_list.append(char_name)
            return True
        else:
            return False

    def remove_character_from_roll(self, char_name):
        if char_name in self.select_list:
            self.select_list.remove(char_name)
            return True
        else:
            return False

    def clear_selected_chars(self):
        if not self.select_list:
            return False
        else: 
            self.select_list.clear()
            return True

    def generate_results(self):
        rollType = self.rollSelect.get()
        roll = Roll()
        advantage = 0

        if self.adv_var.get() == 1 and self.dis_var.get() == 0:
            advantage = 1

        elif self.dis_var.get() == 1 and self.adv_var.get() == 0:
            advantage = -1

        length = len(self.select_list)
        count = 0
        for length in self.select_list:
            name = self.select_list[count]
            characterToRoll = self.roster_dict[name]
            rollResult, dice, diceResult = roll.calculate_roll(characterToRoll, rollType, advantage)
            self.result_dict[name] = [rollResult, dice, diceResult]
            count += 1
            
    def roll_again(self):
        self.result_dict.clear()
        self.select_list.clear()
        
    def reset_game(self):
        self.roll_again()
        self.character_roster_dict.clear()
