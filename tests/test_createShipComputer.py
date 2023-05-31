from src.PlayersField import PlayersField


def test_createShipComputer_positive():
    player = PlayersField(12)
    numderOfCell = 2
    coordinatesFree = [(x, y) for x in range(1, 11) for y in range(1, 11)]
    assert len(player.createShipComputer(numderOfCell, coordinatesFree)) == 2


def test_createShipComputer_negative():
    player = PlayersField(12)
    numderOfCell = 2
    coordinatesFree = []
    assert len(player.createShipComputer(numderOfCell, coordinatesFree)) == 0