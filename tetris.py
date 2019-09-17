import pygame
from pygame.locals import *
import random
from settings import *

class Tetris(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[Shapes.index(shape)] #{shape} = error, find out how to fix it 
        self.rotation = 0
        
def create_grid(locked_pos={}):
    #create one list for every row in grid
    #since we have 20 rows we want to create 20 sub lists
    #each sub list is going to have 10 colors 
    grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]
    
    #drawing static blocks
    #columns (y) = j, rows (x) = i
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                key = locked_pos[(j, i)]
                grid[i][j] = key
    return grid
        
                   
def convert_shape_format(self):
    pass

def valid_space():
    pass
    
def check_lost():
    pass

#picks one random shape falling down the screen 
def get_shape():
    return Tetris(5, 0, random.choice(Shapes))

def draw_text():
    pass

def draw_grid(Surface, grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(Surface, grid[i][j], (X + j*block_size, Y + i*block_size, block_size, block_size), 0)
            
            #looping through every color the grid
            #Surface = what I'm drawing on to 
            #grid[i][j] = color
            #X + j*30, Y + i+30 = the position in which it's being drawn on to
    
    
    pygame.draw.rect(Surface, (red), (X, Y, board_width, board_height), 4)
    #draws the actual grid
    #4 = border size
    
    
def draw_window(Surface, grid):
    Surface.fill((black))
    
    #Tetris title
    pygame.font.init()
    
    T = font.render("T", 1, (blue)) 
    E = font.render("E", 1, (yellow)) 
    T2 = font.render("T", 1, (red)) 
    R = font.render("R", 1, (green)) 
    I = font.render("I", 1, (light_blue))
    S = font.render("S", 1, (orange))
    
    Surface.blit(T, (X - board_width / 15, 30))
    
    Surface.blit(E, ((X + board_width / 2) - (E.get_width() / 2) - 95, 30))
    
    Surface.blit(T2, ((X + board_width / 2) - (T2.get_width() / 2) - 35, 30))
    
    Surface.blit(R, ((X + board_width / 2) - (R.get_width() / 2) + 15, 30))
    
    Surface.blit(I, ((X + board_width / 2) - (T2.get_width() / 2) + 85, 30))
    
    Surface.blit(S, ((X + board_width / 2) - (T2.get_width() / 2) + 135, 30))

    #Surface.blit(I, (X - board_width / 14, 30))
    #Surface.blit(S, (X - board_width / 14, 30))
    #Surface.blit(T, (X - board_width / 2 - T.get_width() / 2, 30))
    
    draw_grid(Surface, grid)        
    pygame.display.update()        

def main(win):
    global grid
    
    locked_pos = {}
    grid = create_grid(locked_pos)
    
    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0 
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    
                    current_piece.x -= 1
                    if not(valid_space(current_piece, grid)):
                        current_piece += 1
                    
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece -= 1
                
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece -= 1
                    
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece -= 1

#the if not condition returns and checks if the current position of the piece is in a valid space
                        
        draw_window(win, grid)      
        
    
def main_menu(win):
    main(win)

#creating a pygame surface
win = pygame.display.set_mode((s_width, s_height))
main_menu(win)



 