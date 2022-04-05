'''See PyGame Events documentation for a list of the events built into pygame: https://www.pygame.org/docs/ref/event.html '''
import pygame

def main():
    #-----------------------------Setup------------------------------------------------------#
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))
    
    
    #-----------------------------Program Variable Initialization----------------------------#
    # Set up some data to describe a small circle and its color
    # Set up some data to describe a small circle and its color
    circlePos = [50,100]  #X and Y Positions
    circleSpeed = [0,0]  #X and Y Speeds
    circleSize = 30  
    circleColor = (255, 0, 0)        # A color is a mix of (Red, Green, Blue)

    #-----------------------------Main Program Loop---------------------------------------------#
    while True:
        #-----------------------------Event Handling-----------------------------------------#
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        elif ev.type == pygame.KEYDOWN:  #KEYDOWN has the attributes: key, mod, unicode, scancode
            print('A Key was pressed down.  ', end='')
            print(f'key: {ev.key}, mod: {ev.mod}, unicode: {ev.unicode}, scancode: {ev.scancode}')
            
            if ev.key == pygame.K_LEFT:
                print('Move Left')
                circleSpeed[0] -= 0.05
            elif ev.key == pygame.K_RIGHT:
                print('Move Right')
                circleSpeed[0] += 0.05
        
#         #Uncomment this section to change the movement type to stop when the key is let go
#         elif ev.type == pygame.KEYUP:
#             if ev.key == pygame.K_LEFT:
#                 circleSpeed[0] = 0
#             elif ev.key == pygame.K_RIGHT:
#                 circleSpeed[0] = 0                
            
            print("MOUSEBUTTONDOWN Event Ran")

        #-----------------------------Program Logic---------------------------------------------#
        # Update your game objects and data structures here...
        circlePos[0] += circleSpeed[0]
        circlePos[1] += circleSpeed[1]


        #-----------------------------Drawing Everything-------------------------------------#
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))

               
        # Draw a circle on the surface
        pygame.draw.circle(mainSurface, circleColor, circlePos, 20)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.

main()


