import sys, pygame, random, pygame_widgets, lance, os, json
from pygame_widgets.button import Button

pygame.init()
pygame.font.init()

class Hra:
    def __init__(self) -> None:
        self.file_path = './file.json'
        check_file = os.path.isfile(self.file_path)
        """if(check_file):
            print('FILE EXIST!')
        else:
            print('FILE NOT EXIST!')"""
        self.dvojkoskta = Dvojkostka()
        self.bar = Bar()
        

        volba = input("Budeš hrát s hráčem (1), nebo s AI (0)?")
        if volba == "1":
            hrac1 = input("Jméno hráče 1: ")
            self.Hrac1 = KonzolovyHrac(hrac1, "Bila")
            hrac2 = input("Jméno hráče 2: ")
            self.Hrac2 = KonzolovyHrac(hrac2, "Cerna")
        elif volba == "0":
            hrac1 = input("Jméno hráče 1: ")
            self.Hrac1 = KonzolovyHrac(hrac1, "Bila")
            hrac2 = input("Jméno Ai 1: ")
            self.Hrac2 = AiHrac(hrac2, "Cerna")
        self.plocha = HerniPole(self.Hrac1, self.Hrac2)
        self.Hrac1 = KonzolovyHrac(hrac1, "Bila")
        self.Hrac2 = KonzolovyHrac(hrac2, "Cerna")
        self.aktualni_hrac = self.Hrac1  # Nastavení počátečního hráče na Hrac1

    def zmenit_tah(self):
        if self.aktualni_hrac == self.Hrac1:
            self.aktualni_hrac = self.Hrac2
        else:
            self.aktualni_hrac = self.Hrac1
    

    def Ulozit(self) -> None:
        data = {
            'Bily': self.bar.pocet_zetonu_bila_cil,
            'Cerny': self.bar.pocet_zetonu_cerna_cil,
            'Player1': {
                'Jmeno': self.Hrac1.jmeno,
                'Barva': self.Hrac1.barva,
                'Score': self.bar.pocet_zetonu_bila_cil,
               # 'Pole': self.Hrac1.policko 
            },
            'Player2': {
                'Jmeno': self.Hrac2.jmeno,
                'Barva': self.Hrac2.barva,
                'Score': self.bar.pocet_zetonu_cerna_cil,
               # 'Pole': self.Hrac2.policko 
            }
        }
        with open(self.file_path, 'w') as file:
            json.dump(data, file)
        print("Hra byla uložena.")

    def Nahrat(self) -> None:
        data = {
            'Bily': self.bar.pocet_zetonu_bila_cil,
            'Cerny': self.bar.pocet_zetonu_cerna_cil,
            'Player1': {
                'Jmeno': self.Hrac1.jmeno,
                'Barva': self.Hrac1.barva,
                'Score': self.bar.pocet_zetonu_bila_cil,
               # 'Pole': self.Hrac1.policko 
            },
            'Player2': {
                'Jmeno': self.Hrac2.jmeno,
                'Barva': self.Hrac2.barva,
                'Score': self.bar.pocet_zetonu_cerna_cil,
               # 'Pole': self.Hrac2.policko 
            }
        }
        with open(self.file_path, 'r') as file:
            json.load(file)
        print("Hra byla nahrána.")

class HerniPole:
    def __init__(self, Hrac1, Hrac2) -> None:
        self.sirka = 1450
        self.vyska = 1000
        self.obraz = pygame.display.set_mode((self.sirka,self.vyska))
        self.obraz.fill((255,155,50))
        self.hrac1 = Hrac1
        self.hrac2 = Hrac2
        self.aktualni_hrac = Hrac1

        rect = pygame.Rect(1220, 0, 280, 1000)
        black = (0,0,0)
        pygame.draw.rect(self.obraz, black, rect)
        
        white = (255,255,255)
        font = pygame.font.SysFont("Open Sans", 21)
        text_surface = font.render("Na tahu je hráč: " + self.aktualni_hrac.jmeno, True, white)
        text_rect = text_surface.get_rect()
        text_rect.center = (1350, 500)
        self.obraz.blit(text_surface, text_rect)

        self.tlacitko_hod = Button(self.obraz, 
                                   1290, 
                                   750, 
                                   100, 
                                   80,
                                   padding=20,
                                   text='Hod Kostkami',
                                   onClick=lambda: new.dvojkoskta.hod_kostkou())
        
        self.ulozit_tlacitko = Button(self.obraz, 
                                      1290,
                                      110,
                                      100,
                                      70,
                                      padding=20,
                                      text='Ulozit',
                                      onClick=lambda: new.Ulozit())
        
        self.nahrat_tlacitko = Button(self.obraz, 
                                      1290,
                                      210,
                                      100,
                                      70,
                                      padding=20,
                                      text='Nahrat',
                                      onClick=lambda: new.Nahrat())

        self.seznam_pol = []
        self.polygon_24 = Polygon(24, (100,100,100), ((1000+100,0),(1000+200,0),(1000+150,350)))
        self.polygon_23 = Polygon(23, (150,0,0), ((1000,0),(1000+100,0),(1000+50,350)))
        self.polygon_22 = Polygon(22, (100,100,100), ((800+100,0),(800+200,0),(800+150,350)))
        self.polygon_21 = Polygon(21, (150,0,0), ((800,0),(800+100,0),(800+50,350)))
        self.polygon_20 = Polygon(20, (100,100,100), ((600+100,0),(600+200,0),(600+150,350)))
        self.polygon_19 = Polygon(19, (150,0,0), ((600,0),(600+100,0),(600+50,350)))
        self.polygon_18 = Polygon(18, (100,100,100), ((400+100,0),(400+200,0),(400+150,350)))
        self.polygon_17 = Polygon(17, (150,0,0), ((400,0),(400+100,0),(400+50,350)))
        self.polygon_16 = Polygon(16, (100,100,100), ((200+100,0),(200+200,0),(200+150,350)))
        self.polygon_15 = Polygon(15, (150,0,0), ((200,0),(200+100,0),(200+50,350)))
        self.polygon_14 = Polygon(14, (100,100,100), ((0+100,0),(0+200,0),(0+150,350)))
        self.polygon_13 = Polygon(13, (150,0,0), ((0,0),(0+100,0),(0+50,350)))
        self.polygon_12 = Polygon(12,(100,100,100), ((0,1000),(0+100, 1000),(0+50, 650)))
        self.polygon_11 = Polygon(11,(150,0,0), ((0+100,1000),(0+200, 1000),(0+150, 650)))
        self.polygon_10 = Polygon(10,(100,100,100), ((200,1000),(200+100, 1000),(200+50, 650)))
        self.polygon_9 = Polygon(9,(150,0,0), ((200+100,1000),(200+200, 1000),(200+150, 650)))
        self.polygon_8 = Polygon(8,(100,100,100), ((400,1000),(400+100, 1000),(400+50, 650)))
        self.polygon_7 = Polygon(7,(150,0,0), ((400+100,1000),(400+200, 1000),(400+150, 650)))
        self.polygon_6 = Polygon(6,(100,100,100), ((600,1000),(600+100, 1000),(600+50, 650)))
        self.polygon_5 = Polygon(5,(150,0,0), ((600+100,1000),(600+200, 1000),(600+150, 650)))
        self.polygon_4 = Polygon(4,(100,100,100), ((800,1000),(800+100, 1000),(800+50, 650)))
        self.polygon_3 = Polygon(3,(150,0,0), ((800+100,1000),(800+200, 1000),(800+150, 650)))
        self.polygon_2 = Polygon(2,(100,100,100), ((1000,1000),(1000+100, 1000),(1000+50, 650)))
        self.polygon_1 = Polygon(1,(150,0,0), ((1000+100,1000),(1000+200, 1000),(1000+150, 650)))

        self.seznam_pol.append(self.polygon_1)
        self.seznam_pol.append(self.polygon_2)
        self.seznam_pol.append(self.polygon_3)
        self.seznam_pol.append(self.polygon_4)
        self.seznam_pol.append(self.polygon_5)
        self.seznam_pol.append(self.polygon_6)
        self.seznam_pol.append(self.polygon_7)
        self.seznam_pol.append(self.polygon_8)
        self.seznam_pol.append(self.polygon_9)
        self.seznam_pol.append(self.polygon_10)
        self.seznam_pol.append(self.polygon_11)
        self.seznam_pol.append(self.polygon_12)
        self.seznam_pol.append(self.polygon_13)
        self.seznam_pol.append(self.polygon_14)
        self.seznam_pol.append(self.polygon_15)
        self.seznam_pol.append(self.polygon_16)
        self.seznam_pol.append(self.polygon_17)
        self.seznam_pol.append(self.polygon_18)
        self.seznam_pol.append(self.polygon_19)
        self.seznam_pol.append(self.polygon_20)
        self.seznam_pol.append(self.polygon_21)
        self.seznam_pol.append(self.polygon_22)
        self.seznam_pol.append(self.polygon_23)
        self.seznam_pol.append(self.polygon_24)
        """for i in range(0,1001, 200):
            polygon_1 = pygame.draw.polygon(self.obraz, (100,100,100), ((i,1000),(i+100,1000),(i+50,650)))
            polygon_2 = pygame.draw.polygon(self.obraz, (150,0,0), ((i+100,1000),(i+200,1000),(i+150,650)))
            self.seznam_pol.append(polygon_1)
            self.seznam_pol.append(polygon_2)

        for i in range(0,1001, 200):
            polygon_1 = pygame.draw.polygon(self.obraz, (100,100,100), ((i,0),(i+100,0),(i+50,350)))
            polygon_2 = pygame.draw.polygon(self.obraz, (150,0,0), ((i+100,0),(i+200,0),(i+150,350)))
            self.seznam_pol.append(polygon_1)
            self.seznam_pol.append(polygon_2)"""

        pygame.draw.rect(self.obraz, (155,155,155), (400,450, 400,100))
        pygame.draw.rect(self.obraz, (255,255,255), (0,475, 200,50))
        pygame.draw.rect(self.obraz, (0,0,0), (1000,475, 200,50))

        pygame.display.flip()

class Polygon:
    def __init__(self, cislo_pole, barva, souradnice, zasobnik = [], seznam_pol = []) -> None:
        self.cislo_pole = cislo_pole
        self.barva = barva
        self.souradnice = souradnice
        self.zasobnik = zasobnik
        self.seznam_pol = seznam_pol


    def vytvor_polygon(self):
        polygon = pygame.draw.polygon(new.plocha.obraz, (self.barva), (self.souradnice))
        self.seznam_pol.append(polygon)

    def pridej_kruh(self):
        if len(self.zasobnik<5):
            self.zasobnik = self.zasobnik + 1
        else:
            print("Plný zásobník!")

    def sundej_kruh(self):
        if len(self.zasobnik > 0):
            self.zasobnik = self.zasobnik - 1
        else:
            print("Prázdný zásobník") 




class Dvojkostka:
    def __init__(self) -> None:
        self.kostka1 = None
        self.kostka2 = None
        self.tlacitko = True

        self.jedna = pygame.image.load('1.png')
        self.dva = pygame.image.load('2.png')
        self.tri = pygame.image.load('3.png')
        self.ctyri = pygame.image.load('4.png')
        self.pet = pygame.image.load('5.png')
        self.sest = pygame.image.load('6.png')
        

    def hod_kostkou(self) -> str:
        self.kostka1 = random.randrange(1,7)
        self.kostka2 = random.randrange(1,7)
        if self.kostka1 == 1:
            new.plocha.obraz.blit(self.jedna, (525,450))
        elif self.kostka1 == 2:
            new.plocha.obraz.blit(self.dva, (525,450))
        elif self.kostka1 == 3:
            new.plocha.obraz.blit(self.tri, (525,450))
        elif self.kostka1 == 4:
            new.plocha.obraz.blit(self.ctyri, (525,450))
        elif self.kostka1 == 5:
            new.plocha.obraz.blit(self.pet, (525,450))
        elif self.kostka1 == 6:
            new.plocha.obraz.blit(self.sest, (525,450))

        if self.kostka2 == 1:
            new.plocha.obraz.blit(self.jedna, (600,450))
        elif self.kostka2 == 2:
            new.plocha.obraz.blit(self.dva, (600,450))
        elif self.kostka2 == 3:
            new.plocha.obraz.blit(self.tri, (600,450))
        elif self.kostka2 == 4:
            new.plocha.obraz.blit(self.ctyri, (600,450))
        elif self.kostka2 == 5:
            new.plocha.obraz.blit(self.pet, (600,450))
        elif self.kostka2 == 6:
            new.plocha.obraz.blit(self.sest, (600,450))

        return f"Hodil jsi: [{self.kostka1}, {self.kostka2}]"
    
    

class Bar:
    def __init__(self) -> None:
        self.pocet_zetonu_bila_cil = 0
        self.pocet_zetonu_cerna_cil = 0
        self.zeton = None

    def vytvor_zeton_cerny(self):
        self.zeton = HerniKamen(200,200, (0,0,0))
        self.zeton.vytvor_zeton()

    def vytvor_zeton_bily(self):
        self.zeton = HerniKamen(200,200, (255,255,255))
        self.zeton.vytvor_zeton()
        
class HerniKamen:
    def __init__(self, x, y, barva) -> None:
        self.x = x
        self.y = y
        self.vyska = 30
        self.sirka = 10
        self.pozice = 0
        self.barva = barva
        self.kruh = None
        self.kruhy = []

    def akt_pozice(self) -> str:
        return f"Aktuální pozice = [{self.pozice}]"
    
    def vytvor_zeton(self):
        print(new.plocha.seznam_pol)
        """if self.barva == (0,0,0):
            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[0].centerx, new.plocha.seznam_pol[0].bottom - self.vyska], 30, 0))
            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[0].centerx, new.plocha.seznam_pol[0].bottom - self.vyska *3 ], 30, 0))
            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[0].centerx, new.plocha.seznam_pol[0].bottom - self.vyska *5 ], 30, 0))
            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[0].centerx, new.plocha.seznam_pol[0].bottom - self.vyska *7], 30, 0))
            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[0].centerx, new.plocha.seznam_pol[0].bottom - self.vyska *9], 30, 0))

            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[6].centerx, new.plocha.seznam_pol[17].top + self.vyska], 30, 0))
            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[6].centerx, new.plocha.seznam_pol[17].top + self.vyska *3], 30, 0))
            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[6].centerx, new.plocha.seznam_pol[17].top + self.vyska *5], 30, 0))
            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[6].centerx, new.plocha.seznam_pol[17].top + self.vyska *7], 30, 0))
            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[6].centerx, new.plocha.seznam_pol[17].top + self.vyska *9], 30, 0))

            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[4].centerx, new.plocha.seznam_pol[19].top + self.vyska], 30, 0))
            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[4].centerx, new.plocha.seznam_pol[19].top + self.vyska *3], 30, 0))
            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[4].centerx, new.plocha.seznam_pol[19].top + self.vyska *5], 30, 0))

            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[11].centerx, new.plocha.seznam_pol[11].bottom - self.vyska], 30, 0))
            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[11].centerx, new.plocha.seznam_pol[11].bottom - self.vyska *3 ], 30, 0))

        if self.barva == (255,255,255):
            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[0].centerx, new.plocha.seznam_pol[23].top + self.vyska], 30, 0))
            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[0].centerx, new.plocha.seznam_pol[23].top + self.vyska *3], 30, 0))
            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[0].centerx, new.plocha.seznam_pol[23].top + self.vyska *5], 30, 0))
            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[0].centerx, new.plocha.seznam_pol[23].top + self.vyska *7], 30, 0))
            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[0].centerx, new.plocha.seznam_pol[23].top + self.vyska *9], 30, 0))

            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[6].centerx, new.plocha.seznam_pol[6].bottom - self.vyska], 30, 0))
            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[6].centerx, new.plocha.seznam_pol[6].bottom - self.vyska *3 ], 30, 0))
            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[6].centerx, new.plocha.seznam_pol[6].bottom - self.vyska *5 ], 30, 0))
            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[6].centerx, new.plocha.seznam_pol[6].bottom - self.vyska *7], 30, 0))  
            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[6].centerx, new.plocha.seznam_pol[6].bottom - self.vyska *9], 30, 0))

            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[4].centerx, new.plocha.seznam_pol[4].bottom - self.vyska], 30, 0))
            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[4].centerx, new.plocha.seznam_pol[4].bottom - self.vyska *3], 30, 0))
            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[4].centerx, new.plocha.seznam_pol[4].bottom - self.vyska *5], 30, 0))

            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[11].centerx, new.plocha.seznam_pol[12].top + self.vyska], 30, 0))
            self.kruhy.append(pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[11].centerx, new.plocha.seznam_pol[12].top + self.vyska *3], 30, 0))"""
        

class Hrac:
    def __init__(self, jmeno, barva) -> None:
        self.jmeno = jmeno
        self.barva = barva
    
    def vypis_hrace(self) -> str:
        return print(f"Hráč: {self.jmeno}, barva: {self.barva}")

class KonzolovyHrac(Hrac):
    pass

class AiHrac(Hrac):
    pass

new = Hra()
font = pygame.font.SysFont('Arial', 30)
new.plocha.obraz.blit(font.render(new.Hrac1.jmeno, True, (255,0,0)), (0, 480))
new.plocha.obraz.blit(font.render(new.Hrac2.jmeno, True, (255,0,0)), (1000, 480))
#new.bar.vytvor_zeton_bily()

new.plocha.polygon_24.vytvor_polygon()
new.plocha.polygon_23.vytvor_polygon()
new.plocha.polygon_22.vytvor_polygon()
new.plocha.polygon_21.vytvor_polygon()
new.plocha.polygon_20.vytvor_polygon()
new.plocha.polygon_19.vytvor_polygon()
new.plocha.polygon_18.vytvor_polygon()
new.plocha.polygon_17.vytvor_polygon()
new.plocha.polygon_16.vytvor_polygon()
new.plocha.polygon_15.vytvor_polygon()
new.plocha.polygon_14.vytvor_polygon()
new.plocha.polygon_13.vytvor_polygon()
new.plocha.polygon_12.vytvor_polygon()
new.plocha.polygon_11.vytvor_polygon()
new.plocha.polygon_10.vytvor_polygon()
new.plocha.polygon_9.vytvor_polygon()
new.plocha.polygon_8.vytvor_polygon()
new.plocha.polygon_7.vytvor_polygon()
new.plocha.polygon_6.vytvor_polygon()
new.plocha.polygon_5.vytvor_polygon()
new.plocha.polygon_4.vytvor_polygon()
new.plocha.polygon_3.vytvor_polygon()
new.plocha.polygon_2.vytvor_polygon()
new.plocha.polygon_1.vytvor_polygon()

new.bar.vytvor_zeton_cerny()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if pygame.key.get_pressed()[pygame.K_q]:
        new.Ulozit()
        pygame.quit()
        sys.exit()
        
    pygame_widgets.update(events)
    pygame.display.update()

#Dodělat základní rozestavení, hlavně nasazování žetonů na sebe
