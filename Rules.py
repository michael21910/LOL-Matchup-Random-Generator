class Rules:
    def __init__(self):
        self.rules = """
- Dropdown selections:
    - Total Player: 1 ~ 10
    - Game Mode: Normal Game (NG), All Random (AR)
    - Spy: ON, OFF, ONLY SPY

- What does the button do?
    - Clear MatchUp Information: Clears the matchup information, that is, the right side of the screen.
    - Generate MatchUp: Generates the matchup information at the right side of the screen according to your selection.
    - Copy MatchUp Information: Copy the matchup information to the clipboard.
    - Export files to matchup.txt: Export the matchup information to a file called matchup.txt, you can find it at the same folder as the main.exe file.

- Game Modes
    - Normal Game (NG): Normal game in LOL, randomized factor are: champion, skills, first item, and runes.
    - All Random (AR): All random game in LOL, randomized factor are: champion, skills, first item, and runes.
    - Both game modes can have the spy mode ON or OFF.
    - Only Spy: The game mode where one of the player will be assigned to the spy role. This function only provides the spy role, no other factors are randomized.
"""

    def GetRules(self):
        rulesLineSplit = self.rules.split("\n")
        returnRules = ""
        for i in range(1, len(rulesLineSplit)):
            returnRules += rulesLineSplit[i] + "\n"
        return returnRules