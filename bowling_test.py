import unittest
import bowling_game


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = bowling_game.BowlingGame()

    def test_gutter(self):
        game = bowling_game.BowlingGame()
        for i in range (20):
            game.roll(0)
        assert game.score() == 0

    def test_all_ones(self):
        game = bowling_game.BowlingGame()
        for i in range(20):
            game.roll(1)
            assert game.score() == 20

    def test_one_spare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.roll_many(0, 17)
        assert self.game.score() == 16

    def test_one_strike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.roll_many(0, 16)
        assert self.game.score() == 24

    def perfect_game_test(self):
        self.rollMany(10, 12)
        assert self.game.score() == 300

    def test_all_spares(self):
        self.rollMany(5, 21)
        assert self.game.score() == 150


    def roll_many(self, pins, rolls):
        for i in range(rolls):
            self.game.roll(pins)