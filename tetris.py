import pygame
from pygame.locals import *
import time
import random
import sys
from settings import *





class Tetris:
    def main():
        pygame.init()
        fps_clock = pygame.time.Clock()
        screen = pygame.display.set_mode((width, height))
        font = pygame.font.Font(FONT, 24)
        title_font = pygame.font.Font(FONT, 110)
        pygame.display.set_caption('TETRIS')
        
        show_text_screen('TETRIS')
        
        #game loop
        while True:
            if random.randint(0, 1) == 0:
                pass
            else:
                pass 
            run_game()
            show_text_screen('GAME OVER')
    
    #setting up game variables            
    def run_game():
        board = get_blank_board()
        down_time = pygame.time.time()
        sideways_time = pygame.time.time()
        fall_time = pygame.time.time()
        move_down = False
        move_left = False
        move_right = False
        score = 0
        level, fall_freq = calculate_freq(score)
        
        falling_piece = get_new_piece()
        next_piece = get_new_piece()
        
        #game loop
        while True:
            if falling_piece == None:
                
                falling_piece == next_piece
                next_piece = get_new_piece()
                
                #resetting fall_time
                fall_time = pygame.time.time()
                
                if not valid_pos(board, falling_piece):
                    return
            
            Check_Quit()
            #handling event
            for event in pygame.event.get():
                if event.type == KEYUP:
                    #pause game
                    if (pygame.event.key == K_p):
                        screen.fill(black)
                        show_text_screen('PAUSED')
                        fall_time = pygame.time.time()
                        down_time = pygame.time.time()
                        sideways_time = pygame.time.time()
                        
                    elif (pygame.event.key == K_LEFT):
                        move_left = False
                        
                    elif (pygame.event.key == K_RIGHT):
                        move_right = False
                        
                    elif (pygame.event.key == K_DOWN):
                        move_down == False
                        
                elif pygame.event.type == KEYDOWN:
                    
                    #moving sideways
                    if (pygame.event.key == K_LEFT) and valid_pos(board, falling_piece, adjX=-1):
                        
                        falling_piece['x'] -= 1
                        move_left = True
                        move_right = False
                        sideways_time = pygame.time.time()
                        
                    elif (pygame.event.key == K_RIGHT) and valid_pos(board, falling_piece, adjX=1):
                        falling_piece['x'] += 1
                        move_right = True
                        move_left = False
                        sideways_time = pygame.time.time()

                        
                        
                        
                        
                        
          
                #drawing to screen
            screen.fill(black)
            draw_board(board)
            draw_status(score, level)
            if falling_piece != None:          
                draw_piece(falling_piece)
                    
            pygame.display.update()
            fps_clock(fps)
                        
                
   
                    
                    
                    
                    
    def make_text(text, Font, color):
        surf = Font.render(text, True, color)
        return surf, surf.get_rect()
    
    #displaying large text in the 
    def display_screen(text):
        pass
    
    
    
if __name__ == '__main__':
    main()
        