from src.Background import Background
from src.Game import Game
from src.players_field import PlayersField


def test_addPointCoor_positive():
    game = Game()
    back = Background()
    firedCell = (1, 2)
    player = PlayersField(0)
    back.coorOfPoints = [(2, 4), (3, 7)]
    player.coordinatesForShots = [(1, 2), (7, 2)]
    game.addPointCoor(firedCell, player, back)
    assert back.coorOfPoints == [(2, 4), (3, 7), (1, 2)]
    assert player.coordinatesForShots == [(7, 2)]


def test_addPointCoor_negative():
    game = Game()
    back = Background()
    firedCell = (1, 2)
    player = PlayersField(0)
    back.coorOfPoints = [(1, 2), (3, 7)]
    player.coordinatesForShots = [(5, 6), (7, 2)]
    game.addPointCoor(firedCell, player, back)
    assert back.coorOfPoints == [(1, 2), (3, 7)]
    assert player.coordinatesForShots == [(5, 6), (7, 2)]