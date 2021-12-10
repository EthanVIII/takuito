import pygame
import sys
sys.path.append(".")
from AI import *
from Board import *

def main() -> None:
    state: State = State(1, ["" for i in range(0,25)])
    pygame.display.set_caption("Takquito")
    gameloop(state, init(1000,700))

def init(width: int, height: int) -> pygame.Surface:
    win: pyGame.Surface  = 0 #pygame.display.set_mode((width,height))
    return win

def gameloop(state: State, win: pygame.Surface) -> None:
    while state.turn > 0:
        nextState: State = assignMoves(state)
        state = incTurn(nextState)
        printState(state)
        
    printWinner(state)
         
    
if __name__ == "__main__":
    main()
