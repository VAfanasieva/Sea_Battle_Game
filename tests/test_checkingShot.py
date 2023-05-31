from src.Background import Background
from src.Game import Game
from src.PlayersField import PlayersField


def test_checkingShot_miss():
    game = Game()
    back = Background()
    player = PlayersField(12)
    opponent = PlayersField(0)
    opponent.coorLiveCell = [[(1, 2), (5, 3)], [(2, 5)]]
    firedCell = (7, 3)
    assert False == game.checkingShot(firedCell, player, opponent, False, back)


def test_checkingShot_human_killed():
    game = Game()
    back = Background()
    player = PlayersField(12)
    opponent = PlayersField(0)
    opponent.coorLiveCell = [[(1, 2)], [(2, 5), (3, 5)]]
    firedCell = (1, 2)
    assert True == game.checkingShot(firedCell, player, opponent, False, back)
    assert back.coorOfCrosses.sort() == ([(1, 2)]).sort()
    assert back.coorOfUnnecessaryCells.sort() == ([(1, 1), (2, 2), (1, 3), (2, 1), (2, 3)]).sort()
    assert opponent.shipsKilled == [[(1, 2)]]
    assert player.numberOfEnemyShipsKilled == 1


def test_checkingShot_human_hit():
    game = Game()
    back = Background()
    player = PlayersField(12)
    opponent = PlayersField(0)
    opponent.coorLiveCell = [[(1, 2), (1, 3)], [(2, 5), (3, 5)]]
    firedCell = (1, 2)
    assert True == game.checkingShot(firedCell, player, opponent, False, back)
    assert back.coorOfCrosses.sort() == ([(1, 2)]).sort()
    assert back.coorOfUnnecessaryCells.sort() == ([(2, 1), (2, 3)]).sort()
    assert opponent.shipsKilled == []
    assert player.numberOfEnemyShipsKilled == 0


def test_checkingShot_computer_killed():
    game = Game()
    back = Background()
    player = PlayersField(12)
    opponent = PlayersField(0)
    player.computerNextShot = [(1, 2), (2, 3)]
    opponent.coorLiveCell = [[(1, 2)], [(2, 5), (3, 5)]]
    firedCell = (1, 2)
    assert True == game.checkingShot(firedCell, player, opponent, True, back)
    assert back.coorOfCrosses.sort() == ([(1, 2)]).sort()
    assert back.coorOfUnnecessaryCells.sort() == ([(1, 1), (2, 2), (1, 3), (2, 1), (2, 3)]).sort()
    assert player.computerNextShot == []
    assert player.numberOfEnemyShipsKilled == 1


def test_checkingShot_computer_hit():
    game = Game()
    back = Background()
    player = PlayersField(12)
    opponent = PlayersField(0)
    opponent.coorLiveCell = [[(1, 2), (1, 3)], [(2, 5), (3, 5)]]
    firedCell = (1, 2)
    assert True == game.checkingShot(firedCell, player, opponent, True, back)
    assert back.coorOfCrosses.sort() == ([(1, 2)]).sort()
    assert back.coorOfUnnecessaryCells.sort() == ([(2, 1), (2, 3)]).sort()
    assert player.computerNextShot.sort() == ([(1, 1), (2, 2), (1, 3)]).sort()