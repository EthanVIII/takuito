class State:
    # 1 - P1's turn, 2 - P2's turn, 0 - No longer playing.
    def __init__(self, turn: int, board: list[str]) -> None:
        self.turn: int = turn
        self.round: int = 0
        self.board: list[str] = board
        self.move: str = ""

def index(x:int,y:int) -> int:
    return x + y * 5
    
def assignMoves(state: State) -> State:
    if state.turn == 1:
        state.move = p1(state)
    elif state.turn == 2:
        state.move = p2(state)
    else:
        raise Exception("Invalid Player - assignMoves()")
    if not validMove(state.move) :
        raise Exception("Invalid Move - assignMoves()")
    state = movePiece(state)
    return state

# TODO
def movePiece(state: State) -> State:
    moveStr = state.move
    if moveStr[0] == 'm':
        # movement ruleset
    elif moveStr[1] == 'n':
        # New piece ruleset
        
    return state

def validMove(state: State) -> bool:
    moveStr = state.move
    # Check if new on blank square
    # Check if move over wall
    # Check carry
    # Check capstone


# TODO
def p1(state: State) -> str:
    move = ""
    return move

# TODO
def p2(state: State) -> str:
    move = ""
    return move

# TODO for AI
def listMoves(state: State) -> list[str]:
    return [""]

# TODO
def checkDone(state: State) -> (bool, int):
    return (True, 0)

def incTurn(state: State) -> State:
    (isDone, winner) = checkDone(state)
    if not isDone:
        if state.turn == 1:
            state.turn = 2
        elif state.turn == 2:
            state.turn = 1
        state.round = state.round + 1
    else:
        state.turn = -1 * winner   
    return state

