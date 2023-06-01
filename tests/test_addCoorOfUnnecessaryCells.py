from src.background import Background
from src.game import Game
from src.players_field import PlayersField


def test_addCoorOfUnnecessaryCells_all_diagonally():
    game = Game()
    back = Background()
    player = PlayersField(12)
    opponent = PlayersField(0)
    firedCell = (3, 2)
    back.coorOfCrosses = [(2, 4), (3, 7)]
    back.coorOfUnnecessaryCells = [(8, 5), (9, 5)]
    player.coordinatesForShots = [(2, 1), (7, 2), (1, 2), (4, 1), (2, 3), (4, 3)]
    game.addCoorOfUnnecessaryCells(firedCell, player, opponent, back)
    assert back.coorOfUnnecessaryCells.sort() == ([(8, 5), (9, 5), (1, 2), (4, 1), (2, 3), (4, 3)]).sort()
    assert player.coordinatesForShots.sort() == ([(2, 1), (7, 2)]).sort()


def test_addCoorOfUnnecessaryCells_all_around():
    game = Game()
    back = Background()
    player = PlayersField(12)
    opponent = PlayersField(0)
    firedCell = (3, 2)
    back.coorOfCrosses = [(2, 4), (3, 7)]
    back.coorOfUnnecessaryCells = [(8, 5), (9, 5)]
    player.coordinatesForShots = [(2, 1), (7, 2), (1, 2), (4, 1), (2, 3), (4, 3), (2, 2), (3, 1), (4, 2), (3, 3)]
    game.addCoorOfUnnecessaryCells(firedCell, player, opponent, back, False)
    assert back.coorOfUnnecessaryCells.sort() == ([(8, 5), (9, 5), (1, 2), (4, 1), (2, 3), (4, 3), (2, 2), (3, 1), (4, 2), (3, 3)]).sort()
    assert player.coordinatesForShots.sort() == ([(2, 1), (7, 2)]).sort()


def test_addCoorOfUnnecessaryCells_deletions_from_the_list_1():
    game = Game()
    back = Background()
    player = PlayersField(12)
    opponent = PlayersField(0)
    firedCell = (3, 2)
    back.coorOfCrosses = [(2, 4), (3, 7)]
    back.coorOfUnnecessaryCells = [(8, 5), (9, 5)]
    player.coordinatesForShots = [(2, 1), (7, 2)]
    game.addCoorOfUnnecessaryCells(firedCell, player, opponent, back)
    assert back.coorOfUnnecessaryCells.sort() == ([(8, 5), (9, 5), (1, 2), (4, 1), (2, 3), (4, 3)]).sort()
    assert player.coordinatesForShots.sort() == ([(2, 1), (7, 2)]).sort()


def test_addCoorOfUnnecessaryCells_deletions_from_the_list_2():
    game = Game()
    back = Background()
    player = PlayersField(12)
    opponent = PlayersField(0)
    firedCell = (3, 2)
    back.coorOfCrosses = [(2, 4), (3, 7)]
    back.coorOfUnnecessaryCells = [(8, 5), (9, 5)]
    player.coordinatesForShots = [(2, 1), (7, 2)]
    game.addCoorOfUnnecessaryCells(firedCell, player, opponent, back, False)
    assert back.coorOfUnnecessaryCells.sort() == ([(8, 5), (9, 5), (1, 2), (4, 1), (2, 3), (4, 3)]).sort()
    assert player.coordinatesForShots.sort() == ([(2, 1), (7, 2)]).sort()


def test_addCoorOfUnnecessaryCells_going_beyond_borders_y_1():
    game = Game()
    back = Background()
    player = PlayersField(12)
    opponent = PlayersField(0)
    firedCell = (1, 2)
    back.coorOfCrosses = [(7, 4), (3, 9)]
    back.coorOfUnnecessaryCells = [(8, 5), (9, 5)]
    player.coordinatesForShots = [(2, 1), (7, 2), (1, 2), (3, 2)]
    game.addCoorOfUnnecessaryCells(firedCell, player, opponent, back)
    assert back.coorOfUnnecessaryCells.sort() == ([(8, 5), (9, 5), (1, 2), (3, 2)]).sort()
    assert player.coordinatesForShots.sort() == ([(2, 1), (7, 2)]).sort()


def test_addCoorOfUnnecessaryCells_going_beyond_borders_y_2():
    game = Game()
    back = Background()
    player = PlayersField(12)
    opponent = PlayersField(0)
    firedCell = (1, 2)
    back.coorOfCrosses = [(7, 4), (3, 9)]
    back.coorOfUnnecessaryCells = [(8, 5), (9, 5)]
    player.coordinatesForShots = [(2, 1), (7, 2), (1, 1), (1, 2), (2, 2), (3, 2), (3, 1)]
    game.addCoorOfUnnecessaryCells(firedCell, player, opponent, back)
    assert back.coorOfUnnecessaryCells.sort() == ([(8, 5), (9, 5), (1, 1), (1, 2), (2, 2), (3, 2), (3, 1)]).sort()
    assert player.coordinatesForShots.sort() == ([(2, 1), (7, 2)]).sort()


def test_addCoorOfUnnecessaryCells_going_beyond_borders_x_1():
    game = Game()
    back = Background()
    player = PlayersField(12)
    opponent = PlayersField(0)
    firedCell = (1, 4)
    back.coorOfCrosses = [(9, 8), (3, 7)]
    back.coorOfUnnecessaryCells = [(8, 5), (9, 5)]
    player.coordinatesForShots = [(2, 1), (7, 2), (2, 3), (2, 5)]
    game.addCoorOfUnnecessaryCells(firedCell, player, opponent, back)
    assert back.coorOfUnnecessaryCells.sort() == ([(8, 5), (9, 5), (2, 3), (2, 5)]).sort()
    assert player.coordinatesForShots.sort() == ([(2, 1), (7, 2)]).sort()


def test_addCoorOfUnnecessaryCells_going_beyond_borders_x_2():
    game = Game()
    back = Background()
    player = PlayersField(12)
    opponent = PlayersField(0)
    firedCell = (1, 4)
    back.coorOfCrosses = [(9, 8), (3, 7)]
    back.coorOfUnnecessaryCells = [(8, 5), (9, 5)]
    player.coordinatesForShots = [(2, 1), (7, 2), (2, 3), (2, 5), (1, 3), (2, 4), (1, 5)]
    game.addCoorOfUnnecessaryCells(firedCell, player, opponent, back)
    assert back.coorOfUnnecessaryCells.sort() == ([(8, 5), (9, 5), (2, 3), (2, 5),  (1, 3), (2, 4), (1, 5)]).sort()
    assert player.coordinatesForShots.sort() == ([(2, 1), (7, 2)]).sort()


def test_addCoorOfUnnecessaryCells_tuples_are_in_the_list_coorOfCrosses_1():
    game = Game()
    back = Background()
    player = PlayersField(12)
    opponent = PlayersField(0)
    firedCell = (3, 2)
    back.coorOfCrosses = [(2, 4), (3, 7), (1, 2), (4, 1), (2, 3), (4, 3)]
    back.coorOfUnnecessaryCells = [(8, 5), (9, 5)]
    player.coordinatesForShots = [(2, 1), (7, 2), (1, 2), (4, 1), (2, 3), (4, 3)]
    game.addCoorOfUnnecessaryCells(firedCell, player, opponent, back)
    assert back.coorOfUnnecessaryCells.sort() == ([(8, 5), (9, 5)]).sort()
    assert player.coordinatesForShots.sort() == ([(2, 1), (7, 2)]).sort()


def test_addCoorOfUnnecessaryCells_tuples_are_in_the_list_coorOfCrosses_2():
    game = Game()
    back = Background()
    player = PlayersField(12)
    opponent = PlayersField(0)
    firedCell = (3, 2)
    back.coorOfCrosses = [(2, 4), (3, 7), (1, 2), (4, 1), (2, 3), (4, 3), (2, 2), (3, 1), (4, 2), (3, 3)]
    back.coorOfUnnecessaryCells = [(8, 5), (9, 5)]
    player.coordinatesForShots = [(2, 1), (7, 2), (1, 2), (4, 1), (2, 3), (4, 3), (2, 2), (3, 1), (4, 2), (3, 3)]
    game.addCoorOfUnnecessaryCells(firedCell, player, opponent, back, False)
    assert back.coorOfUnnecessaryCells.sort() == ([(8, 5), (9, 5)]).sort()
    assert player.coordinatesForShots.sort() == ([(2, 1), (7, 2)]).sort()


def test_addCoorOfUnnecessaryCells_tuples_are_in_the_list_coorOfUnnecessaryCells_1():
    game = Game()
    back = Background()
    player = PlayersField(12)
    opponent = PlayersField(0)
    firedCell = (3, 2)
    back.coorOfCrosses = [(2, 4), (3, 7)]
    back.coorOfUnnecessaryCells = [(8, 5), (9, 5), (1, 2), (4, 1), (2, 3), (4, 3)]
    player.coordinatesForShots = [(2, 1), (7, 2), (1, 2), (4, 1), (2, 3), (4, 3)]
    game.addCoorOfUnnecessaryCells(firedCell, player, opponent, back)
    assert back.coorOfUnnecessaryCells.sort() == ([(8, 5), (9, 5), (1, 2), (4, 1), (2, 3), (4, 3)]).sort()
    assert player.coordinatesForShots.sort() == ([(2, 1), (7, 2)]).sort()


def test_addCoorOfUnnecessaryCells_tuples_are_in_the_list_coorOfUnnecessaryCells_2():
    game = Game()
    back = Background()
    player = PlayersField(12)
    opponent = PlayersField(0)
    firedCell = (3, 2)
    back.coorOfCrosses = [(2, 4), (3, 7)]
    back.coorOfUnnecessaryCells = [(8, 5), (9, 5), (1, 2), (4, 1), (2, 3), (4, 3), (2, 2), (3, 1), (4, 2), (3, 3)]
    player.coordinatesForShots = [(2, 1), (7, 2), (1, 2), (4, 1), (2, 3), (4, 3), (2, 2), (3, 1), (4, 2), (3, 3)]
    game.addCoorOfUnnecessaryCells(firedCell, player, opponent, back, False)
    assert back.coorOfUnnecessaryCells.sort() == ([(8, 5), (9, 5), (1, 2), (4, 1), (2, 3), (4, 3), (2, 2), (3, 1), (4, 2), (3, 3)]).sort()
    assert player.coordinatesForShots.sort() == ([(2, 1), (7, 2)]).sort()





