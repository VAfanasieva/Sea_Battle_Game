from src.Background import Background
from src.Game import Game
from src.PlayersField import PlayersField


def test_addUnnecessaryCellsAfterTheShipIsKilled_add_one_cell():
    game = Game()
    back = Background()
    player = PlayersField(12)
    opponent = PlayersField(0)
    damagedCells = [(2, 2), (3, 2), (4, 2)]
    back.coorOfCrosses = [(2, 2), (3, 2), (4, 2)]
    back.coorOfUnnecessaryCells = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5)]
    player.coordinatesForShots = [(2, 1), (1, 2)]
    game.addUnnecessaryCellsAfterTheShipIsKilled(damagedCells, player, opponent, back)
    assert back.coorOfUnnecessaryCells.sort() == ([(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (1, 2)]).sort()
    assert player.coordinatesForShots.sort() == ([(2, 1)]).sort()


def test_addUnnecessaryCellsAfterTheShipIsKilled_add_one_cell_2():
    game = Game()
    back = Background()
    player = PlayersField(12)
    opponent = PlayersField(0)
    damagedCells = [(2, 2), (3, 2), (4, 2)]
    back.coorOfCrosses = [(2, 2), (3, 2), (4, 2)]
    back.coorOfUnnecessaryCells = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5)]
    player.coordinatesForShots = [(2, 1)]
    game.addUnnecessaryCellsAfterTheShipIsKilled(damagedCells, player, opponent, back)
    assert back.coorOfUnnecessaryCells.sort() == ([(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (1, 2)]).sort()
    assert player.coordinatesForShots.sort() == ([(2, 1)]).sort()


def test_addUnnecessaryCellsAfterTheShipIsKilled_going_beyond_borders():
    game = Game()
    back = Background()
    player = PlayersField(12)
    opponent = PlayersField(0)
    damagedCells = [(1, 1), (2, 1), (3, 1)]
    back.coorOfCrosses = [(1, 1), (2, 1), (3, 1)]
    back.coorOfUnnecessaryCells = [(1, 2), (2, 2), (3, 2), (4, 2)]
    player.coordinatesForShots = [(2, 1), (1, 2), (4, 1)]
    game.addUnnecessaryCellsAfterTheShipIsKilled(damagedCells, player, opponent, back)
    assert back.coorOfUnnecessaryCells.sort() == ([(1, 2), (2, 2), (3, 2), (4, 2), (4, 1)]).sort()
    assert player.coordinatesForShots.sort() == ([(2, 1), (1, 2)]).sort()


def test_addUnnecessaryCellsAfterTheShipIsKilled_going_beyond_borders_2():
    game = Game()
    back = Background()
    player = PlayersField(12)
    opponent = PlayersField(0)
    damagedCells = [(1, 1), (2, 1), (3, 1)]
    back.coorOfCrosses = [(1, 1), (2, 1), (3, 1)]
    back.coorOfUnnecessaryCells = [(1, 2), (2, 2), (3, 2), (4, 2)]
    player.coordinatesForShots = [(2, 1), (1, 2)]
    game.addUnnecessaryCellsAfterTheShipIsKilled(damagedCells, player, opponent, back)
    assert back.coorOfUnnecessaryCells.sort() == ([(1, 2), (2, 2), (3, 2), (4, 2), (4, 1)]).sort()
    assert player.coordinatesForShots.sort() == ([(2, 1), (1, 2)]).sort()


def test_addUnnecessaryCellsAfterTheShipIsKilled_not_add_cell():
    game = Game()
    back = Background()
    player = PlayersField(12)
    opponent = PlayersField(0)
    damagedCells = [(2, 2), (3, 2), (4, 2)]
    back.coorOfCrosses = [(2, 2), (3, 2), (4, 2)]
    back.coorOfUnnecessaryCells = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (1, 2)]
    player.coordinatesForShots = [(2, 1)]
    game.addUnnecessaryCellsAfterTheShipIsKilled(damagedCells, player, opponent, back)
    assert back.coorOfUnnecessaryCells.sort() == ([(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (1, 2)]).sort()
    assert player.coordinatesForShots.sort() == ([(2, 1)]).sort()