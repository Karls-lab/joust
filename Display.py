import pygame
import json 
import os

class Menu():
    def __init__(self, screen) -> None:
        self.screen = screen
        self.selection = None
        self.WHITE = (255, 255, 255)

    
    def draw_text_to_center(self, text, font, color):
        self.screen.fill((0, 0, 0))
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen.get_width()/2, self.screen.get_height()/2)
        self.screen.blit(text_surface, text_rect)


    def draw_menu(self):
        font = pygame.font.SysFont('arial', 40)
        self.draw_text_to_center("Press Enter to Start", font, self.WHITE)


    def draw_game_over(self):
        font = pygame.font.SysFont('arial', 40)
        self.draw_text_to_center("Game Over! :(", font, self.WHITE)


    def draw_next_level(self, level_no):
        next_level = level_no + 1
        font = pygame.font.SysFont('arial', 40)
        self.draw_text_to_center(f"Level {next_level}, Press Enter to Start", font, self.WHITE)


class HighScore():
    def __init__(self, screen) -> None:
        self.screen = screen
        self.WHITE = (255, 255, 255)


    def is_high_score(self, score):
        high_scores = self.read_high_scores()
        for high_score in high_scores:
            if score > high_score['score']:
                return True
        return False
    

    def add_high_score(self, name, score):
        high_scores = self.read_high_scores()
        high_scores.append({'name': name, 'score': score})
        if len(high_scores) > 10:
            sorted_scores = sorted(high_scores, key=lambda k: k['score'], reverse=True)
            sorted_scores.pop()
        self.write_high_scores(high_scores)


    def input_score(self, score):
        pass
        

    def read_high_scores(self):
        with open(os.path.join('data', 'highscores.json'), 'a+') as json_file:
            if json_file.read() == '':
                json_file.write('[]')
            #data = json.load(json_file)
            #return data


    def write_high_scores(self, data):
        with open(os.path.join('data', 'high_scores.json', 'w')) as outfile:
            json.dump(data, outfile)


    def draw_high_scores(self):
        high_scores = self.read_high_scores()
        font = pygame.font.SysFont('arial', 40)
        self.screen.fill((0, 0, 0))
        for i, high_score in enumerate(high_scores):
            text_surface = font.render(f"{high_score['name']} {high_score['score']}", True, self.WHITE)
            text_rect = text_surface.get_rect()
            text_rect.center = (self.screen.get_width()/2, self.screen.get_height()/2 + i * 50)
            self.screen.blit(text_surface, text_rect)
        pygame.display.flip()


    def draw_text_to_center(self, text, font, color):
        self.screen.fill((0, 0, 0))
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen.get_width()/2, self.screen.get_height()/2)
        self.screen.blit(text_surface, text_rect)

