
class Character:
    def __init__(self, name, element, level, stren, spt, wis, intl, dex):
        self.name = name
        self.element = element
        self.level = level

        self.stren = stren
        self.spt = spt
        self.wis = wis
        self.intl = intl
        self.dex = dex

        self.talents = {}

    #GETTERS
    def get_name(self):
        return self.name

    def get_element(self):
        return self.element

    def get_level(self):
        return self.level

    def get_stren(self):
        return self.stren

    def get_spt(self):
        return self.spt

    def get_wis(self):
        return self.wis

    def get_intl(self):
        return self.intl

    def get_dex(self):
        return self.dex

    def get_talent(self, talentName):
        if talentName in self.talents:
            return self.talents.get(talentName)
        else:
            return 0

    def get_all_talents(self):
        return self.talents

    #SETTERS
    def set_name(self, value):
        self.name = value

    def set_element(self, value):
        self.element = value

    def set_level(self, value):
        self.level = value

    def set_stren(self, value):
        self.stren = value

    def set_spt(self, value):
         self.spt = value

    def set_wis(self, value):
        self.wis = value

    def set_intl(self, value):
        self.intl = value

    def set_dex(self, value):
        self.dex = value

    #EXTRA FUNCTIONS
    def add_talent(self, talentName, talent_type):
        self.talents[talentName] = talent_type

    def find_stat(self, rollStat):
        statDictionary = {
            'WIS' : self.wis,
            'INT' : self.intl,
            'STR' : self.stren,
            'SPT' : self.spt,
            'DEX' : self.dex,
            'CHA' : 5
        }
        return statDictionary.get(rollStat)

    def get_elementStat(self):
        elementStat_dic = {
            "Fire": "STR",
            "Earth": "SPT",
            "Wind": "WIS",
            "Ice": "INTL",
            "Shadow": "DEX",
            "unawakened":"N/A"
        }
        return elementStat_dic.get(self.element)

    def get_elementModifier(self):
        if self.level == 1:
            return 1
        elif self.level == 2:
            return 2
        elif self.level == 3:
            return 5
        else:
            return 0

    def get_statModifier(self, stat):
        result = int(stat) - 5
        return result

    