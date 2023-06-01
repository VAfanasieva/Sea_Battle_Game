from src.Background import Background
from src.Game import Game
from src.players_field import PlayersField


def test_addCoorOfCrosses_positive():
    game = Game()
    back = Background()
    firedCell = (1, 2)
    player = PlayersField(0)
    back.coorOfCrosses = [(2, 4), (3, 7)]
    player.coordinatesForShots = [(1, 2), (7, 2)]
    game.addCoorOfCrosses(firedCell, player, back)
    assert back.coorOfCrosses == [(2, 4), (3, 7), (1, 2)]
    assert player.coordinatesForShots == [(7, 2)]


def test_addCoorOfCrosses_negative():
    game = Game()
    back = Background()
    firedCell = (1, 2)
    player = PlayersField(0)
    back.coorOfCrosses = [(1, 2), (3, 7)]
    player.coordinatesForShots = [(5, 6), (7, 2)]
    game.addCoorOfCrosses(firedCell, player, back)
    assert back.coorOfCrosses == [(1, 2), (3, 7)]
    assert player.coordinatesForShots == [(5, 6), (7, 2)]

