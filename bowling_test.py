import unittest
import bowling_game

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = bowling_game.BowlingGame()

    def testGutterGame(self):
        game = bowling_game.BowlingGame()
        for i in range (20):
            game.roll(0)
        assert game.score() == 0

    def testAllOnes(self):
        game = bowling_game.BowlingGame()
        for i in range(20):
            game.roll(1)
            assert game.score() == 20

    def testOneSpare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0, 17)
        assert self.game.score() == 16

    def testOneStrike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0, 16)
        assert self.game.score() == 24

    def perfectGameTest(self):
        self.rollMany(10, 12)
        assert self.game.score() == 300

    def testAllSpares(self):
        self.rollMany(5, 21)
        assert self.game.score() == 150


    def rollMany(self, pins, rolls):
        for i in range(rolls):
            self.game.roll(pins)