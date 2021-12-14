class State:
    # 1 - P1's turn, 2 - P2's turn, 0 - No longer playing.
    def __init__(self, turn: int) -> None:
        self.turn: int = turn
        self.round: int = 0
        self.board: list[str] = ["" for i in range(0,25)]
        self.move: str = ""
        # [p1 normal pieces, p1 capstones, p2 normal pieces, p2 capstone]
        self.pieces: list[int] = [21,1,21,1]

def index(x:int,y:int) -> int:
    return x + y * 5

def assignMoves(state: State) -> str:
    if state.turn == 1:
        move = p1(state)
    else:
        move = p2(state)
    return move

def direction(x: int,y: int,direct: chr) -> (int,int):
    match direct:
        case 'u':
            return (x,y-1)
        case 'd':
            return (x,y+1)
        case 'l':
            return (x-1,y)
        case 'r':
            return (x+1,y)
        case '_':
            raise Exception("panic - weird Direction")
    return (0,0)



# TODO Move Piece and add piece counter
def movePiece(state: State) -> State:
    moveStr = state.move
    if moveStr[0] == 'n':
        piece: chr = moveStr[1]
        x,y = ord(moveStr[2])-97, int(moveStr[3])
        if state.board[index(x,y)] != "": raise Exception("panic not emp: " + state.board[index(x,y)] + " " + str(x) + str(y))
        state.board[index(x,y)] = piece
        state.move = ""
        return state
    if moveStr[0] == 'm':
        carry: int = ord(moveStr[1])
        x,y = ord(moveStr[2])-97,int(moveStr[3])
        (newX,newY) = direction(x,y,moveStr[4])
        # TODO Flatten Wall
        move: str = state.board[index(x,y)][:carry+1]
        state.board[index(x,y)] = state.board[index(x,y)][carry+1:]
        state.board[index(newX,newY)] = move + state.board[index(newX,newY)]
        moveMore: str = moveStr[5:]
        oldX,oldY = newX,newY
        while len(moveMore) > 0:
            carryMore: int = int(moveMore[0])
            (moreX,moreY) = direction(oldX,oldY,moveMore[1])
            moreMove: str = state.board[index(oldX,oldY)][:carryMore+1]
            state.board[index(oldX,oldY)] = state.board[index(oldX,oldY)][carryMore+1:]
            state.board[index(moreX,moreY)] = moreMove + state.board[index(moreX,moreY)]
            moveMore = moveMore[2:]
            oldX,oldY = moreX,moreY
    state.move = ""
    return state

def checkDone(state: State) -> (bool, int):
    player: int = 0
    winner: int = 0
    outcome: list[bool] = [False,False]
    for mask in [genMask(state.board,1),genMask(state.board,2)]:
        x: int = 0
        y: int = 0
        skipCurrent: bool = False
        while (y < 5):
            checkHor: bool = dfs(mask,x,y,[4,9,14,19,24],[])
            if checkHor: 
                outcome[player] = True
                break
            y = y+1
        y = 0
        while (x < 5):
            if outcome[player]: break
            checkVer: bool = dfs(mask,x,y,[20,21,22,23,24],[])
            if checkVer:
                outcome[player] = True
                break
            x = x+1
        player = player + 1
    # 0 - draw, -1 = P1 wins, -2 = P2 wins
    if outcome[0] and outcome[1]:
        return (True, 0)
    elif outcome[0]:
        return (True, -1)
    elif outcome[1]:
        return (True, -2)
    return (False, 0)

# Generates a boolean mask for each player
def genMask(board: list[str], turn: int) -> list[bool]:
    if turn == 1:
        piece = 'O'
    elif turn == 2:
        piece = 'X'
    capstone = str(turn)
    retBoard: list[bool] = [False for i in range(0,25)] 
    x: int = 0
    y: int = 0
    while y < 5:
        while x < 5:
            if (board[index(x,y)][:1] == piece) or (board[index(x,y)][:1] == capstone):
                retBoard[index(x,y)] = True
            x = x+1
        x = 0
        y = y+1
    
    return retBoard

# Runs a depth-first search from a starting pos to a target pos
def dfs(mask: list[bool], x: int, y: int, succ: list[int], visited: list[int]) -> bool:
    if not mask[index(x,y)]:
        return False
    if index(x,y) in succ:
        return True
    visited = visited + [index(x,y)]
    explored: list[bool] = []
    # Check left
    if (x > 0) and not (index(x-1,y) in visited):
        explored = explored + [dfs(mask,x-1,y,succ,visited)]
    # Check Right
    if (x < 4) and not (index(x+1,y) in visited):
        explored = explored + [dfs(mask,x+1,y,succ,visited)]
    # Check Up
    if (y > 0) and not (index(x,y-1) in visited):
        explored = explored + [dfs(mask,x,y-1,succ,visited)]
    # Check Down
    if (y < 4) and not (index(x, y+1) in visited):
        explored = explored + [dfs(mask,x,y+1,succ,visited)]
    if True in explored:
        return True
    return False

def incTurn(state: State) -> State:
    (isDone, winner) = checkDone(state)
    if not isDone:
        if state.turn == 1:
            state.turn = 2
        elif state.turn == 2:
            state.turn = 1
        state.round = state.round + 1
    else:
        state.turn = winner   
    return state

# TODO
def p1(state: State) -> str:
    moves = listMoves(state)
    return moves[0]

# TODO
def p2(state: State) -> str:
    moves = listMoves(state)
    return moves[0]


# Debug
def listMoves(state: State) -> list[str]:
    turn: int = state.turn
    ret: list[str] = []
    fullList: list[str] = ['O','o','1','X','x','2']
    subList: list[str] = fullList[(turn-1)*3: ((turn-1)*3) + 3]
    x: int = 0
    y: int = 0
    
    while y < 5:
        while x < 5:
            if state.board[index(x,y)] == "":
                # Placing normal piece/Wall
                if state.pieces[(turn-1)*2] > 0: 
                    ret.append("n" + subList[0] + chr(x+97) + str(y))
                    ret.append("n" + subList[1] + chr(x+97) + str(y))
                # Placing Capstone
                if state.pieces[((turn-1)*2)+1] > 0:
                    ret.append("n" + subList[2] + chr(x+97) + str(y))
            elif state.board[index(x,y)][:1] in subList:
                # Move pieces
                if len(state.board[index(x,y)]) < 6:
                    carry: int = len(state.board[index(x,y)]) - 1
                else:
                    carry: int = 4
                ret = ret + moveTree(state , x, y, carry, subList,False,"", [carry])
            x = x+1
        x = 0
        y = y+1
    return ret
# To Fix
def moveTree(state: State, x: int, y: int, carry: int, pieces: list[str], additional: bool, current: str, previous) -> list[str]:
    if carry < 0:
        return [current]
    board = state.board
    toMove = board[index(x,y)]
    hasCapstone = (toMove[:1] == pieces[2])
    retList: list[str] = []
    c: int = carry
    oldCurrent = current
    while c >= 0:
    # move up
        if (y > 0) and not (board[index(x,y-1)][:1] in ['o','x','1','2']):
            move = 'm' + str(c) + chr(x+97) + str(y) + 'u'
            state.move = move
            if additional:
                current =  current + str(c) + 'u'
            else:
                current = move
            state2 = movePiece(state)
            retList = retList + moveTree(state2, x,y-1, c-1,pieces,True,current, previous + [carry])
        current = oldCurrent
        # move down
        if (y < 4) and not (board[index(x,y+1)][:1] in ['o','x','1','2']):
            
            move = 'm' + str(c) + chr(x+97) + str(y) + 'd'
            state.move = move
            if additional:
                current = current + str(c) + 'd'
            else:
                current = move
            state2 = movePiece(state)
            retList = retList + moveTree(state2, x,y+1, c-1,pieces,True,current, previous + [carry])
        current = oldCurrent
        # move left
        if (x > 0) and not (board[index(x-1,y)][:1] in ['o','x','1','2']):
            move = 'm' + str(carry) + chr(x+97) + str(y) + 'l'
            state.move = move
            if additional:
                current = current + str(c) + 'l'
            else:
                current = move
            state2 = movePiece(state)
            retList = retList + moveTree(state2, x-1,y, c-1,pieces,True,current, previous + [carry])
        current = oldCurrent
        # move right
        if (x < 4) and not (board[index(x+1,y)][:1] in ['o','x','1','2']):
            move =  'm' + str(c) + chr(x+97) + str(y) + 'r'
            state.move = move
            if additional:
                current = current + str(c) + 'r'
            else:
                current = move
            state2= movePiece(state)
            retList = retList + moveTree(state2, x+1,y, c-1,pieces,True,current, previous + [carry])
        c = c-1
    return retList

