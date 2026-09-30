import asyncio
import pygame

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Test Game")
clock = pygame.time.Clock()

async def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill((255, 0, 0))

        pygame.display.flip()

        clock.tick(60)

        await asyncio.sleep(0)

    pygame.quit()

asyncio.run(main())