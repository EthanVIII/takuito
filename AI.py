class State:
    # 1 - P1's turn, 2 - P2's turn, 0 - No longer playing.
    def __init__(self, turn: int) -> None:
        self.turn: int = turn
        self.round: int = 0
        self.board: list[str] = ["" for i in range(0,25)]
        self.move: str = ""
        self.P1pieces: int = 21
        self.P2pieces: int = 21
        self.P1capstone: int = 1
        self.P2capstone: int = 1

def index(x:int,y:int) -> int:
    return x + y * 5

def assignMoves(state: State) -> State:
    if state.turn == 1:
        state.move = p1(state)
    elif state.turn == 2:
        state.move = p2(state)
    else:
        raise Exception("Invalid Player - assignMoves()")
    if not validMove(state) :
        raise Exception("Invalid Move - assignMoves()")
    state = movePiece(state)
    return state

# Debug
def movePiece(state: State) -> State:
    moveStr = state.move
    # Movement Ruleset
    if moveStr[0] == 'm':
        carry = int(moveStr[1])
        x1, y1 = int(ord(moveStr[2])-97), int(moveStr[3])
        toMove = state.board[index(x1,y1)][:carry+1]
        state.board[index(x1,y1)] = state.board[index(x1,y1)][carry+1:]
        match moveStr[4]:
            case "u":
                x,y = x1, y1+1
            case "d":
                x,y = x1, y1-1
            case "l":
                x,y = x1-1, y1
            case "r":
                x,y = x1+1,y1
        if (toMove == '1' or toMove == '2') and (state.board[index(x,y)][:1] == 'o' or state.board[index(x,y)][:1] == 'x'):
            state.board[index(x,y)][0] = chr(ord(state.board[index(x,y)][0]) - 32)
        state.board[index(x,y)] = toMove + state.board[index(x,y)]
        if len(moveStr) > 4:
            moveStr = moveStr[5:]
            while len(moveStr) > 0:
                carry = int(moveStr[0])
                toMove = state.board[index(x,y)][:carry+1]
                state.board[index(x,y)] = state.board[index(x,y)][carry+1:]
                match moveStr[1]:
                    case "u":
                        x1,y1 = x, y+1
                    case "d":
                        x1,y1 = x, y-1
                    case "l":
                        x1,y1 = x-1, y
                    case "r":
                        x1,y1 = x+1, y
                if (toMove == '1' or toMove == '2') and (state.board[index(x1,y1)][:1] == 'o' or state.board[index(x1,y1)][:1] == 'x'):
                    state.board[index(x1,y1)][0] = chr(ord(state.board[index(x1,y1)][0]) - 32)
                state.board[index(x1,y1)] = toMove + state.board[index(x1,y1)]
                moveStr = moveStr[2:]
    # Placement Ruleset
    elif moveStr[0] == 'n':
        pieceType = moveStr[1]
        x,y = int(ord(moveStr[2])-97), int(moveStr[3])
        if state.board[index(x,y)] == '':
           state.board[index(x,y)] = str(pieceType) 
        else: 
            raise Exception("Invalid Move - movePiece()")
    state.move = ""
    return state

# TODO
def p1(state: State) -> str:
    pieces = ["O","o","1"]
    move = "n0a4"
    return move

# TODO
def p2(state: State) -> str:
    pieces = ["X","x","2"]
    move = "nXb2"
    return move

# TODO for AI
def listMoves(state: State) -> list[str]:
    return [""]

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
