import pandas as pd

class Score:
    def __init__ (self):
        self.leaderboard = {}

    def addScore(self,player,score):
        if player in self.leaderboard:
            self.leaderboard[player].append(score)
            self.insertion_sort(player)
        else:
            self.leaderboard[player] = [score]

    def insertion_sort(self,player):

        if len(self.leaderboard[player])<=1:
            return

        for i in range(1, len(self.leaderboard[player])):
            key = self.leaderboard[player][i]
            j = i - 1
            while j >= 0 and key < self.leaderboard[player][j]:
                self.leaderboard[player][j+1] = self.leaderboard[player][j]
                j -= 1
            self.leaderboard[player][j+1] = key  

    def display(self):
        df = pd.DataFrame(self.leaderboard)
        return df.iloc[::-1].head(10).to_string(index = False)

    