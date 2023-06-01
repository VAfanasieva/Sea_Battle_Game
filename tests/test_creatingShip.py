from src.players_field import PlayersField
from src.Background import Background


def test_creatingShip_positive():
    player = PlayersField(0)
    nowBack = Background()
    assert player.creatingShip(244, 190, 309, 203, nowBack).sort() == [(2, 2), (3, 2), (4, 2)].sort()


def test_creatingShip_negative():
    player = PlayersField(0)
    nowBack = Background()
    assert player.creatingShip(244, 190, 405, 203, nowBack) == []       # слишком большой по Х
    assert player.creatingShip(244, 190, 157, 457, nowBack) == []       # слишком большой по У


def test_creatingShip_negative_1():
    player = PlayersField(0)
    nowBack = Background()
    assert player.creatingShip(244, 79, 309, 87, nowBack) == []        # за пределами сетки по У
    assert player.creatingShip(156, 190, 264, 203, nowBack) == []       # за пределами сетки по Х


def test_creatingShip_boundary_points():
    player = PlayersField(0)
    nowBack = Background()
    assert player.creatingShip(210, 150, 239, 179, nowBack) == []
    assert player.creatingShip(240, 180, 270, 210, nowBack) == []
    assert player.creatingShip(240, 180, 269, 209, nowBack) == []


