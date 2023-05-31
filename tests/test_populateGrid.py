from src.PlayersField import PlayersField


def test_populateGrid_positive():
    player = PlayersField(12)
    player.populateGrid()
    assert len(player.coorOwnShips) == 10
    assert len(player.coorLiveCell) == 10

