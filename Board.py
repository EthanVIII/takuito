import pygame
from AI import *
    
def printWinner(state: State) -> None:
    if state.turn == 0:
        print("Draw @ R: " + str(state.round))
    elif state.turn == -1:
        print("P1 Wins @ R: " + str(state.round))
    elif state.turn == -2:
        print("P2 Wins @ R: " + str(state.round))

def printState(state: State) -> None:
    l: list[int] = [max(len(state.board[index(x,y)]) for y in range(0,5)) for x in range(0,5)]
    for y in range(0,5): 
        s: str = "|"
        for x in range(0,5):
            cell: str = state.board[index(x,y)]
            s = s + cell + (" " * (l[x] - len(cell))) + "|"
        print("-"*len(s))
        print(s)
    print("-"*len(s))

# TODO Fix Visual
class Rect:
    def __init__(self,win:pygame.Surface, color: pygame.Color, rect: pygame.Rect) -> None:
        self.color = color
        self.rect = rect
        self.win = win

    def draw(self) -> None:
        pygame.draw.rect(self.win,self.color,self.rect)

def genBoard(win: pygame.Surface) -> [Rect]:
    board = []
    board.append(Rect(win,(255,255,255),pygame.Rect(100,100,30,30)))
    return board

def visualHandler() -> None:
    # sprites = genBoard(win)
    pygame.time.delay(30)
    pos = pygame.mouse.get_pos()
    win.fill((0,0,0))
    # Exit Condition
    key = pygame.key.get_pressed()
    if key[pygame.K_q]:
        pass

    for event in pygame.event.get():
        # Exit Condition
        if event.type == pygame.QUIT:
            pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for sprite in sprites:
                    if sprite.rect.collidepoint(event.pos):
                        pass

    # TODO: Fix Click and Drag Functionality
    buttonDown = pygame.MOUSEBUTTONDOWN
    for sprite in sprites:
        if sprite.rect.collidepoint(pos) and buttonDown:
            (x,y) = sprite.rect.size
            (a,b) = pos
            sprite.rect = pygame.Rect((a+0.5*x,b+0.5*y),(x,y))
        sprite.draw()
    pygame.display.update()

    
