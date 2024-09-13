import pygame as pg
import sys
from setting import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *
from button import *
from main import *

pg.init()

SCREEN = pg.display.set_mode(RES)
pg.display.set_caption("VALODANT")

game = Game()
gameplay = 0

BG = pg.image.load("assets/bgbgbg.png")

rank =[]


def get_font(size): # Returns Press-Start-2P in the desired size
    return pg.font.Font("assets/spaceranger.ttf", size)

def play():
    
    gameplay = 1
    rankbool=False
    game.player.health = 20
    game.player.gameplaylast = 1
    starttime = pg.time.get_ticks()
    while True:
        # events = pg.event.get()
        # for event in events:
        #     if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
        #         main_menu()
        #         gameplay = 2
        if gameplay == 1:
            game.run()
            pg.mouse.set_visible(False)
            gameplay = game.object_handler.gameplaylast
            # SCREEN.blit(add_rank(float((pg.time.get_ticks() - starttime)/ 1000.0)), (25, 25))
            if gameplay != 2:  
                gameplay = game.player.gameplaylast
                
            else:
                game.object_handler.__init__(game)
                game.player.__init__(game)
                rankbool = True
            
        elif gameplay == 0:
            game.object_renderer.game_over()
            main_menu()
        elif gameplay == 2:
            if rankbool :
                add_rank(float((pg.time.get_ticks() - starttime)/ 1000.0))
                save_rank()
                rankbool = False
            else:
                main_menu()
            
        
            
        
                   
def load_rank():
    f = open("rank.txt","r")
    rank.append(float(f.readline()))
    rank.append(float(f.readline()))
    rank.append(float(f.readline()))
    rank.append(float(f.readline()))
    rank.append(float(f.readline()))
    f.close()
    print(rank)
    
def add_rank(data):
    rank.append((data))
    rank.sort()
    rank.pop(-1)
    
    
def save_rank():
    f = open("rank.txt","w")
    for time in rank:
        f.write(str(time) + "\n")
    f.close()
    # print(rank)
    
def ranking():
    while True:
        RANKING_MOUSE_POS = pg.mouse.get_pos()

        SCREEN.fill("white")

        # OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        # OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        # SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        RANKING_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        RANKING_BACK.changeColor(RANKING_MOUSE_POS)
        RANKING_BACK.update(SCREEN)

        
        
        
        test1 = get_font(20).render("No 1 :  " + str(rank[0]), True, "black")
        test2 = get_font(20).render("No 2 :  " + str(rank[1]), True, "black")
        test3 = get_font(20).render("No 3 :  " + str(rank[2]), True, "black")
        test4 = get_font(20).render("No 4 :  " + str(rank[3]), True, "black")
        test5 = get_font(20).render("No 5 :  " + str(rank[4]), True, "black")
        
        SCREEN.blit(test1, (100, 50))
        SCREEN.blit(test2, (100, 100))
        SCREEN.blit(test3, (100, 150))
        SCREEN.blit(test4, (100, 200))
        SCREEN.blit(test5, (100, 250))
        
        
        
        
        
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.mouse.set_visible(True)
                    main_menu()
            if event.type == pg.MOUSEBUTTONDOWN :
                if RANKING_BACK.checkForInput(RANKING_MOUSE_POS):
                    main_menu()
                    
        pg.display.update()
        



def main_menu():
    while True:
        pg.mouse.set_visible(True)
        SCREEN.blit(BG, (0, 0))
        pg.display.set_caption("VALODANT")

        NAME_TEXT = get_font(20).render("65011174 ANUCHA KAEOMAMUEANG", True, "white")
        SCREEN.blit(NAME_TEXT, (0, 0))
        
        MENU_MOUSE_POS = pg.mouse.get_pos()

        NAME_GAME = get_font(100).render("VALODANT", True, "#b68f40")
        MENU_RECT = NAME_GAME.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pg.image.load("assets/Play_Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        RANKING_BUTTON = Button(image=pg.image.load("assets/Ranking_Rect.png"), pos=(640, 400), 
                            text_input="RANKING", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pg.image.load("assets/Quit_Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(NAME_GAME, MENU_RECT)

        for button in [PLAY_BUTTON, RANKING_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                    gameplay = 1
                if RANKING_BUTTON.checkForInput(MENU_MOUSE_POS):
                    ranking()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pg.quit()
                    sys.exit()

        pg.display.update()
load_rank()
main_menu()