import random
import time
import os

class MatchUpGenerator:
    def __init__(self, totalPlayer, gameMode, spyMode):
        self.TOTAL_PLAYER = totalPlayer
        self.GAME_MODE = gameMode
        self.SPY_MODE = spyMode
        self.CHAMPION_LIST = list()
        self.SKILL_LIST = list()
        self.ITEM_LIST = list()
        self.RUNES_LIST = list()
    
    # assign factor variables, including: CHAMPION_LIST, SKILL_LIST, ITEM_LIST, RUNES_LIST
    def AssignFactorVariables(self):

        # set up variables from file
        def VariableSetUpByFile(fileName):
            with open(fileName, "r", encoding = "utf-8") as file:
                return file.read().splitlines()

        current_directory = os.path.dirname(__file__)
        self.CHAMPION_LIST = VariableSetUpByFile(os.path.join(current_directory, "factorTextFile", "champions.txt"))
        if self.GAME_MODE == "NG":
            self.SKILL_LIST = VariableSetUpByFile(os.path.join(current_directory, "factorTextFile", "skillsNG.txt"))
            self.ITEM_LIST = VariableSetUpByFile(os.path.join(current_directory, "factorTextFile", "itemsNG.txt"))
        elif self.GAME_MODE == "AR":
            self.SKILL_LIST = VariableSetUpByFile(os.path.join(current_directory, "factorTextFile", "skillsAR.txt"))
            self.ITEM_LIST = VariableSetUpByFile(os.path.join(current_directory, "factorTextFile", "itemsAR.txt"))
        self.RUNES_LIST = VariableSetUpByFile(os.path.join(current_directory, "factorTextFile", "runes.txt"))

    # return matchup information
    def GenerateMatchUp(self):

        # get champion index, no repeat
        # return list of numbers
        def GetChampionIndex(champCount):
            return random.sample(range(0, champCount), self.TOTAL_PLAYER)
        
        # get skill index
        # return: [ [player 1 skill 1, player 1 skill 2], [], [], [], ... ]
        def GetSkillIndex(skillCount):
            allPlayerSkillIndex = list()
            for _ in range(self.TOTAL_PLAYER):
                allPlayerSkillIndex.append( random.sample(range(0, skillCount), 2) )
                time.sleep(0.0001)
            return allPlayerSkillIndex
        
        # assign factor variables
        self.AssignFactorVariables()

        # get count of each factor
        champCount = len(self.CHAMPION_LIST)
        skillCount = len(self.SKILL_LIST)
        itemCount = len(self.ITEM_LIST)
        runesCount = len(self.RUNES_LIST)

        # get index list
        champIndexList = GetChampionIndex(champCount)
        skillIndexList = GetSkillIndex(skillCount)

        # generate output
        output = ""
        for i in range(self.TOTAL_PLAYER):
            outputPersonal = f"Player {i + 1}\n\
Champion: {self.CHAMPION_LIST[ champIndexList[i] ]}\n\
Skill1: {self.SKILL_LIST[ skillIndexList[i][0] ]}\n\
Skill2: {self.SKILL_LIST[ skillIndexList[i][1] ]}\n\
Item1: {self.ITEM_LIST[random.randint(0, itemCount - 1)]}\n\
Runes: {self.RUNES_LIST[random.randint(0, runesCount - 1)]}\n\n"
            output += outputPersonal

        # if spy mode triggered
        spyPlayer = random.randint(1, self.TOTAL_PLAYER)
        if self.SPY_MODE == "ON":
            output += f"Spy: Player {spyPlayer}\n"
        elif self.SPY_MODE == "ONLY SPY":
            output = f"Spy: Player {spyPlayer}\n"

        return output