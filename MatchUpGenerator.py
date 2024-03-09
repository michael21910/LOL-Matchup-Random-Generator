import random
import time
import os

class MatchUpGenerator:
    def __init__(self, playerCount, mode):
        self.PLAYERCOUNT = playerCount
        self.MODE = mode
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
        if self.MODE == "NG":
            self.SKILL_LIST = VariableSetUpByFile(os.path.join(current_directory, "factorTextFile", "skillsNG.txt"))
            self.ITEM_LIST = VariableSetUpByFile(os.path.join(current_directory, "factorTextFile", "itemsNG.txt"))
        elif self.MODE == "AR":
            self.SKILL_LIST = VariableSetUpByFile(os.path.join(current_directory, "factorTextFile", "skillsAR.txt"))
            self.ITEM_LIST = VariableSetUpByFile(os.path.join(current_directory, "factorTextFile", "itemsAR.txt"))
        self.RUNES_LIST = VariableSetUpByFile(os.path.join(current_directory, "factorTextFile", "runes.txt"))

    # return matchup information
    def GenerateMatchUp(self):

        # get champion index, no repeat
        # return list of numbers
        def GetChampionIndex(champCount):
            return random.sample(range(0, champCount), self.PLAYERCOUNT)
        
        # get skill index
        # return: [ [player 1 skill 1, player 1 skill 2], [], [], [], ... ]
        def GetSkillIndex(skillCount):
            allPlayerSkillIndex = list()
            for _ in range(self.PLAYERCOUNT):
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
        for i in range(self.PLAYERCOUNT):
            outputPersonal = f"Player {i + 1}\n\
Champion: {self.CHAMPION_LIST[ champIndexList[i] ]}\n\
Skill1: {self.SKILL_LIST[ skillIndexList[i][0] ]}\n\
Skill2: {self.SKILL_LIST[ skillIndexList[i][1] ]}\n\
Item1: {self.ITEM_LIST[random.randint(0, itemCount - 1)]}\n\
Runes: {self.RUNES_LIST[random.randint(0, runesCount - 1)]}\n\n"
            output += outputPersonal

        return output