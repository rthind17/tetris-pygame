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
                           
def convert_shape_format(shape): #takes the format of the block shapes and converts it into a form python can read
    pos = []
    format = shape.shape[shape.rotation % len(shape.shape)]
    #gives the sub list (the first list in the shape variables) needed
    #Ex. if shape.rotation = 0, then 0 % len(shape.shape) (len = 4) gives us the first list of the shape 
    #Ex. if shape.rotation = 1, then 1 % len(shape.shape) (len = 4) gives us the second list of the shape  
    
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pos.append((shape.x + j, shape.y + i))
#shape.x = current value of the shape
#if the shape is moving down the screen, is moving left and right we need to add the j value is
        
    for i, place in enumerate(pos):
        pos[i] = (pos[0] - 2, pos[1] - 4)
    
    return pos

def valid_space(shape, grid):
    accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == (black)] for i in range(20)]
#getting every single possible position for a 10x20 grid and adding it in a tuple
#if grid[i][j] == black only adds the position of (j, i) if grid[i][j] == black is true

    accepted_pos = [j for sub in accepted_pos for j in sub]
#converting into a 1 dimensional list
#takes all positions in accepted_pos and adding it into a one dimensional list 

    formatted = convert_shape_format(shape)
    
    for pos in formatted:
#checks if pos exists in accepted_pos
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True
    
def check_lost(pos):
#checks if any of the positions are above the screen
    for i in pos:
        x, y = pos
        if y < 1:
            return True
    
    return False
        
#picks one random shape falling down the screen 
def get_shape():
    return Tetris(5, 0, random.choice(Shapes))

def draw_text():
    pass

def draw_grid(Surface, grid):
    for i in range(len(grid)):
        #drawing horizontal lines
        pygame.draw.line(Surface, (gray), (X, Y + i*block_size), (X + board_width, Y + i*block_size))
     #draws 20 vertical lines   
     #everytime the function loops through a new row, the value of Y changes at the line that is being drawn, and X value stays static at the left side and right side of the screen
    
        for j in range(len(grid[i])):
            #drawing vertical lines
            pygame.draw.line(Surface, (gray), (X + j*block_size, Y), (X + j*block_size, Y + board_height))
     #draws 10 horizontal lines
     #everytime the function loops through a new column, the value of X changes at the line that is being drawn, and the value of Y stays static at the top and bottom of the screen
            
                       
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

    draw_grid(Surface, grid)        
    pygame.display.update() 

##################################################   
    
def draw_next_shape(shape, Surface): #displays the next falling shape on the right side of the screen
    text = TEXT
    title = text.render('NEXT SHAPE', 1, (white))
    
    Sx = X + board_width + 50
    Sy = Y + board_height/2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]
    
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(Surface, shape.color, (Sx + j*block_size, Sy + i*block_size, 30, 30), 0)
    
    Surface.blit(title, (Sx + 10, Sy - 30))
    
###################################################


###################################################

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
        fall_speed = 0.27
        grid = create_grid(locked_pos)
        fall_time += clock.get_rawtime()
#rawtime gets the amount of time since the last clock.tick()
#when first adding fall time and clock, equals 0
#next iteration its going to see how long it takes the while loop to run and then it's going to add that amount
        clock.tick()
        
        if fall_time/1000 >= fall_speed:
            fall_time = 0 
            current_piece.y += 1
#moves the block piece automatically down by 1

            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1
                    
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                
                if event.key == pygame.K_UP:
                    #rotating shape
                    current_piece.rotation = current_piece.rotation + 1 % len(current.piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation =  current_piece.rotation - 1 % len(current_piece.shape)
                    
                if event.key == pygame.K_DOWN:
                    #moving shape down
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1

#the if not condition returns and checks if the current position of the piece is in a valid space
        
        shape_pos = convert_shape_format(current_piece)
        for i in range(len(shape_pos)):
        #add color of piece to the grid for drawing
            
            x, y = shape_pos[i]
            if y > -1: #if not above the screen
                grid[y][x] = current_piece.color
        
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_pos[p] = current_piece.color 
                #the reason we have locked_pos is because we can get the position and color
                #when we passed locked_pos in the grid function (main function) we can get each of those positions in the grid and update the color of piece
                #locked_pos is a dictionary with a key of position and a value of color {pos:color}
                
            current_piece = next_piece 
            next_piece = get_shape()
            change_piece = False
                        
        draw_window(win, grid)
        draw_next_shape(next_piece, win)
        pygame.display.update()
        
        #Check if player lost
        if check_lost(locked_pos):
            run = False
      
    pygame.display.quit()    

################################################    
    
def main_menu(win):
    main(win)

#creating a pygame surface
win = pygame.display.set_mode((s_width, s_height))
main_menu(win)



 