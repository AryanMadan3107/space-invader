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








def ym():
    if keys_pressed[pygame.K_w]:
        yellow.y-=1



run=True

while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(bg,(0,0))
    pygame.draw.rect(screen,"black",border)
    screen.blit(sr,red)
    screen.blit(sy,yellow)
    keys_pressed = pygame.key.get_pressed()
    ym()
    pygame.display.update()