from re import M
from click import pass_context
import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *

class Game:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_games()
        
    def new_games(self):
        self.map = Map(self)
        self.player = Player(self)
        self.raycasting = RayCasting(self)
        
    def update(self):
        pg.display.flip()
        self.player.update()
        self.raycasting.update()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
        
    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        self.player.draw()
        
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
    
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
    
if __name__ == '__main__':
    game = Game()
    game.run()