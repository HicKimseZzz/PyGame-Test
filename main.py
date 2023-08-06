import pygame

WIDTH,HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Slayer Obama")

red_orange = (255,70,0)
gray = (174,173,172)
Box = pygame.Rect(100,40,75,75)
cccp_flag0_image = pygame.image.load("bunea.jpg")
cccp_flag0 = pygame.transform.rotate(pygame.transform.scale(cccp_flag0_image,(100,100)),0)

FPS = 60
Vel = 5
Bullets_Vel = 7
Num_Bullets = 3

def draw_window(cccp):
    WIN.fill(red_orange)
    #pygame.draw.rect(WIN,gray,Box)
    WIN.blit(cccp_flag0,(cccp.x,cccp.y))
    pygame.display.update()

def cccp_move(Keys_pressed,cccp):
    if Keys_pressed[pygame.K_UP] and cccp.y - Vel > 0:
        cccp.y -= Vel
    if Keys_pressed[pygame.K_DOWN] and cccp.y + Vel + cccp.height < 500:
        cccp.y += Vel
    if Keys_pressed[pygame.K_RIGHT] and cccp.x + Vel + cccp.width < 900:
        cccp.x += Vel
    if Keys_pressed[pygame.K_LEFT] and cccp.x - Vel > 0:
        cccp.x -= Vel

def main():
    cccp = pygame.Rect(400,200,100,100)

    Bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RCTRL and len(Bullets) < Num_Bullets:
                    Bullet = pygame.Rect(cccp.x + cccp.width, cccp.y+ cccp.height//2 - 2,10,5)
                    Bullets.append(Bullet)
                    pass
        Keys_pressed = pygame.key.get_pressed()
        Keys = pygame.key.get_repeat()
          
        draw_window(cccp)
        cccp_move(Keys_pressed,cccp)
    pygame.quit()

if __name__ == "__main__":
    main()
