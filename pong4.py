import pygame,sys,random
from pygame.locals import *

(w, h, blk) = ( 700, 500, 10 )
(WHITE,BLACK,RED,GREEN,BLUE) = ((255,255,255), (0,0,0), (255,0,0), (0,255,0), (0,0,255))
(rw, rh, rv) = (10, 50, 10)
(cx, cy, ps, cvymax) = (blk, h//2 - rh//2, 0, 5)
(px, py, cs) = (w - blk - rw, h//2 - rh//2, 0)
(bx, by, br, bvx, bvy, bvxmin, bvymin, bvxmax, bvymax)  = ( w//2, h//2, 5, 8, 5, 8, 5, 20, 15)

pygame.init()
screen=pygame.display.set_mode((w, h))
pygame.mouse.set_visible(False)  
level=1.0
run=True
while run:
    screen.fill(BLACK)
    # Draw center line
    for i in range(blk,h,h//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(screen,WHITE,(w//2-5,i,10,h//20))
    # Draw paddles
    pygame.draw.rect(screen, WHITE, (px, py, rw, rh))
    pygame.draw.rect(screen, WHITE, (cx, cy, rw, rh))

    # Draw ball
    pygame.draw.circle(screen, RED, (bx, by), br)
    # Show Score
    font=pygame.font.SysFont(None,64)
    text=font.render(f"{cs}   {ps}", True, WHITE)
    screen.blit(text,(w//2-text.get_width()//2, 20))

    # Move Paddle of Player
    #pressed_key=pygame.key.get_pressed()
    #if pressed_key[K_UP] and py > 0:
    #    py += -rv
    #if pressed_key[K_DOWN] and py < h - rh:
    #    py += rv
    mx,my=pygame.mouse.get_pos()
    py = 0 if my < 0 else h - rh if my > h - rh else my
    
     # Computer AI
    bcx = bx - cx + rh
    bcy = by - (cy + rh)
    pcx = px - cx
    cvy = 0
    if bvx < 0 and bcx < pcx * level:
        if bcy >0:
            cvy = min(bcy,cvymax)
        else:
            cvy = max(bcy,-cvymax)
    # Move paddle of Computer
    cy += cvy
    cy = 0 if cy< 0 else h - rh if cy > h -rh else cy

    # Move the ball
    bx += bvx
    by += bvy

    # Bounce off top and bottom
    if by < br :
        by = br
        bvy = -bvy
    elif by + br > h:
        by = h - br
        bvy = -bvy 

    #  If intersecting with Computer
    if bx - br < cx + rw and by > cy and by < cy+ rh:
        bx = cx + rw + br
        bvx *= -1.1 # Invert and increase velocity by 10%
        bvy = random.random() * bvymax * 2 - bvymax # Random y velocity between -bvymax and bvymax
    #  If intersecting with Player
    elif bx + br > px and by > py and by < py + rh: 
        bx = px - br
        bvx *= -1.1 # Invert and increase velocity by 10%
        bvy = random.random() * bvymax * 2 - bvymax # Random y velocity between -bvymax and bvymax
    
    bvx = bvxmax if bvx > bvxmax else -bvxmax if bvx<-bvxmax else bvx
    
    # Update Score
    if bx  < 0:
        ps +=1
        (bx, by, bvx, bvy) = (px - br, py + rh//2, -bvxmin, bvymin)
    elif bx > w:
        cs +=1
        (bx, by, bvx, bvy) = (cx + br, cy + rh//2, bvxmin, bvymin)

    # Show Game Over
    if ps == 10 or cs == 10:
        font=pygame.font.SysFont(None,128)
        text=font.render("Game Over", True, BLUE)
        screen.blit(text,(w//2-text.get_width()//2, h * 1//3))

        font=pygame.font.SysFont(None,80)
        text=font.render("You Win !!" if ps==10 else "You Lost !!", True, RED)
        screen.blit(text,(w//2-text.get_width()//2, h * 2//3))
        run = False
    pygame.display.update()
    pygame.time.wait(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE: #エスケープキーが押されたら終了
                pygame.quit()
                sys.exit()

pygame.time.wait(3000)
pygame.quit()
sys.exit()