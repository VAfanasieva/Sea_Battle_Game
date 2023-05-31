from src.PlayersField import PlayersField


def test_addBlockShip_positive():
    player = PlayersField(12)
    direction = 1
    vector = 0
    coordinatesShip = [(1, 2)]
    coor = 1
    assert 1, 2 == player.addBlockToShip(coor, direction, vector, coordinatesShip)


def test_addBlockShip_negative():
    player = PlayersField(12)
    direction = -1
    vector = 0
    coordinatesShip = [(1, 2)]
    coor = 1
    assert 1, 2 == player.addBlockToShip(coor, direction, vector, coordinatesShip)
