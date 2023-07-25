import math


class Player:
    """
    The purpose of this class is to allow the creation of multiple players.
    Variables:
    - Name: plyear name
    - Height: player height
    - Weight:player weight
    """
    def __init__(self, name: str, height: int, weight: float, bmi: float) -> None:
        self.name = name
        self.height = height
        self.weight = weight
        self.bmi = bmi

    def playerPrint(self):
        """
        This method print all the 4 information about each player of the team.
        """
        return f"{self.name} ---- {self.height} cm ---- {self.weight} kg ---- {self.bmi:.1f} kg/m\u00B2"
    

class Team:
    """
    This class purpose is to add the amount of players to a team as the user wants.
    Them creates a list with all the informations for each player.
    """

    def __init__(self, tn: str) -> None:
        self.teamName = tn
    players = []
    
    def addplayer(self):
        """
        """
        name = input("Insert player name: (to escape insert 'exit') ")
        while name.lower() != "exit":
            h = int(input("Insert the height in cm: "))
            w = float(input("Insert the weight in kg: "))
            bmi = w / (math.pow((h/100), 2))
            p = Player(name, h, w, bmi)
            self.players.append(p)
            name = input("Insert player name: (to escape insert 'exit') ")

    def listing(self):
        """
        """
        for p in self.players:
            print(p.playerPrint())



if __name__ == "__main__":
    T = Team(input("What is the team name? "))
    T.addplayer()
    T.listing()