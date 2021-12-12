from AI import *
from Board import *
from debug import *
def main() -> None:
    state: State = State(1)
    # gameloop(state)
    debug2()

    # gameloop(state, init(1000,700))
# def init(width: int, height: int) -> pygame.Surface:
    # pygame.display.set_caption("Takquito")
    # win: pyGame.Surface  = 0 #pygame.display.set_mode((width,height))
    # return win

def gameloop(state: State) -> None:
    while state.turn > 0:
        nextState: State = assignMoves(state)
        state = incTurn(nextState)
        printState(state)
        
    printWinner(state)
         
    
if __name__ == "__main__":
    main()
