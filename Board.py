from AI import *
    
def printWinner(state: State) -> None:
    match state.turn:
        case 0:
            print("Draw @ R: " + str(state.round))
        case -1:
            print("P1 Wins @ R: " + str(state.round))
        case -2:
            print("P2 Wins @ R: " + str(state.round))

def printState(state: State) -> None:
    print("Turn: " + str(state.turn))
    l: list[int] = [max(len(state.board[index(x,y)]) for y in range(0,5)) for x in range(0,5)]
    for y in range(0,5): 
        s: str = "|"
        for x in range(0,5):
            cell: str = state.board[index(x,y)]
            s = s + cell + (" " * (l[x] - len(cell))) + "|"
        print("-"*len(s))
        print(s)
    print("-"*len(s))


