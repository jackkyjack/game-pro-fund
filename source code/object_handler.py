from sprite_object import *
from npc import *
from random import choices, randrange

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list =[]
        self.npc_sprite_path = 'sprites/npc/'
        self.static_sprtie_path = 'sprites/static_sprites/'
        self.anim_sprite_path = 'sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}
        self.gameplaylast = 1
        
        
        # spawn npc
        self.enemies = 20# npc count
        self.npc_types = [Duck, Amogus, Pepe, purple, Jettt]
        self.weights = [40, 20, 10, 10, 20]
        self.restricted_area = {(i, j) for i in range(10) for j in range(10)}
        self.spawn_npc()
        
        # sprite map
        # add_sprite(SpriteObject(game))
        # add_sprite(SpriteObject(game, pos=(1.5, 1.5)))
        # add_sprite(AnimatedSprite(game))
        
        
        #npc map
        # add_npc(NPC(game))
        # add_npc(NPC(game, path= 'sprites/npc/purple/0.png', pos=(11.5, 2.5), scale=1.5,shift = 0))
        # add_npc(NPC(game, path= 'sprites/npc/Pepe/0.png',pos=(13, 2)))
        # add_npc(NPC(game, path= 'sprites/npc/Jettt/0.png', pos=(14.5, 4.5)))
        # add_npc(NPC(game, pos=(13, 2)))
        
    def spawn_npc(self):
        for i in range(self.enemies):
                npc = choices(self.npc_types, self.weights)[0]
                pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
                while (pos in self.game.map.world_map) or (pos in self.restricted_area):
                    pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
                self.add_npc(npc(self.game, pos=(x + 0.5, y + 0.5)))
        
    def check_win(self):
        if not len(self.npc_positions):
            self.game.object_renderer.win()
            self.gameplaylast = 2
            
            
        
    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        self.check_win()
        
    def add_npc(self, npc):
        self.npc_list.append(npc)
    
    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)