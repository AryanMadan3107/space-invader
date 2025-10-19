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

healthfont=pygame.font.SysFont("bookmanoldstyle",25)
winfont=pygame.font.SysFont("comicsans",100)

yellowbullet=[]
redbullet=[]

redhp=10
yellowhp=10

gameover=False
winnertext=""



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
            if event.key == pygame.K_RCTRL:
                bullet = pygame.Rect(red.x-15, red.y+47, 20, 5)
                redbullet.append(bullet)
                bulletshoot.play()
    screen.blit(bg,(0,0))
    pygame.draw.rect(screen, "black", border)
    screen.blit(sr,red)
    screen.blit(sy,yellow)
    keys_pressed = pygame.key.get_pressed()
    winnertext=""
    for bullet in yellowbullet:
        pygame.draw.rect(screen,"yellow", bullet)
        bullet.x+=2
        if red.colliderect(bullet):
            redhp-=1
            yellowbullet.remove(bullet)
            bulletcollision.play()
            if redhp<=0:
                winnertext="yellow wins!"
                gameover=True
    for bullet in redbullet:
        pygame.draw.rect(screen,"red", bullet)
        bullet.x-=2
        if yellow.colliderect(bullet):
            yellowhp-=1
            redbullet.remove(bullet)
            bulletcollision.play
            if yellowhp<=0:
                winnertext="red wins!"
                gameover=True
    if gameover==True:
        wintext=winfont.render(winnertext, True,"orange")
        screen.blit(wintext,(500,400))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        break
    redhealth=healthfont.render("health = "+str(redhp),True,"red")
    yellowhealth=healthfont.render("health = "+str(yellowhp),True,"yellow")
    screen.blit(redhealth,(1000,100))
    screen.blit(yellowhealth,(50,100))
    ym()
    rm()
    pygame.display.update()