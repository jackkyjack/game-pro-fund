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




class Game():
        def __init__(self):
            pg.init()
            pg.mouse.set_visible(False)
            self.screen = pg.display.set_mode(RES)
            self.clock = pg.time.Clock()
            self.delta_time = 1
            self.global_trigger = False
            self.global_event = pg.USEREVENT + 0
            pg.time.set_timer(self.global_event, 40)
            self.new_game()
            self.timer = pg.time
            
        def new_game(self):
            self.map = Map(self)
            self.player = Player(self)
            self.object_renderer = ObjectRenderer(self)
            self.raycasting = RayCasting(self)
            # self.static_sprite = SpriteObject(self)
            # self.animated_sprtie = AnimatedSprite(self)
            self.object_handler = ObjectHandler(self)
            self.weapon = Weapon(self)
            self.sound = Sound(self)
            self.pathfinding = PathFinding(self)
            
        def update(self):
            self.player.update()
            self.raycasting.update()
            # self.static_sprite.update()
            # self.animated_sprtie.update()
            self.object_handler.update()
            self.weapon.update()
            pg.display.flip()
            self.delta_time = self.clock.tick(FPS)
            pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

        def draw(self):
            # self.screen.fill('black')
            self.object_renderer.draw()
            self.weapon.draw()
            # self.map.draw()
            # self.player.draw()
            pg.draw.rect(game.screen, 'white', (639,355,2,10))
            pg.draw.rect(game.screen, 'white', (635,359,10,2))
            
        def check_events(self):
            self.global_trigger = False
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.mouse.set_visible(True)
                    
                elif event.type == self.global_event:
                    self.global_trigger = True
                self.player.single_fire_event(event)
        
        def run(self):
                self.check_events()
                self.update()
                self.draw()
                


game = Game()