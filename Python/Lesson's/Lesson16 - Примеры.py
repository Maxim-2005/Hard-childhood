import pygame

class class1(object):
    pygame.init()
    game_music = pygame.mixer.music.load('sounds\\audio.mp3')
    image = pygame.image.load('images\\BG.png')
    font = pygame.font.SysFont('serif', 32)
    msg = 'Hello World'
    text = font.render(msg, True, 'grey')

    def draw(self, g):
        g.fill('brown')
        pygame.mixer.Sound.play(self.sound)
        g.blit(self.image, (125, 325))
        pygame.mixer.music.play(-1)
        g.blit(self.text, (300, 50))
        # pygame.draw.line(g, 'yellow', (50, 50), (500, 100), 1)
        # pygame.draw.aaline(g, 'yellow', (50, 150), (500, 200), 1)
        # pygame.draw.line(g, 'red', (250, 50), (300, 200), 1)

        # pygame.draw.rect(g, 'black', (100, 100, 300, 300), 5)
        # pygame.draw.circle(g, 'white', (400, 400), 100, 5)
        # pygame.draw.ellipse(g, 'purple', (500, 300, 200, 100), 5)
        # pygame.draw.arc(g, 'orange', (300, 200, 400, 250), 6, 3, 3)

        pygame.draw.line(g, (139, 69, 19), (400, 125), (400, 500), 30)
        pygame.draw.rect(g, 'darkgreen', (300, 350, 200, 100))
        pygame.draw.rect(g, 'darkgreen', (325, 250, 150, 100))
        pygame.draw.rect(g, 'darkgreen', (350, 150, 100, 100))
        pygame.draw.rect(g, 'darkgreen', (375, 100, 50, 50))

        pygame.draw.lines(g, 'yellow', False, [(100, 100), (200, 200), (100, 200)], 5)
        pygame.draw.polygon(g, 'yellow', ((100, 200), (300, 10), (36, 80), (49, 341)), 5)

        # Проверка колизии
        def TEST(self, pos):
            if (pos[0] > self.rect.x and pos[0] < self.rect.x + self.rect.width
                    and pos[1] > self.rect.y and pos[1] < self.rect.y + self.rect.height):
                return True
            else:
                return False