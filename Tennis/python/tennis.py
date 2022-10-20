# -*- coding: utf-8 -*-

class TennisGame:

    def __init__(self, player1Name, player2Name):
        self.player_1_name = player1Name
        self.player_2_name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player_1_name:
            self.p1points += 1
        elif player_name == self.player_2_name:
            self.p2points += 1
        else:
            raise Exception()

    def score(self):
        result = ""
        tempScore = 0
        if (self.p1points == self.p2points):
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
                3: "Forty-All",
            }.get(self.p1points, "Deuce")
        elif (self.p1points >= 4 or self.p2points >= 4):
            minusResult = self.p1points - self.p2points
            if (minusResult == 1):
                result = "Advantage " + self.player_1_name
            elif (minusResult == -1):
                result = "Advantage " + self.player_2_name
            elif (minusResult >= 2):
                result = "Win for " + self.player_1_name
            else:
                result = "Win for " + self.player_2_name
        else:
            for i in range(1, 3):
                if (i == 1):
                    tempScore = self.p1points
                else:
                    result += "-"
                    tempScore = self.p2points
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[tempScore]
        return result
