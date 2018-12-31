import pygame, time
from random import randint
pygame.init()

DISPLAYWIDTH =  600
DISPLAYHEIGHT = 600
FPS =           60
CWH = 100 #Card_Width_Height_
C_AM = 4 #Card_amount 1
CM = C_AM * (CWH+10) # Card amount 2

gameDisplay = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT))
pygame.display.set_caption('Memory Game')
CLOCK = pygame.time.Clock()
#Settings

BLACK =     (  0,  0,  0)
WHITE =     (255,255,255)
GREY =      ( 70, 70, 70)
RED =       (255,  0,  0)
GREEN =     (0,  255,  0)
BLUE =      (0,    0,255)
YELLOW =    (255,255,  0)
MAGENTA =   (255,  0,255)
CYAN =      (  0,255,255)
ORANGE =    (255,100,  0)
PURPLE =    (100,  0,150)
COLOR1 =    ()
COLOR2 =    ()
COLOR3 =    ()
COLOR4 =    ()
COLOR5 =    ()
COLOR6 =    ()
COLOR7 =    ()
COLOR8 =    ()
COLOR9 =    ()
COLOR10 =   ()

RGB = [RED, GREEN, BLUE, YELLOW, MAGENTA, CYAN, ORANGE, PURPLE]
#Colors

def random_order(n):
    list_1 = 2*list(range(0,n))
    list_2 = []
    while len(list_1) > 0:
        number = list_1[randint(0,len(list_1)-1)]
        list_1.remove(number)
        list_2.append(number)
    return list_2
    #Generates list of number in a random order

def draw_cards(dictionary_1, dictionary_2):
    NUMBER = 0
    NUMBERLIST = random_order(C_AM*2)
    for X in range(0,CM,CWH+10):
        for Y in range(0,CM,CWH+10):
            dictionary_1["card_{0}".format(NUMBER)] = (X, Y)
            dictionary_2["card_{0}".format(NUMBER)] = RGB[NUMBERLIST[NUMBER]]
            NUMBER += 1
    return dictionary_1, dictionary_2
    #Generates field of cards in dictionaries

def light_up(dictionary_1, set_1, mouse, click):
    for card in dictionary_1:
        CARD = dictionary_1[card]
        if CARD[0] + CWH > mouse[0] > CARD[0] and CARD[1] + CWH > mouse[1] > CARD[1]:
            pygame.draw.rect(gameDisplay, GREY, (CARD[0], CARD[1], CWH, CWH))
            if click[0] == 1:
                set_1.add(card)
        else:
            pygame.draw.rect(gameDisplay, BLACK, (CARD[0], CARD[1], CWH, CWH))
    #Checks if mouse is over a rectangle, if so, rectangle gets grey

def open_cards(dictionary_1, dictionary_2, set_1, mouse, click):
    for card in dictionary_1 and dictionary_2 and set_1:
        CARD1 = dictionary_1[card]
        pygame.draw.rect(gameDisplay, dictionary_2[card], (CARD1[0], CARD1[1], CWH, CWH))
    #Renders the cards that are in the set CARDS_OPENED

def print_text(font, text, color, coords):
    font = pygame.font.SysFont(font, 30)
    textsurface = font.render(text, True, color)
    gameDisplay.blit(textsurface, coords)
    #Defines print_text and lets you display text on your screen

def game_loop():
    EXIT = False
    CARDS = {}
    CARDS_COLORS = {}
    CARDS_OPENED = set()
    SAME_CARDS = set()
    SCORE = 0
    #Dictionarys and sets

    draw_cards(CARDS, CARDS_COLORS)

    while EXIT == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                EXIT = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    EXIT = True
        #Events

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #Mouse movement and mouse clicks

        gameDisplay.fill(WHITE)
        light_up(CARDS, CARDS_OPENED, mouse, click)
        open_cards(CARDS, CARDS_COLORS, CARDS_OPENED, mouse, click)
        print_text("Arial", "Score: {0}".format(SCORE), BLACK, (500,0))
        #Functions

        pygame.display.update()
        CLOCK.tick(FPS)
        #Update

        if sum(1 for card in CARDS_OPENED) == 2:
            for card in CARDS_OPENED:
                SAME_CARDS.add(CARDS_COLORS[card])
            if len(SAME_CARDS) == 1:
                SCORE += 1
                pygame.draw.rect(gameDisplay, WHITE, (500,0,100,50))
                print_text("Arial", "Score: {0}".format(SCORE), BLACK, (500, 0))
                pygame.display.update()
                for card in CARDS_OPENED:
                    CARDS.pop(card)
                    CARDS_COLORS.pop(card)
            time.sleep(1)
            SAME_CARDS = set()
            CARDS_OPENED = set()
        #Checks if two cards are opened, and if two opened cards have same color - if so, remove cards
        #End of definition


game_loop()
pygame.quit()
quit()
#Gameloop, end of game - quit
