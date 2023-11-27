import pandas as pd
import pickle

class Score:
    def __init__(self):
        self.leaderboard = []
        self.max = 0
        self.min = 0

    def insertion_sort(self):
        for i in range(1, len(self.leaderboard)):
            key = self.leaderboard[i]
            j = i - 1
            while j >= 0 and key[1] > self.leaderboard[j][1]:
                self.leaderboard[j + 1] = self.leaderboard[j]
                j -= 1
            self.leaderboard[j + 1] = key

    def save(self, name, score):
        if len(self.leaderboard) < 5:
            self.leaderboard.append([name, score])
            self.insertion_sort()
        else:
            pass

    def save_game(self, filename):
        game_data = {
            'leaderboard': self.leaderboard
        }

        with open(filename, 'wb') as file:
            pickle.dump(game_data, file)

    def load_game(self, filename):
        with open(filename, 'rb') as file:
            game_data = pickle.load(file)

        self.leaderboard = game_data['leaderboard']
        self.max = self.getMax()
        self.min = self.getMin()

    def display(self):
        if not self.leaderboard:
            data = pd.DataFrame(self.leaderboard, columns=["Name", "Score"])
        print(data)

    def display2(self):
        for value in self.leaderboard:
            print(value)
        

    def getMax(self):
        if not self.leaderboard:
            return None  # Return None if the leaderboard is empty
        self.insertion_sort()
        return self.leaderboard[0][1]

    def getMin(self):
        if not self.leaderboard:
            return None  # Return None if the leaderboard is empty
        self.insertion_sort()
        return self.leaderboard[-1][1]

    def check(self, value):
        min_score = self.getMin()
        max_score = self.getMax()

        # Check if leaderboard is not empty and value is within the range
        if min_score is not None and max_score is not None:
            return min_score < value < max_score
        elif min_score is None and max_score is None:
            # Empty leaderboard, consider any value within the range
            return True
        else:
            # One of min_score or max_score is None, indicating an inconsistent state
            return False

