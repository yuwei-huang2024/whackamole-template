import pygame, sys
import random

def draw_grid(screen):
    #draw horizontal lines
    for i in range(1, 16):
        pygame.draw.line(
            screen,
            (39,59,221),
            (0, i * 32),
            (660, i * 32),
        )
    #draw vertical lines
    for i in range(1, 20):
        pygame.draw.line(
            screen,
            (39,59,221),
            (i * 32, 0),
            (i * 32, 528),
        )

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 512))
    screen.fill((139,212,205))
    draw_grid(screen)
    pygame.display.update()
    try:
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen.blit(mole_image, mole_image.get_rect(topleft=(3, 3)))
        pygame.display.update()
        mole_width = 3
        mole_length = 3
        #clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mole_rectangle = pygame.Rect(mole_width - 3, mole_length - 3, 32, 32)
                    if mole_rectangle.collidepoint(event.pos):
                        mole_width_box = random.randrange(1, 20)
                        mole_length_box = random.randrange(1, 16)
                        mole_width = 3 + 32 * mole_width_box
                        mole_length = 3 + 32 * mole_length_box
                        screen.fill((139, 212, 205))
                        draw_grid(screen)
                        screen.blit(mole_image, mole_image.get_rect(topleft=(mole_width, mole_length)))
                        pygame.display.update()
                        # print(mole_width, mole_length)
            #pygame.display.flip()
            #clock.tick(60)
    finally:
            pygame.quit()


if __name__ == "__main__":
    main()
