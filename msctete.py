import pygame, random
pygame.init()

frstr = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Musca Tete")


ceas = pygame.time.Clock()
fps = 60

latura = 15
timp = 3
cronom = 0
scor = 0

font = pygame.font.SysFont("arial", 16)

def txt():
    text = font.render("Scor:" + str(scor), True, (255, 255, 255))
    text2 = font.render("Timp:" + str(timp), True, (255, 255, 255))
    text2Rect = text2.get_rect()
    textRect = text.get_rect()
    text2Rect.center = (50, 80)
    textRect.center = (50, 50)
    frstr.blit(text, textRect)
    frstr.blit(text2, text2Rect)

class musca(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((latura, latura))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 400 - latura
        self.rect.y = 400 - latura
        self.vit = 10
    def update(self):
        global latura, rulare
        self.x = self.rect.x
        self.y = self.rect.y
        self.taste = pygame.key.get_pressed()
        if self.taste[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.vit
        if self.taste[pygame.K_DOWN] and self.rect.y < 800 - latura:
            self.rect.y += self.vit
        if self.taste[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.vit
        if self.taste[pygame.K_RIGHT] and self.rect.x < 800 - latura:
            self.rect.x += self.vit
        if lovit:
            latura += 5
            self.image = pygame.Surface((latura, latura))
            self.image.fill((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y
            if self.vit > 1:
                self.vit -= 1
        if timp < 1:
            pygame.time.delay(2000)
            rulare = False
            

class punct(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 800 - 20)
        self.rect.y = random.randrange(0, 800 - 20)
    def update(self):
        global timp, cronom
        cronom += 1
        if cronom == fps:
            timp -= 1
            cronom = 0

toate = pygame.sprite.Group()
puncte = pygame.sprite.Group()
jucatori = pygame.sprite.Group()

msc = musca()
toate.add(msc)
jucatori.add(msc)

pct = punct()
toate.add(pct)
puncte.add(pct)

rulare = True
while rulare:
    ceas.tick(fps)
    frstr.fill((0, 0, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rulare = False

    lovit = pygame.sprite.groupcollide(jucatori, puncte, False, True)

    if lovit:
        scor += 1
        timp = 3
        cronom = 0
        pct = punct()
        toate.add(pct)
        puncte.add(pct)

    toate.update()
    toate.draw(frstr)
    txt()
    pygame.display.flip()

pygame.quit()
