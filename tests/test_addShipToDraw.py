from src.players_field import PlayersField
from src.background import Background


def test_addShipToDraw_positive():
    player = PlayersField(0)
    nowBack = Background()
    numberOfDowned = [0, 0, 0, 0]
    tempShip = [(1, 1), (1, 2)]
    player.addShipToDraw(tempShip, numberOfDowned, nowBack)
    assert player.coorOwnShips == [[(1, 1), (1, 2)]]
    assert player.coorLiveCell == [[(1, 1), (1, 2)]]


def test_addShipToDraw_quantity_tracking():
    player = PlayersField(0)
    nowBack = Background()
    player.coorOwnShips.append([(3, 4), (4, 4), (5, 4), (6, 4)])
    player.coorLiveCell.append([(3, 4), (4, 4), (5, 4), (6, 4)])
    numberOfDowned = [0, 0, 0, 1]
    tempShip = [(1, 1), (1, 2), (1, 3), (1, 4)]
    player.addShipToDraw(tempShip, numberOfDowned, nowBack)
    assert player.coorOwnShips == [[(3, 4), (4, 4), (5, 4), (6, 4)]]
    assert player.coorLiveCell == [[(3, 4), (4, 4), (5, 4), (6, 4)]]


def test_addShipToDraw_negative():
    player = PlayersField(0)
    nowBack = Background()
    player.coorOwnShips.append([(3, 4), (4, 4), (5, 4), (6, 4)])
    player.coorLiveCell.append([(3, 4), (4, 4), (5, 4), (6, 4)])
    player.removeCoorFromFree([(3, 4), (4, 4), (5, 4), (6, 4)])
    numberOfDowned = [0, 0, 0, 1]
    tempShip = [(2, 3), (2, 4)]
    player.addShipToDraw(tempShip, numberOfDowned, nowBack)
    assert player.coorOwnShips == [[(3, 4), (4, 4), (5, 4), (6, 4)]]
    assert player.coorLiveCell == [[(3, 4), (4, 4), (5, 4), (6, 4)]]