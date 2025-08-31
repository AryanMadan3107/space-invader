import pygame

pygame.init()

WIDTH=1200
HEIGHT=800
screen=pygame.display.set_mode((WIDTH,HEIGHT))

border=pygame.Rect(590,0,20,800)

bg=pygame.image.load("Lesson 5/images/space (1).png")

red=pygame.Rect(900,400,100,100)
sr=pygame.image.load("Lesson 5/images/spaceship_red.png")
sr=pygame.transform.scale(sr,(100,100))
sr=pygame.transform.rotate(sr,270)

yellow=pygame.Rect(300,400,100,100)
sy=pygame.image.load("Lesson 5/images/spaceship_yellow.png")
sy=pygame.transform.scale(sy,(100,100))
sy=pygame.transform.rotate(sy,90)

bulletshoot=pygame.mixer.Sound("Lesson 5/images/Gun+Silencer.mp3")
bulletcollision=pygame.mixer.Sound("Lesson 5/images/Grenade+1.mp3")

yellowbullet=[]






def ym():
    if keys_pressed[pygame.K_w] and yellow.y>0:
        yellow.y-=1
    if keys_pressed[pygame.K_s] and yellow.y<700:
        yellow.y+=1
    if keys_pressed[pygame.K_d] and yellow.x<490:
        yellow.x+=1
    if keys_pressed[pygame.K_a] and yellow.x>0:
        yellow.x-=1

def rm():
    if keys_pressed[pygame.K_UP] and red.y>0:
        red.y-=1
    if keys_pressed[pygame.K_DOWN] and red.y<700:
        red.y+=1
    if keys_pressed[pygame.K_RIGHT] and red.x<1100:
        red.x+=1
    if keys_pressed[pygame.K_LEFT] and red.x>590:
        red.x-=1



run=True

while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                bullet = pygame.Rect(yellow.x+100, yellow.y+47, 20,5)
                yellowbullet.append(bullet)
                bulletshoot.play()
    screen.blit(bg,(0,0))
    pygame.draw.rect(screen, "black", border)
    screen.blit(sr,red)
    screen.blit(sy,yellow)
    keys_pressed = pygame.key.get_pressed()
    for bullet in yellowbullet:
        pygame.draw.rect(screen,"black", bullet)
        bullet.x+=2
    ym()
    rm()
    pygame.display.update()