import pygame

pygame.font.init()

s_width = 800
s_height = 700
block_size = 30
board_width = 300 
board_height = 600

X = (s_width - board_width) // 2
Y = s_height - board_height

#colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (185, 185, 185)
red = (255, 17, 0)
yellow = (255, 213, 0)
blue = (0, 47, 255)
light_blue = (0, 255, 234)
green = (2, 212, 23)
purple = (64, 0, 110)
orange = (255, 149, 28)
pink = (255, 82, 157)

shape_colors = [red, yellow, blue, light_blue, green, purple, orange] 

#font
FONT_PATH = './font/Tetris.ttf'
font = pygame.font.Font(FONT_PATH, 60)

#image
img_path = pygame.image.load('tetris.jpg')
img = pygame.transform.scale(img_path, (s_width//2, s_height//2))

img1_path = pygame.image.load('black.jpg')
img1 = pygame.transform.scale(img1_path, (s_width, s_height))

#tetris shapes
S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]