from src.players_field import PlayersField


def test_removeCoorFromFree_positive():
    player = PlayersField(0)
    coordinatesFreeAfterCreation = [(x, y) for x in range(1, 11) for y in range(1, 11)]
    ship = [(2, 2), (3, 2)]
    coordinatesFreeAfterCreation.remove((1, 1))
    coordinatesFreeAfterCreation.remove((2, 1))
    coordinatesFreeAfterCreation.remove((3, 1))
    coordinatesFreeAfterCreation.remove((4, 1))
    coordinatesFreeAfterCreation.remove((4, 2))
    coordinatesFreeAfterCreation.remove((4, 3))
    coordinatesFreeAfterCreation.remove((3, 3))
    coordinatesFreeAfterCreation.remove((2, 3))
    coordinatesFreeAfterCreation.remove((1, 3))
    coordinatesFreeAfterCreation.remove((1, 2))
    player.removeCoorFromFree(ship)
    assert player.coordinatesFree.sort() == coordinatesFreeAfterCreation.sort()


def test_removeCoorFromFree_going_beyond_borders():
    player = PlayersField(0)
    coordinatesFreeAfterCreation = [(x, y) for x in range(1, 11) for y in range(1, 11)]
    ship = [(1, 1)]
    coordinatesFreeAfterCreation.remove((2, 1))
    coordinatesFreeAfterCreation.remove((2, 2))
    coordinatesFreeAfterCreation.remove((1, 2))
    player.removeCoorFromFree(ship)
    assert player.coordinatesFree.sort() == coordinatesFreeAfterCreation.sort()


def test_removeCoorFromFree_cell_not_in_Free():
    player = PlayersField(0)
    coordinatesFreeAfterCreation = [(x, y) for x in range(1, 11) for y in range(1, 11)]
    player.coordinatesFree.remove((2, 1))
    ship = [(1, 1)]
    coordinatesFreeAfterCreation.remove((2, 2))
    coordinatesFreeAfterCreation.remove((1, 2))
    player.removeCoorFromFree(ship)
    assert player.coordinatesFree.sort() == coordinatesFreeAfterCreation.sort()

