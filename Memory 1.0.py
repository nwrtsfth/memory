import pygame
from random import randint
pygame.init()

CWH = 150 #Card width and height
CARDS_X = 6 #Amount of cards on x-as
CARDS_Y = 6 #Amount of cards on y-as
X_AS_LEN = CARDS_X*(CWH+10) #Total lenght in pixels of x-as
Y_AS_LEN = CARDS_Y*(CWH+10) #Total lenght in pixels of y-as
DISPLAY_WIDTH  = X_AS_LEN+140
DISPLAY_HEIGHT = Y_AS_LEN+100
print (DISPLAY_WIDTH)
print (DISPLAY_HEIGHT)
#Display and cards settings

TICK    = 60
DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
CLOCK   = pygame.time.Clock()
#Program settings

BLACK =     (0,0,0)
WHITE =     (255,255,255)
GREY =      (70,70,70)
RED =       (255,0,0)       #1
GREEN =     (0,255,0)       #2
BLUE =      (0,0,255)       #3
YELLOW =    (255,255,0)     #4
MAGENTA =   (255,0,255)     #5
CYAN =      (0,255,255)     #6
ORANGE =    (255,100,0)     #7
PURPLE =    (100,0,150)     #8
SEAGREEN =  (140,190,140)   #9
GOLD =      (220,165,30)    #10
PINK =      (255,100,180)   #11
DARKGREEN = (0,130,0)       #12
BEIGE =     (230,200,150)   #13
DARKRED =   (130,0,0)       #14
DARKBLUE =  (30,30,110)     #15
BROWN =     (120,50,10)     #16
LIGHTBLUE = (170,210,230)   #17
TEAL =      (0,130,130)     #18
RGB = [RED, GREEN, BLUE, YELLOW, MAGENTA, CYAN, ORANGE, PURPLE, SEAGREEN, GOLD, PINK, DARKGREEN, BEIGE, DARKRED, DARKBLUE, BROWN, LIGHTBLUE, TEAL]

def random_order(n):
    list_1 = 2*list(range(0,int(n)))
    list_2 = []
    while len(list_1) > 0:
        NUMBER = list_1[randint(0,len(list_1)-1)]
        list_1.remove(NUMBER)
        list_2.append(NUMBER)
    return list_2
#Generates a list with specific range in random order

def generate_cards(dict_1, dict_2):
    NUMBER = 0
    list_1 = random_order((CARDS_X*CARDS_Y)/2)
    for x in range(0, X_AS_LEN, CWH+10):
        for y in range(0, Y_AS_LEN, CWH+10):
            dict_1["card_{0}".format(NUMBER)] = (x, y)
            dict_2["card_{0}".format(NUMBER)] = RGB[list_1[NUMBER]]
            NUMBER += 1
    return dict_1, dict_2
#Assigns all colors and coordinates to cards

def draw_cards(dict_1, dict_2, set_1, mouse, click, TIMER, CLICKS):
    for card in dict_1:
        CARD = dict_1[card]
        if CARD[0]+CWH > mouse[0] > CARD[0] and CARD[1]+CWH > mouse[1] > CARD[1] and card not in set_1:
            pygame.draw.rect(DISPLAY, GREY, (CARD[0], CARD[1], CWH, CWH))
            if click[0] == 1 and TIMER == 0:
                set_1.add(card)
                CLICKS += 1
        elif card in set_1:
            pygame.draw.rect(DISPLAY, dict_2[card], (CARD[0], CARD[1], CWH, CWH))
        else:
            pygame.draw.rect(DISPLAY, BLACK, (CARD[0], CARD[1], CWH, CWH))
    return CLICKS
#Draws all cards on screen and if mouse hovers over card and card not opened, card becomes grey

def startgame(dict_1, dict_2, SCORE, CLICKS):
    generate_cards(dict_1, dict_2)
    SCORE = 0
    CLICKS = 0
    return SCORE, CLICKS


def stopgame():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

def draw_text(font, size, text, color, coords):
    DISPLAY.blit(pygame.font.SysFont(font, size).render(text, True, color), coords)
#Draws text on screen with given information

def size(text, size):
    text_width = (pygame.font.SysFont("Arial", size).render(text, True, (0, 0, 0)).get_width())/2
    return text_width
#Gives value of lenght of textsize
#Textheight by size 30 is 36
#Textheight by size 50 is 58

def game():
    PLAY    = False
    OPTIONS = False
    SCORE   = 0
    CLICKS  = 0
    TIMER   = 0
    CARDS   = {}
    CARDS_COLORS    = {}
    CARDS_OPENED    = set()
    SAME_CARDS      = set()
    MENUBUTTONS = {"Play":      [(80, 200, 180), DISPLAY_WIDTH/2-190, DISPLAY_HEIGHT/2-25 ,120, 50, "Play",    DISPLAY_WIDTH/2-size("Play", 30)-130, DISPLAY_HEIGHT/2-18],
                   "Options":   [(80, 200, 180), DISPLAY_WIDTH/2-60,  DISPLAY_HEIGHT/2-25 ,120, 50, "Options", DISPLAY_WIDTH/2-size("Options", 30),  DISPLAY_HEIGHT/2-18],
                   "Quit":      [(80, 200, 180), DISPLAY_WIDTH/2+70,  DISPLAY_HEIGHT/2-25, 120, 50, "Quit",    DISPLAY_WIDTH/2-size("Quit", 30)+130, DISPLAY_HEIGHT/2-18]}
    ENDBUTTONS = {"Restart":    [(80, 200, 180), DISPLAY_WIDTH/2-60,  DISPLAY_HEIGHT/2-50, 120, 50, "Restart", DISPLAY_WIDTH/2-size("Restart", 30),  DISPLAY_HEIGHT/2-44],
                  "Menu":       [(80, 200, 180), DISPLAY_WIDTH/2-60,  DISPLAY_HEIGHT/2+10, 120, 50, "Menu",    DISPLAY_WIDTH/2-size("Menu", 30),     DISPLAY_HEIGHT/2+16],
                  "Quit":       [(80, 200, 180), DISPLAY_WIDTH/2-60,  DISPLAY_HEIGHT/2+70, 120, 50, "Quit",    DISPLAY_WIDTH/2-size("Quit", 30),     DISPLAY_HEIGHT/2+76]}
                                # Key: [color, first x, first y, second x, second y, Text, text_x, text_y ]
    #Creates all variables, dictionaries and sets needed

    while True:
        stopgame()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #Key and mouse logs

        DISPLAY.fill(WHITE)
        for button in MENUBUTTONS:
            button = MENUBUTTONS[button]
            pygame.draw.rect(DISPLAY, button[0],(button[1], button[2], button[3], button[4]))
            if button[1] + button[3] > mouse[0] > button[1] and button[2] + button[4] > mouse[1] > button[2]:
                pygame.draw.rect(DISPLAY, (120, 220, 240), (button[1], button[2], button[3], button[4]))
                if click[0] == 1 and button[5] == "Play" and TIMER == 0:
                    SCORE, CLICKS = startgame(CARDS, CARDS_COLORS, SCORE, CLICKS)
                    PLAY = True
                    TIMER = 30
                if click[0] == 1 and button[5] == "Options" and TIMER == 0:
                    OPTIONS = True
                    TIMER = 30
                if click[0] == 1 and button[5] == "Quit" and TIMER == 0:
                    pygame.quit()
                    quit()
            draw_text("Arial", 30, button[5], BLACK, (button[6], button[7]))

        if TIMER > 0:
            TIMER -= 1

        while OPTIONS == True:
            stopgame()
            DISPLAY.fill(WHITE)
            pygame.display.update()

        while PLAY == True:
            stopgame()
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            #Key and mouse logs

            DISPLAY.fill(WHITE)
            CLICKS = draw_cards(CARDS, CARDS_COLORS, CARDS_OPENED, mouse, click, TIMER, CLICKS)     #Displays cards with color according to if opened, mouse over or nothing
            draw_text("Arial", 30, "Score: {0}".format(SCORE), BLACK, (DISPLAY_WIDTH-115,0))        #Displays the players score
            draw_text("Arial", 30, "Clicks: {0}".format(CLICKS), BLACK, (DISPLAY_WIDTH-115,40))     #Displays the amount of cards the players has clicked on
            #Draws cards and text on screen

            if sum(1 for card in CARDS_OPENED) == 2 and TIMER == 0:
                TIMER = 91
                for card in CARDS_OPENED:
                    SAME_CARDS.add(CARDS_COLORS[card])
                if len(SAME_CARDS) == 1:
                    SCORE += 1
            #If there are two cards opened, and timer = 0, then keep the cards opened for 1.5 seconds, and if two cards are the same, add 1 to total score
            if TIMER == 1:
                if len(SAME_CARDS) == 1:
                    for card in CARDS_OPENED:
                        CARDS.pop(card)
                CARDS_OPENED = set()
                SAME_CARDS = set()
            #After 1.5 seconds, close the cards and if two cards are the same, remove them from screen completely

            if SCORE == int(CARDS_X * CARDS_Y / 2) and TIMER == 0:
                for button in ENDBUTTONS:
                    button = ENDBUTTONS[button]
                    pygame.draw.rect(DISPLAY, button[0], (button[1], button[2], button[3], button[4]))
                    if button[1] + button[3] > mouse[0] > button[1] and button[2] + button[4] > mouse[1] > button[2]:
                        pygame.draw.rect(DISPLAY, (120, 240, 220), (button[1], button[2], button[3], button[4]))
                        #Draws all buttons on endscreen
                        if click[0] == 1 and button[5] == "Restart":
                            SCORE, CLICKS = startgame(CARDS, CARDS_COLORS, SCORE, CLICKS)
                            TIMER = 30
                        #If restartbutton is clicked, a new deck will be generated and all the scores are set to 0
                        if click[0] == 1 and button[5] == "Menu":
                            PLAY = False
                            TIMER = 30
                        #If menubutton is clicked, the program returns to its first loop; the menu
                        if click[0] == 1 and button[5] == "Quit":
                            pygame.quit()
                            quit()
                        #If quitbutton is clicked, programm will be closed
                    draw_text("Arial", 30, button[5], BLACK, (button[6], button[7]))
                draw_text("Arial", 50, "You won!", BLACK, (DISPLAY_WIDTH / 2 - 84, DISPLAY_HEIGHT / 2 - 110))
            #Checks if game has ended and displays 3 options: restart, menu or quit

            if TIMER > 0:
                TIMER -= 1
            #If time left, retracts 1 from time

            pygame.display.update()
            CLOCK.tick(TICK)
            #Update

        pygame.display.update()
        CLOCK.tick(TICK)
        #Update


game()
pygame.quit()
quit()
#End of programm, pygame and python quit.