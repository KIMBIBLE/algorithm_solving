import sys
readline = lambda: sys.stdin.readline()

class GameMap:
    OCEAN = 1
    LAND = 0
    VISITED = 2

    def __init__(self, row, col):
        self.__gameMap = [[GameMap.OCEAN] * (col + 2)]
        for _ in range(row):
            line = [GameMap.OCEAN] + list(map(int, readline().split())) + [GameMap.OCEAN]
            self.__gameMap.append(line)
        self.__gameMap.append([GameMap.OCEAN] * (col + 2))


    def isValidPos(self, row, col):
        if self.__gameMap[row][col] == GameMap.LAND:
            return True

        return False


    def visit(self, row, col):
        self.__gameMap[row][col] = GameMap.VISITED


    def show(self):
        for line in self.__gameMap:
            print(line)



class Player:
    INVALID_POS = -1
    head_info = {
        0: (-1, 0),     # North
        1: (0, 1),      # East
        2: (1, 0),      # South
        3: (0, -1)      # West
    }


    def __init__(self, cur_row, cur_col, head):
        self.__row_pos = cur_row
        self.__col_pos = cur_col
        self.__cur_head = head
    

    @property
    def cur_head(self):
        return self.__cur_head


    def getCurrentPosition(self):
        return self.__row_pos, self.__col_pos


    def setNewPosition(self, row, col):
        self.__row_pos = row
        self.__col_pos = col


    def moveHead(self):
        if self.__cur_head == 0:
            self.__cur_head = 3

        else:
            self.__cur_head -= 1



class Game:
    def __init__(self, n, m, dx, dy, head):
        self.__visited_cnt = 0
        self.__trial_cnt = 0
        
        self.__gameMap = GameMap(n, m)
        cur_col = 1 + dx
        cur_row = 1 + dy
        if self.__gameMap.isValidPos(cur_row, cur_col):
            self.__gameMap.visit(cur_row, cur_col)
            self.addVisitedCnt()

        self.__player = Player(cur_row, cur_col, head)


    def showCurrentStatus(self):
        print('trial {}'.format(self.__trial_cnt))
        print('current head: {}'.format(self.__player.cur_head))
        print('current Pos: {}'.format(self.__player.getCurrentPosition()))
        print('move offset: {}'.format(Player.head_info[self.__player.cur_head]))
        print('visited cnt: {}'.format(self.visited_cnt))

        self.showCurrentMap()
        

    def showCurrentMap(self):
        self.__gameMap.show()


    @property
    def visited_cnt(self):
        return self.__visited_cnt


    def addVisitedCnt(self):
        self.__visited_cnt += 1


    def isPossibleToMove(self, row, col):
        if self.__gameMap.isValidPos(row, col):
            return True

        return False


    def goNextPosition(self):
        # head 돌리고, 이동을 반복함. (현재 head 기준으로, 북/서/남/동)
        for _ in range(4):
            self.__player.moveHead()
            self.__trial_cnt += 1
            self.showCurrentStatus()

            row_offset, col_offset = Player.head_info[self.__player.cur_head]
            row, col = self.__player.getCurrentPosition()
            next_row = row + row_offset
            next_col = col + col_offset
            print('Move to ({}, {})'.format(next_row, next_col))
            print('')

            # 이동 가능하면 이동하고, 이동이 불가능하면 head 돌리고 이동 작업을 다시 반복
            if self.isPossibleToMove(next_row, next_col):
                self.__player.setNewPosition(next_row, next_col)
                self.__gameMap.visit(next_row, next_col)
                self.addVisitedCnt()

                return self.__player.getCurrentPosition()

        # 시작 head 기준으로, 북/서/남/동 위치에 갈 곳이 남아있지 않은 경우
        return (Player.INVALID_POS, Player.INVALID_POS)

    def play(self):
        while True:
            x, y = self.goNextPosition()
            if x == Player.INVALID_POS and y == Player.INVALID_POS:
                break



if __name__ == '__main__':
    n, m = map(int, readline().split())
    
    dx, dy, head = map(int, readline().split())
    game = Game(n, m, dx, dy, head)
    game.play()
    print('visited cnt: {}'.format(game.visited_cnt))
    

