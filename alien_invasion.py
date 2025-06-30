import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button

def run_game():
    # initialize game and create a screen object.
    # initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
         (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # make the play button
    play_button = Button(ai_settings, screen, "Play")
    # create an instance to store game statistics.
    stats = GameStats(ai_settings)
    # set background color.
    bg_color = (200, 230, 230)
    # make a ship, a group of bullets, and a group of aliens
    ship = Ship(ai_settings, screen)
    # make a group to store bullets in.
    bullets = Group()
    aliens = Group()
    # make an alien
    # alien = Alien(ai_settings, screen)
    # create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start the main loop for the game.
    while True:
        # watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, ship, bullets, play_button,aliens  )
        if stats.game_active:
            ship.update() 
            bullets.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, ship, aliens, bullets)
        # redraw the screen during pass through the loop.
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)
        # draw the play button if the game is inactive.
        # if not stats.game_active:
        #     play_button.draw_button()
        # making the most recently drawn screen visible.
        pygame.display.flip()
        pygame.font.init()

run_game()

