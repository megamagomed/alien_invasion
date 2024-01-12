from pathlib import Path


class GameStats:
    def __init__(self, ai_game):
        self.path = Path("hi_score.txt")
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = int(self.path.read_text())

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
