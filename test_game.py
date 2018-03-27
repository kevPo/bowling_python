from unittest import TestCase

from Game import Game


class TestGame(TestCase):

    def setUp(self):
        self.game = Game()

    def roll_many(self, rolls, pins):
        for i in range(rolls):
            self.game.roll(pins)

    def test_all_gutters_returns_zero(self):
        self.roll_many(20, 0)

        assert self.game.score == 0

    def test_all_ones_returns_20(self):
        self.roll_many(20, 1)

        assert self.game.score == 20

    def test_spare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(2)
        self.roll_many(17, 0)

        assert self.game.score == 14

    def test_strike(self):
        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(4)
        self.roll_many(16, 0)

        assert self.game.score == 24

    def test_perfect_game(self):
        self.roll_many(12, 10)

        assert self.game.score == 300
