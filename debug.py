from AI import *
from Board import *

def debug5() -> None:
    state = State(1)
    state.board =  [
                "x","x","2","","X",
                "o","o","","1","",
                "","","oo","X","",
                "o","o","","O","X",
                "X","X","o","","oX",
                     ]

    m = "m0c1d"
    l = listMoves(state)
    if m in l:
        print("Yes")
    else:
        print("No")
    printState(state)

def debug4() -> None:
    state = State(1)
    state.move = "n0a0"
    state = movePiece(state)
    state = incTurn(state)
    printState(state)
    state.move = "m0a0d"
    state = movePiece(state)
    state = incTurn(state)
    printState(state)
    state.move = "n0a0"
    state = movePiece(state)
    state = incTurn(state)
    printState(state)


def debug3() -> None:
    state = State(1)
    state.board =  [
                "","","","","",
                "","","","","",
                "","","OO","","",
                "","","","","",
                "","","","","",
                     ]
    l = listMoves(state)
    print(l)
    print(len(l))




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
