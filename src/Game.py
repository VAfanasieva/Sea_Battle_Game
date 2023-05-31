from src.PlayersField import PlayersField


class Game:
    def __init__(self):
        pass

    def addCoorOfCrosses(self, firedCell, playr, back):
        """добавляет координаты крестиков и удаляет эти коорлинаты из доступных для выстрелов"""
        if firedCell not in back.coorOfCrosses:
            back.coorOfCrosses.append(firedCell)
        if firedCell in playr.coordinatesForShots:
            playr.coordinatesForShots.remove(firedCell)

    def addPointCoor(self, firedCell, playr, back):
        """добавляет координаты точкек и удаляет эти коорлинаты из доступных для выстрелов"""
        if firedCell not in back.coorOfPoints:
            back.coorOfPoints.append(firedCell)
        if firedCell in playr.coordinatesForShots:
            playr.coordinatesForShots.remove(firedCell)

    def addCoorOfUnnecessaryCells(self, firedCell, playr, opponent, back, diagonalOnly=True):
        """добавляет координаты ненужных клеток - тех, в которых точно нет корабля
        и удаляет эти коорлинаты из доступных для выстрелов"""
        arrayUnnecessaryCells = []
        x, y = firedCell
        arrayUnnecessaryCells.append((x + 1, y + 1))
        arrayUnnecessaryCells.append((x - 1, y + 1))
        arrayUnnecessaryCells.append((x + 1, y - 1))
        arrayUnnecessaryCells.append((x - 1, y - 1))
        if not diagonalOnly:
            arrayUnnecessaryCells.append((x + 1, y))
            arrayUnnecessaryCells.append((x - 1, y))
            arrayUnnecessaryCells.append((x, y - 1))
            arrayUnnecessaryCells.append((x, y + 1))
        for firedCell in arrayUnnecessaryCells:
            if firedCell not in back.coorOfUnnecessaryCells and firedCell not in back.coorOfCrosses and (
                    1 + opponent.offset) <= firedCell[0] <= (10 + opponent.offset) and 1 <= firedCell[1] <= 10:
                back.coorOfUnnecessaryCells.append(firedCell)
            if firedCell in playr.coordinatesForShots:
                playr.coordinatesForShots.remove(firedCell)

    def addUnnecessaryCellsAfterTheShipIsKilled(self, damagedCells, playr, opponent, back):
        """после убитого корабля проходится по всем его клеткам и
        все клетки вокруг их добавляет в массив с ненужными клетками
        и удаляет эти коорлинаты из доступных для выстрелов"""
        for ship in damagedCells:
            cell = (ship[0] + 1, ship[1])
            if (cell not in back.coorOfUnnecessaryCells) and (cell not in back.coorOfCrosses) and (
                    (1 + opponent.offset) <= cell[0] <= (10 + opponent.offset) and 1 <= cell[1] <= 10):
                back.coorOfUnnecessaryCells.append(cell)
                if cell in playr.coordinatesForShots:
                    playr.coordinatesForShots.remove(cell)

            cell = (ship[0] - 1, ship[1])
            if (cell not in back.coorOfUnnecessaryCells) and (cell not in back.coorOfCrosses) and (
                    (1 + opponent.offset) <= cell[0] <= (10 + opponent.offset) and 1 <= cell[1] <= 10):
                back.coorOfUnnecessaryCells.append(cell)
                if cell in playr.coordinatesForShots:
                    playr.coordinatesForShots.remove(cell)

            cell = (ship[0], ship[1] - 1)
            if (cell not in back.coorOfUnnecessaryCells) and (cell not in back.coorOfCrosses) and (
                    (1 + opponent.offset) <= cell[0] <= (10 + opponent.offset) and 1 <= cell[1] <= 10):
                back.coorOfUnnecessaryCells.append(cell)
                if cell in playr.coordinatesForShots:
                    playr.coordinatesForShots.remove(cell)

            cell = (ship[0], ship[1] + 1)
            if (cell not in back.coorOfUnnecessaryCells) and (cell not in back.coorOfCrosses) and (
                    (1 + opponent.offset) <= cell[0] <= (10 + opponent.offset) and 1 <= cell[1] <= 10):
                back.coorOfUnnecessaryCells.append(cell)
                if cell in playr.coordinatesForShots:
                    playr.coordinatesForShots.remove(cell)

    def checkingShot(self, firedCell, playr, opponent, computerTurn, back):
        """проверяет выстрел игрока, возвращает в соответвие с выстрелом True или False"""
        for ship in range(len(opponent.coorLiveCell)):
            if firedCell in opponent.coorLiveCell[ship]:
                self.addCoorOfCrosses(firedCell, playr, back)
                self.addCoorOfUnnecessaryCells(firedCell, playr, opponent, back)
                if len(opponent.coorLiveCell[ship]) == 1:
                    self.addCoorOfUnnecessaryCells(firedCell, playr, opponent, back, diagonalOnly=False)
                opponent.damagedCells[ship].append(firedCell)
                opponent.coorLiveCell[ship].remove(firedCell)
                if computerTurn:
                    if len(opponent.coorLiveCell[ship]) == 0:
                        self.addUnnecessaryCellsAfterTheShipIsKilled(opponent.damagedCells[ship], playr, opponent, back)
                        playr.computerNextShot.clear()
                        playr.numberOfEnemyShipsKilled += 1
                    else:
                        if firedCell[0] + 1 <= 10:
                            playr.computerNextShot.append((firedCell[0] + 1, firedCell[1]))
                        if firedCell[1] + 1 <= 10:
                            playr.computerNextShot.append((firedCell[0], firedCell[1] + 1))
                        if firedCell[0] - 1 >= 1:
                            playr.computerNextShot.append((firedCell[0] - 1, firedCell[1]))
                        if firedCell[1] - 1 >= 1:
                            playr.computerNextShot.append((firedCell[0], firedCell[1] - 1))
                else:
                    if len(opponent.coorLiveCell[ship]) == 0:
                        self.addUnnecessaryCellsAfterTheShipIsKilled(opponent.damagedCells[ship], playr, opponent, back)
                        opponent.shipsKilled.append(opponent.damagedCells[ship])
                        back.drawShips(opponent.shipsKilled)
                        playr.numberOfEnemyShipsKilled += 1
                return True

        self.addPointCoor(firedCell, playr, back)
        return False

