import pygame as pg
from setting import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture('textures/sky1.png', (WIDTH, HALF_HEIGHT))
        self.sky_offset = 0
        self.blood_screen = self.get_texture('textures/take_damage.png', RES)
        self.game_over_image = self.get_texture('textures/game_over.png', RES)
        self.win_image = self.get_texture('textures/win.png', RES)
        
    def draw(self):
        self.draw_bg()
        self.render_game_objects()
        
    def win(self):
        self.screen.blit(self.win_image, (0, 0))    
    
    def game_over(self):
        self.screen.blit(self.game_over_image, (0, 0))
        pg.time.delay(3000)
        
    def player_damage(self):
        self.screen.blit(self.blood_screen, (0, 0))
    
    def draw_bg(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))
        #floor
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))
    
    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.object_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)
    
    @staticmethod
    def get_texture(path, res = (TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    def load_wall_textures(self):
        return {
            1: self.get_texture('textures/wall1.png'),
            2: self.get_texture('textures/wall2.png'),
        }