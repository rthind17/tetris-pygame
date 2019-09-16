fps = 25
s_width = 800
s_height = 700
block_size = 30
board_width = 300 
board_height = 600

X = (s_width - board_width) / 2
Y = s_height - board_height

#frequency
sideway_freq = 0.15
down_freq = 0.1

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

shape_colors = [(white), (black), (gray), (red), (yellow), (blue), (light_blue), (green), (purple), (orange), (pink)] 

shadow = gray

#font
FONT_PATH = './font/TETRIS.TTF'
font = pygame.font.Font(FONT_PATH, 60)

#tetris shapes
S_shape = [['.....', 
            '.....', 
            '..00.', 
            '.00..', 
            '.....'], 
           ['.....', 
            '..0..', 
            '..00.', 
            '...0.', 
            '.....']]

Z_shape = [['.....',
            '.....',
            '.00..',
            '..00.',
            '.....'],
           ['.....',
            '..0..',
            '.00..',
            '.0...',
            '.....']]

T_shape = [['.....',
            '..O..',
            '.OOO.',
            '.....',
            '.....'],
           ['.....',
            '..O..',
            '..OO.',
            '..O..',
            '.....'],
           ['.....',
            '.....',
            '.OOO.',
            '..O..',
            '.....'],
           ['.....',
            '..O..',
            '.OO..',
            '..O..',
            '.....']]

I_shape = [['..O..',
            '..O..',
            '..O..',
            '..O..',
            '.....'],
           ['.....',
            '.....',
            'OOOO.',
            '.....',
            '.....']]

O_shape = [['.....',
            '.....',
            '.OO..',
            '.OO..',
            '.....']]

J_shape = [['.....',
            '.O...',
            '.OOO.',
            '.....',
            '.....'],
           ['.....',
            '..OO.',
            '..O..',
            '..O..',
            '.....'],
           ['.....',
            '.....',
            '.OOO.',
            '...O.',
            '.....'],
           ['.....',
            '..O..',
            '..O..',
            '.OO..',
            '.....']]

L_shape = [['.....',
            '...O.',
            '.OOO.',
            '.....',
            '.....'],
           ['.....',
            '..O..',
            '..O..',
            '..OO.',
            '.....'],
           ['.....',
            '.....',
            '.OOO.',
            '.O...',
            '.....'],
           ['.....',
            '.OO..',
            '..O..',
            '..O..',
            '.....']]

Shapes = {'S': S_shape,
          'Z': Z_shape,
          'J': J_shape,
          'L': L_shape,
          'I': I_shape,
          'O': O_shape,
          'T': T_shape}


