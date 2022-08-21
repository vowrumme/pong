import pygame,sys,random
from pygame.locals import *

court = { 'width':700, 'height':500 }
color = { 'white':(255,255,255), 'black':(0,0,0), 'red':(255,0,0) }
score = [0,0]
ball  = { 'x': 350, 'y': 100, 'vx': 8, 'vy': 5}
play1 = { 'x':30, 'y': 250, 'height': 100, 'width' : 20}
play2 = { 'x':court['width'] - 50, 'y': 250, 'height': 100, 'width' : 20}
pygame.init()
screen=pygame.display.set_mode((court['width'],court['height']))
while True:
    screen.fill(color['white'])
    # Show Score
    font=pygame.font.SysFont(None,32)
    text=font.render(f"{score[0]} - {score[1]}",True,color['black'])
    screen.blit(text,(court['width']/2-40,100))
    # Draw ball
    pygame.draw.circle(screen,color['red'],(ball['x'],ball['y']), 5)
    # Draw paddles
    pygame.draw.rect(screen,color["black"],(play1['x'],play1['y'],play1['width'],play1['height']))
    pygame.draw.rect(screen,color["black"],(play2['x'],play2['y'],play2['width'],play2['height']))
    # Bounce off top and bottom
    if ball['y'] > court['height'] - 10:
        ball['y'] = court['height'] -10
        ball['vy'] *= -1
    elif ball['y'] < 10:
        ball['y'] = 10
        ball['vy'] *= -1
    #  If intersecting with Paddle #1
    if  ball['x'] < play1['x'] + play1['width'] + 10 and ball['y'] > play1['y'] and ball['y']< play1['y']+ play1['height']:
        ball['x'] = play1['x'] + play1['width'] + 10
        ball['vx'] *= -1.1 ; # Invert and increase velocity by 10%
        ball['vy'] = random.random()*16 - 4 # Random y velocity between -4 and 4
    #  If intersecting with Paddle #2
    if  ball['x'] > play2['x'] - 10 and ball['y'] > play2['y'] and ball['y'] < play2['y'] + play2['height']: 
        ball['x'] = play2['x'] - 10
        ball['vx'] *= -1.1 ; # Invert and increase velocity by 10%
        ball['vy'] = random.random()*16 - 4 # Random y velocity between -4 and 4
    # Move Paddles
    pressed_key=pygame.key.get_pressed()
    if pressed_key[K_w] and play1['y'] > 5:
        play1['y'] -=10
    if pressed_key[K_s] and play1['y'] < court['height'] - play1['height']:
        play1['y'] +=10
    if pressed_key[K_UP] and play2['y'] > 5:
        play2['y'] -=10
    if pressed_key[K_DOWN] and play2['y'] < court['height'] - play2['height']:
        play2['y'] +=10
    # Update Score
    if ball['x'] -5 < 30:
        score[1] +=1
        ball['x'],ball['y'],ball['vx'],ball['vy'] = 350, 100, 8, 5
    if ball['x'] + 5> court['width'] - 50 + play2['width']:
        score[0] +=1
        ball['x'],ball['y'],ball['vx'],ball['vy'] = 350, 100, -8, 5
    # Move the ball
    ball['x'] += ball['vx']
    ball['y'] += ball['vy']
    pygame.display.update()
    pygame.time.wait(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


