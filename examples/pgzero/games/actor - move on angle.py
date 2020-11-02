#-----------------------------------------------------------------------------
# Name:        actors with images example
# Purpose:     And Example file demoing actors
#
# Author:      Mr. Brooks
# Created:     02-Nov-2020
# Updated:     02-Nov-2020
#-----------------------------------------------------------------------------
import math
WIDTH = 200
HEIGHT = 200

gameState = ''

#Create the actor object
knight = Actor('knight_m_run_anim_f0')
#Give the actor a place on the screen to be
knight.pos = (100, 100)
#Make a move variable in the knight actor for our use
knight.move = False #These are all custom attributes https://www.pygame.org/docs/ref/rect.html
knight.speed = 0.5  #Speed for the knight to move at
knight.xDirection = 1 #Amount to move in x Direction
knight.yDirection = 1 #Amount to move in y Direction



def on_mouse_up(pos):
    knight.angle = knight.angle_to(pos)
    print(f'angle: {knight.angle}')
    knight.xDirection = math.cos(math.radians(knight.angle))
    knight.yDirection = -math.sin(math.radians(knight.angle))
    print(f'direction change:({knight.xDirection},{knight.yDirection}')


def on_key_down(key):
    '''Check to see if a key has been released'''
    global knight
    
    if key == keys.A:
        knight.move = not knight.move
         
    
def on_key_up(key):
    pass

def update():
    global knight
    
    if knight.move:
        knight.x += knight.speed*knight.xDirection #Change the x position by a small amount to move it.
        knight.y += knight.speed*knight.yDirection


def draw():
    '''Draw loop for all the graphical elements to display'''
    #Empty the screen for each animation frame
    screen.fill((255, 255, 255))
    #Draw the knight
    knight.draw()