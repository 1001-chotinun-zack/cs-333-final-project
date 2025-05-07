import random
from character_class import Character

class Roll:
    def __init__(self):

        self.talentDictionary = {
            'Acrobatics' : 'DEX',
            'Animal Handling' : 'WIS',
            'Climbing'  : 'STR',
            'Combat' : 'STR',
            'Deception'  : 'CHA',
            'Endurance' : 'SPT',
            'Insight' : 'WIS',
            'Investigation'  : 'INT',
            'Lore'  : 'INT',
            'Medicine' : 'SPT',
            'Perception' : 'WIS',
            'Performance'  : 'CHA',
            'Persuasion' : 'CHA',
            'Resistance' : 'SPT',
            'Sleight of Hand' : 'DEX',
            'Stealth' : 'DEX',
            'Strategy' : 'INT',
            'Swimming'  : 'STR'
        }

    def roll_dice(self, sides=20):
        result = random.randint(1, sides)
        return result

    def get_rollStat(self, rollType):
        rollStat = self.talentDictionary.get(rollType) 
        return rollStat

    def calculate_roll(self, character, rollType, advantage):

        #get character stats
        name = str(character.get_name())
        element = str(character.get_element())
        level = int(character.get_level())
        stren = int(character.get_stren())
        spt = int(character.get_spt())
        wis = int(character.get_wis())
        intl = int(character.get_intl())
        dex = int(character.get_dex ())
        cha = 5
        talents = character.get_all_talents()

        rollStat = "" #stat the roll we're doing falls under
        charStat = 0 #check character's stat in that talent
        char_modifier = 0
        rollResult = 0

        rollStat = self.get_rollStat(rollType)
        charStat = int(character.find_stat(rollStat))
            
        #PROCESS element INFO
        if character.get_elementStat() == rollStat:
            element_modifier = character.get_elementModifier()
            charStat += element_modifier

       #CALCULATE MODIFIERS
        char_modifier = character.get_statModifier(charStat)
        
        # PROCESS TALENTS
        if rollType in talents:    
            if talents[rollType] == "ADV":
                if advantage == -1:
                    advantage = 0
                else:
                    advantage = 1
            elif talents[rollType] == "BUFF":
                char_modifier += 3
                
        #ROLL DICE
        dice = [0,0]
        diceResult = 0

        if advantage == 1:
            dice, diceResult = self.roll_advantage()
        elif advantage == -1:
            dice, diceResult = self.roll_disadvantage()
        else:
            dice[0] = self.roll_dice()
            diceResult = dice[0]

        #GET FINAL ROLL RESULT
        rollResult = diceResult + char_modifier
        return rollResult, dice, diceResult   
    
    def roll_advantage(self):
        dice = [0,0]
        diceResult = 0

        dice[0] = self.roll_dice()
        dice[1] = self.roll_dice()

        #pick the better of the two rolls
        if dice[0] >= dice[1]:
            diceResult = dice[0]
        else:
            diceResult = dice[1]
        
        return dice, diceResult

    def roll_disadvantage(self):
        dice = [0,0]
        diceResult = 0

        dice[0] = self.roll_dice()
        dice[1] = self.roll_dice()

        #pick the worse of the two rolls
        if dice[0] <= dice[1]:
            diceResult = dice[0]
        else:
            diceResult = dice[1]
        
        return dice, diceResult
