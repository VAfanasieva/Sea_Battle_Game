import pytest

from src.Background import Background
from src.Game import Game
from src.players_field import PlayersField


def test_computerShots_positive():
    game = Game()
    back = Background()
    player = PlayersField(12)
    opponent = PlayersField(0)
    player.coordinatesForShots = [(1, 2), (5, 3), (7, 2), (4, 7), (8, 1)]
    player.computerNextShot = [(1, 2), (5, 3), (7, 2), (4, 7), (8, 1)]
    coorForShots = [(1, 2), (5, 3), (7, 2), (4, 7), (8, 1)]

    player.computerShots(game, opponent, coorForShots, back)
    assert len(player.coordinatesForShots) == 4
    assert len(player.computerNextShot) == 4


def test_computerShots_negative_1():
    game = Game()
    back = Background()
    player = PlayersField(12)
    opponent = PlayersField(0)
    player.coordinatesForShots = [(1, 2), (5, 3), (7, 2), (4, 7), (8, 1)]
    player.computerNextShot = []
    coorForShots = [(1, 2), (5, 3)]
    player.computerShots(game, opponent, coorForShots, back)
    assert len(player.coordinatesForShots) == 4
    assert len(player.computerNextShot) == 0


def test_computerShots_negative_2():
    game = Game()
    back = Background()
    player = PlayersField(12)
    opponent = PlayersField(0)
    player.coordinatesForShots = [(7, 2), (4, 7), (8, 1)]
    coorForShots = [(1, 2), (5, 3)]
    with pytest.raises(RecursionError):
        player.computerShots(game, opponent, coorForShots, back)


def test_computerShots_negative_3():
    game = Game()
    back = Background()
    player = PlayersField(12)
    opponent = PlayersField(0)
    coorForShots = [(x, y) for x in range(1, 8) for y in range(1, 8)]
    player.coordinatesForShots = [(7, 7)]
    player.computerShots(game, opponent, coorForShots, back, False)
    assert len(player.coordinatesForShots) == 0
    assert len(player.computerNextShot) == 3







