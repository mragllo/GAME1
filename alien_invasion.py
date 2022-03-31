import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard



def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("alien_invasion")
    # Создание кнопки Play.
    play_button = Button(ai_settings, screen, "Play")
    # Создание экземпляров GameStats и Scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Создание корабля # Создание группы для хранения пуль. # создание группы тарелок
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # Создание пришельца.
    alien = Alien(ai_settings, screen)
    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Запуск основного цикла игры.
    while True:

        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


        # Удаление пуль, вышедших за край экрана.
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        # print(len(bullets))
run_game()
