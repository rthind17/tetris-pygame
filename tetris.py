import pygame
import random
from settings import *

pygame.init()

class Tetris(object):  # *
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

##################################################  

def create_grid(locked_pos={}): #create one list for every row in grid
    #since we have 20 rows we want to create 20 sub lists
    #each sub list is going to have 10 colors
    grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]
    
    #columns (y) = j, rows (x) = i
    for i in range(len(grid)): #drawing static blocks
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                c = locked_pos[(j,i)]
                grid[i][j] = c
    return grid
 
################################################    

def convert_shape_format(shape): #takes the format of the block shapes and converts it into a form python can read
    pos = []
    form = shape.shape[shape.rotation % len(shape.shape)]
#gives the sub list (the first list in the shape variables) needed
    #Ex. if shape.rotation = 0, then 0 % len(shape.shape) (len = 4) gives us the first list of the shape 
    #Ex. if shape.rotation = 1, then 1 % len(shape.shape) (len = 4) gives us the second list of the shape  

    for i, line in enumerate(form):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pos.append((shape.x + j, shape.y + i))
#shape.x = current value of the shape
#if the shape is moving down the screen, is moving left and right we need to add the j value 

    for i, p in enumerate(pos):
        pos[i] = (p[0] - 2, p[1] - 4)

    return pos

###################################################

def valid_space(shape, grid):
    accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
#getting every single possible position for a 10x20 grid and adding it in a tuple
#if grid[i][j] == black only adds the position of (j, i) if grid[i][j] == black is true

    accepted_pos = [j for sub in accepted_pos for j in sub]
#converting into a 1 dimensional list
#takes all positions in accepted_pos and adding it into a one dimensional list 

    formatted = convert_shape_format(shape)

    for pos in formatted: #checks if pos exists in accepted_pos
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True

####################################################
def check_lost(pos): #checks if any of the positions are above the screen
    for p in pos:
        x, y = p
        if y < 1:
            return True

    return False

####################################################

def get_shape(): #picks one random shape falling down the screen 
    return Tetris(5, 0, random.choice(shapes))

####################################################

def draw_text(surface, text, size, color):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (X + board_width /2 - (label.get_width()/2), Y + board_height/2 - label.get_height()/2))
 
####################################################

def draw_grid(surface, grid):
    for i in range(len(grid)): #drawing horizontal lines
        pygame.draw.line(surface, (gray), (X, Y + i*block_size), (X+board_width, Y+ i*block_size))
#draws 20 vertical lines   
#everytime the function loops through a new row, the value of Y changes at the line that is being drawn, and X value stays static at the left side and right side of the screen
        for j in range(len(grid[i])): #drawing vertical lines
            pygame.draw.line(surface, (gray), (X + j*block_size, Y),(X + j*block_size, Y + board_height))
#draws 10 horizontal lines
#everytime the function loops through a new column, the value of X changes at the line that is being drawn, and the value of Y stays static at the top and bottom of the screen
            
#################################################### 

def clear_row(grid, locked): #clears and shifts every row down when all positions are filled
    inc = 0
    for i in range(len(grid)-1, -1, -1): #loops through the grid backwards
        row = grid[i] #row = to every row in the grid
        if (black) not in row: #the way that we know that the row needs to be cleared is when the color black does not exist
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
                    
    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]: #for every key in the sorted list of  locked positions based on the y value
            x, y = key #getting the x and y position of each key in locked
        if y < ind: #if y value of the key is above the current index of the row removed.
#Ex. if row 17 is removed, then anything above row 17 is moved down. 
            new_key = (x, y + inc)
            locked[new_key] = locked.pop(key)
#shifts every single position in the grid, down 
    

####################################################
def draw_next_shape(shape, surface): #displays the next falling shape on the right side of the screen
    text = pygame.font.SysFont('comicsans', 30)
    label = text.render('Next Shape', 1, (white))

    sx = X + board_width + 50
    sy = Y + board_height/2 - 100
    form = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(form):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j*block_size, sy + i*block_size, block_size, block_size), 0)

    surface.blit(label, (sx + 10, sy - 30))
    
####################################################

def draw_window(surface, grid):
    surface.fill((black))

    pygame.font.init()
    T = font.render("T", 1, (blue)) 
    E = font.render("E", 1, (yellow)) 
    T2 = font.render("T", 1, (red)) 
    R = font.render("R", 1, (green)) 
    I = font.render("I", 1, (light_blue))
    S = font.render("S", 1, (orange))
    
    surface.blit(T, (X - board_width / 15, 30))
    
    surface.blit(E, ((X + board_width / 2) - (E.get_width() / 2) - 95, 30))
    
    surface.blit(T2, ((X + board_width / 2) - (T2.get_width() / 2) - 35, 30))
    
    surface.blit(R, ((X + board_width / 2) - (R.get_width() / 2) + 15, 30))
    
    surface.blit(I, ((X + board_width / 2) - (T2.get_width() / 2) + 85, 30))
    
    surface.blit(S, ((X + board_width / 2) - (T2.get_width() / 2) + 135, 30))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (X + j*block_size, Y + i*block_size, block_size, block_size), 0)
#looping through every color the grid
#Surface = what I'm drawing on to 
#grid[i][j] = color
#X + j*30, Y + i+30 = the position in which it's being drawn on to

    pygame.draw.rect(surface, (red), (X, Y, board_width, board_height), 5) #draws the actual grid
#5 = border size

    draw_grid(surface, grid)
    #pygame.display.update()

###################################################

def main(win):  # *
    locked_pos = {}
    grid = create_grid(locked_pos)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27

    while run:
        grid = create_grid(locked_pos)
        fall_time += clock.get_rawtime()
        clock.tick()
#rawtime gets the amount of time since the last clock.tick()
#when first adding fall time and clock, equals 0
#next iteration its going to see how long it takes the while loop to run and then it's going to add that amount

        if fall_time/1000 > fall_speed: #moves the block piece automatically down by 1
            fall_time = 0
            current_piece.y += 1
            if not(valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.x -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.y -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.rotation -= 1

#the if not condition returns and checks if the current position of the piece is in a valid space
                      
        shape_pos = convert_shape_format(current_piece)

        for i in range(len(shape_pos)): #add color of piece to the grid for drawing
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
            clear_row(grid, locked_pos)

        draw_window(win, grid)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        if check_lost(locked_pos):
            draw_text_middle(win, "YOU LOST!", 80, (white))
            pygame.display.update()
            pygame.time.delay(1500)
            run = False

def main_menu(win): 
    run = True
    while run:
        win.blit(img, (s_width/4, s_height/6))
        draw_text(win, 'Press Any Key To Play', 60, (white))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main(win)

    pygame.display.quit()


win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')
main_menu(win)
    




 