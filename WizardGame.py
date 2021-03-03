import pygame
import pygame.surface
Harry = pygame.image.load("HarryPotter.png")
Title = pygame.image.load("Title.png")
StartMenu = pygame.image.load("Start Menu.png")
Rule = pygame.image.load("Rule.png")
GoBack = pygame.image.load("GoBack.png")
Controls = pygame.image.load("Controls.png")
ClicktoBegin = pygame.image.load("Clicktobegin.png")
screen = pygame.display.set_mode((1600, 1000))


screen.fill((255, 255, 255))
screen.blit(Harry, (150, 300))
screen.blit(Title, (500,50))
screen.blit(StartMenu, (800, 400))
pygame.display.flip()



def main():
    pygame.init()
    logo = pygame.image.load("HarryPotter.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Wizard Game")

    Play = False
    Rules = False
    Start = False
    running = True
    ready = False
    Score = 0
    xvalue = 300
    HarryShoot = pygame.transform.scale(Harry, (50, 30))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r and Play == False:
                screen.fill((255, 255, 255))
                screen.blit(Rule, (500, 500))
                screen.blit(Title, (500, 50))
                screen.blit(GoBack, (500, 800))
                pygame.display.flip()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and Play == False:
                screen.fill((255, 255, 255))
                screen.blit(Harry, (150, 300))
                screen.blit(Title, (500, 50))
                screen.blit(StartMenu, (800, 400))
                pygame.display.flip()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s and Play == False:
                Start = True
                Play = True
                screen.fill((255, 255, 255))
                screen.blit(Controls, (1250, 10))
                pygame.display.flip()
                pygame.time.wait(3000)
                screen.blit(ClicktoBegin, (300, 500))
                pygame.display.flip()

                while not ready:
                    event = pygame.event.wait()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        ready = True
                        screen.fill((52, 61, 82))
                        pygame.display.flip()
                    screen.blit(HarryShoot, (150, 300))
                    pygame.display.flip()


                






if __name__ == "__main__":
    main()