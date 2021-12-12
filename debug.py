from AI import *
from Board import *




def debug2() -> None:
    print(checkDone(states()))

def states() -> list[str]:
    b: State = State(1)
    b.board = [
                "","OX","O","O","",
                "","OX","","O","",
                "O","OX","X","O","O",
                "","","X","","",
                "","","X","","",
            ]
    return b

def validMove(state: State) -> bool:
    moveStr = state.move
    return True
    # Check if new on valid square
    # Check if new on blank square
    # Check if move over wall
    # Check carry
    # Check capstone

def debug1(state: State) -> None:
    state.move = "n0a0"
    state.turn = 2
    state = movePiece(state)
    printState(state)
    state.move = "nXb0"
    state.turn = 1
    state = movePiece(state)
    printState(state)
    state.move = "m0a0r"
    state.turn = 2
    state = movePiece(state)
    printState(state)
    state.move = "nxc3"
    state.turn = 1
    state = movePiece(state)
    printState(state)
    state.move = "m1b0u0r"
    state = movePiece(state)
    printState(state)
