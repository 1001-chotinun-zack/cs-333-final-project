import unittest
from game_class import Game
from character_class import Character
from roll_class import Roll

class Test_Character(unittest.TestCase):
    
    def test_dummy(self):
        pass
   
    def test_character_setters(self):
        character = Character("Ben", "Fire", 0, 10, 10, 10, 10 , 10)
        character.add_talent("Animal Handling", "BUFF")
        character.set_name("Holly")
        character.set_element("Earth")
        character.set_level(1)
        character.set_stren(4)
        character.set_spt(5)
        character.set_wis(6)
        character.set_intl(7)
        character.set_dex(4)

        self.assertEqual(character.get_name(), "Holly", "Name should be Holly")
        self.assertEqual(character.get_element(), "Earth", "Element should be Earth")
        self.assertEqual(character.get_level(), 1, "Level should be 1")
        self.assertEqual(character.get_stren(), 4, "Strength should be 4")
        self.assertEqual(character.get_spt(), 5, "Spirit should be 5")
        self.assertEqual(character.get_wis(), 6, "Wisdom should be 6")
        self.assertEqual(character.get_intl(), 7, "intlligence should be 7")
        self.assertEqual(character.get_dex(), 4, "Dexterity should be 4")
        self.assertEqual(character.get_talent("Animal Handling"), "BUFF", "Buff in Animal Handling")
        self.assertEqual(character.get_all_talents(), {"Animal Handling": "BUFF"}, "Buff in Animal Handling")
        
        
    def test_character_getters(self):
        character = Character("Holly", "Earth", 1, 4, 5, 6, 7 , 4)
        character.add_talent("Animal Handling", "BUFF")
        self.assertEqual(character.get_name(), "Holly", "Name should be Holly")
        self.assertEqual(character.get_element(), "Earth", "Element should be Earth")
        self.assertEqual(character.get_level(), 1, "Level should be 1")
        self.assertEqual(character.get_stren(), 4, "Strength should be 4")
        self.assertEqual(character.get_spt(), 5, "Spirit should be 5")
        self.assertEqual(character.get_wis(), 6, "Wisdom should be 6")
        self.assertEqual(character.get_intl(), 7, "intlligence should be 7")
        self.assertEqual(character.get_dex(), 4, "Dexterity should be 4")
        self.assertEqual(character.get_talent("Animal Handling"), "BUFF", "Buff in Animal Handling")
        self.assertEqual(character.get_all_talents(), {"Animal Handling": "BUFF"}, "Buff in Animal Handling")

    def test_find_stat(self):
        character = Character("Holly", "Earth", 1, 4, 5, 6, 7 , 4)
        charStat = character.find_stat("WIS")
        self.assertEqual(charStat, 6, "WIS Stat should be 6")

    def test_get_elementStat(self):
        character = Character("Holly", "Earth", 1, 4, 5, 6, 7 , 4)
        self.assertEqual(character.get_elementStat(), "SPT", "Element stat should be SPT")
        
    def test_get_modifiers(self):
        character = Character("Holly", "Earth", 2, 4, 5, 6, 7 , 4)
        self.assertEqual(character.get_elementModifier(), 2, "Element Modifier should be 2")
        self.assertEqual(character.get_statModifier(character.get_wis()), 1, "WIS stat Modifier should be +1")
    
class Test_Roll(unittest.TestCase):
    
    def test_roll_dice(self):
        roll = Roll()
        result = roll.roll_dice()
        self.assertLessEqual(result, 20, "Roll Result is less than or equal to 20")

    def test_get_rollStat(self):
        roll = Roll()
        self.assertEqual(roll.get_rollStat("Animal Handling"), "WIS", "Animal handling is a WIS stat roll")

    # integration test
    def test_calculate_roll(self):
        character = Character("Holly", "Earth", 1, 4, 6, 5, 7 , 4)
        character.add_talent("Animal Handling", "BUFF")
        roll = Roll()
        rollResult, dice, diceResult = roll.calculate_roll(character, "Endurance", 0)
        modifier_result = rollResult - diceResult
        self.assertEqual(modifier_result, 2, "modifier applied to diceResult should be +2")
    
    #def test_advantage_rolls(self):
        #roll = Roll()
        #adv_dice, adv_diceResult = roll.roll_advantage()
        #dis_dice, dis_diceResult = roll.roll_disadvantage()
        #self.assertGreaterEqual()

class Test_Game(unittest.TestCase):
        
    # integration test
    def test_get_roster(self):
        game = Game()
        character1 = Character("Holly", "Earth", 1, 4, 6, 5, 7 , 4)
        character2 = Character("Ben", "Fire", 2, 10, 1, 2, 3 , 4)
        game.add_character_to_game(character1)
        game.add_character_to_game(character2)
        self.assertEqual(game.get_roster(), ["Holly", "Ben"], "Names in roster are Holly and Ben")
        
    # integration test
    def test_add_character_to_game(self):
        game = Game()
        character = Character("Holly", "Earth", 1, 4, 6, 5, 7 , 4)
        game.add_character_to_game(character)
        self.assertEqual(game.get_roster(), ["Holly"], "Holly is in the roster")
    
    # integration test
    def test_delete_character_from_game(self):
        game = Game()
        character = Character("Holly", "Earth", 1, 4, 6, 5, 7 , 4)
        game.add_character_to_game(character)
        self.assertTrue(game.delete_character_from_game(character.get_name()), "Holly deleted from game")

    # integration test
    def test_select_character_for_roll(self):
        game = Game()
        character = Character("Holly", "Earth", 1, 4, 6, 5, 7 , 4)
        game.add_character_to_game(character)
        self.assertTrue(game.select_character_for_roll(character.get_name), "Holly selected for roll")

    # integration test
    def test_remove_character_from_roll(self):
        game = Game()
        character = Character("Holly", "Earth", 1, 4, 6, 5, 7 , 4)
        game.add_character_to_game(character)
        game.select_character_for_roll(character.get_name)
        self.assertTrue(game.remove_character_from_roll(character.get_name), "Holly removed from roll")

    def test_clear_selected_chars(self):
        game = Game()
        character = Character("Holly", "Earth", 1, 4, 6, 5, 7 , 4)
        game.add_character_to_game(character)
        game.select_character_for_roll(character.get_name)
        self.assertTrue(game.clear_selected_chars(), "Select list cleared")
        
if __name__ == "__main__":
    unittest.main()