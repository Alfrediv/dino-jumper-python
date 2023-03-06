import random 
import pygame
print("hello world")#testing purposes
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Test")
doExit=False
clock = pygame.time.Clock()
p1x=20
p1y=450
yVel = 0 
score = 0
#touch ground
touchGround = False 
#creates 5 slot list 
CactusHeights= [80,40,20,80,30]

CactusXpos=[]

for x in range(1, 5):
    CactusXpos.append(random.randrange(200, 3000))
CactusImg = pygame.image.load('cactus1.png')

#Game loop##############################################
while not doExit:
    #Timer section///////////////////////////////////////
    clock.tick(60)
    score+=1
    print("score:", score)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
    #update cactus location if they're off the screen 
    for x in range(len(CactusXpos)):
        if CactusXpos[x]<0:
            CactusXpos[x]=random.randrange(640,5000)
            print("Reset to ", CactusXpos[x])         
    # check for player hitting cactus 
    for x, y in zip(CactusXpos, CactusHeights):
        a = pygame.Rect((x, 480-y), (30, 80))
        b = pygame.Rect((p1x, p1y), (30, 30))
        if a.colliderect(b) == True:
            print("COLLISION")
            #doExit=true
            #winsound.Beep(900,900)

    #check for pkayer/cactus collison 
    for x, y in zip(CactusXpos, CactusHeights):
        a=pygame.Rect((x, 480-y), (30, 80))
        b=pygame.Rect((p1x, p1y), (30, 30))
        if a.colliderect(b) == True:
            print("COLLISION")

#moves cactus
    CactusXpos = [x - 5 for x in CactusXpos]
    #update position by adding velocity to position 
    p1y += yVel


    #turn off flying 
    if (p1y+30) == 480:
        touchGround = True
    else:
        touchGround = False

    #gravity 
    if (p1y+30) < 480:
        p1y+1
        touchGround = False
    if touchGround == False:
        yVel += 1
    else: 
        yVel = 0
  
        #input section///////////////////////////////////////
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and touchGround == True:
        yVel -= 40
        touchGround = False

    #render section///////////////////////////////////////////////
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 255, 255), (p1x, p1y, 30, 30), 0)
    #draws catuses 
    for x, y in zip(CactusXpos, CactusHeights):
        screen.blit(CactusImg, (x-15,480-y))
    #update the screen
    pygame.display.flip()

