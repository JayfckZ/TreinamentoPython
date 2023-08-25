from random import randint
from time import sleep

class ser_vivo:
    def __init__(self, vida, ataque):
        self.vida: int = vida
        self.ataque: int = ataque

    def atacar(self, defensor):
        if isinstance(defensor, esqueleto):
            n = randint(1, 7)

            if n <= defensor.agilidade:
                print(f"{defensor.tipo} esquivou de seu ataque.")
                
            else:
                defensor.vida -= self.ataque
                if isinstance(self, heroi):
                    print(f"\n{self.nome} causou {self.ataque} de dano.")
                else:
                    print(f"\n{self.tipo} causou {self.ataque} de dano.")
        else:
            defensor.vida -= self.ataque
            if isinstance(self, heroi):
                print(f"\n{self.nome} causou {self.ataque} de dano.")
            else:
                print(f"\n{self.tipo} causou {self.ataque} de dano.")
            

    def tomar_pocao(self, defensor):    
        n = randint(0, 100)
        if self.hma6 == True:
            if n <= 15:
                print("Tomou Poção Abençoada. +75HP")
                self.vida += 75
            elif n <= 45:
                print("Tomou Poção de Cura Melhorada. +50HP")
                self.vida += 50
            else:
                print("Tomou Poção de Cura. +25HP")
                self.vida += 25
        else: 
            if n <= 5:
                print("Tomou Poção Abençoada. +75HP")
                self.vida += 75
            elif n <= 20:
                print("Tomou Poção de Cura Melhorada. +50HP")
                self.vida += 50
            else:
                print("Tomou Poção de Cura. +25HP")
                self.vida += 25

        n = randint (0, 100)  
        if n <= 25:
            sleep(0.5)
            self.vida -= defensor.ataque
            print(f"{defensor.tipo} te atacou enquanto você tomava sua poção e causou {defensor.ataque} de dano!")

        return n
        
    def round(self):
        cmd = int(input("------------------------"
                        "\n1- Atacar"
                        "\n2- Curar"
                        "\n3- Encontrar outro inimigo."
                        "\n4- Fugir"
                        "\nSelecione a ação: "))
        print("------------------------")
        return cmd

#-----------------------------------------------------------------------------------------------------------#

class heroi(ser_vivo):
    def __init__(self, vida, ataque, nome, vidamax):
        super().__init__(vida, ataque)
        self.nome: str = nome
        self.vidamax: int = vidamax

        self.classes: str = ["", ""]
        self.numclasses: int = 0
        
        self.xp: int = 0
        self.nvl1: int = 0
        self.nvl2: int = 0

        self.hg4: bool = False
        self.hg6: bool = False
        
        self.hma4: bool = False
        self.hma6: bool = False

        self.hc4: bool = False
        self.hc6: bool = False



        self.armadura: int = 0          # A FAZER
        self.moedas: int = 0            # A FAZER
        
        self.itens = {
        "Couro de Lobo": -1,
        "Ossos de Esqueleto": -2,
        "Rubi de Vaelin": False,
        "Pedra Mística do Wizzle": False,
        "Cristais de Malikard": False,
        "Cristais de Kiravin": False,
        "Tesouro de Satoro": False,
        "Couro de Dragão": -1,
        "Couro de Dragão Branco": -1,
        "Couro de Dragão Negro": -1
        }

    def atacar(self, defensor):
        super().atacar(defensor)
        
#       TESTE PARA VER SE O INIMIGO CONTRA-ATACA
        sleep(1)
        n = randint (0, 100)
        n2 = randint (0, 100)

        if isinstance(defensor, goblin) or isinstance(defensor, troll):
            n -= defensor.inteligencia

        if (n <= 30) and (defensor.vida >= 0):
            if self.hg4 == True:
                if self.hg6 == True and n2 <= 35:
                    n2 = randint(0, 100)

                    if n2 <= 10:
                        defensor.vida -= 80
                        print("Você conseguiu bloquear o ataque inimigo e infligir um enorme dano!")
                    else:
                        print("Você bloqueou uma investida inimiga.")

                elif n2 <= 20:
                    print("Você bloqueou uma investida inimiga.")

            elif self.hc6 == True:
                n = randint(1, 100)

                if n <= 60:
                    print("Você se esquivou de uma investida inimiga!")
                else:
                    if (isinstance(defensor, lobo)) and (n < 30): 
                        self.vida -= int(defensor.ataque * defensor.forca)
                        print(f"{defensor.tipo} conseguiu revidar e causou {int(defensor.ataque * defensor.forca)} de dano!")
                    elif isinstance(defensor, troll):
                        self.vida -= defensor.ataque
                        print(f"{defensor.tipo} conseguiu revidar e causou {defensor.ataque} de dano!")
                        defensor.vida += defensor.regeneracao
                        print(f"O {defensor.tipo} regenerou {defensor.regeneracao}! Cuidado com seus ataques!")
                    else:
                        self.vida -= defensor.ataque
                        print(f"{defensor.tipo} conseguiu revidar e causou {defensor.ataque} de dano!")

            else:            
                if (isinstance(defensor, lobo)) and (n < 30): 
                    self.vida -= int(defensor.ataque * defensor.forca)
                    print(f"{defensor.tipo} conseguiu revidar e causou {int(defensor.ataque * defensor.forca)} de dano!")
                elif isinstance(defensor, troll):
                        self.vida -= defensor.ataque
                        print(f"{defensor.tipo} conseguiu revidar e causou {defensor.ataque} de dano!")
                        defensor.vida += defensor.regeneracao
                        print(f"O {defensor.tipo} regenerou {defensor.regeneracao}! Cuidado com seus ataques!")
                else:
                    self.vida -= defensor.ataque
                    print(f"{defensor.tipo} conseguiu revidar e causou {defensor.ataque} de dano!")
        
        sleep(0.5)
        if defensor.vida <= 0:
            print(f"\nVocê derrotou {defensor.tipo} com sucesso!")
            print(f"Sua vida: {self.vida}HP")
        else:
            print(f"\n{self.nome}: {self.vida}HP\n"
                  f"{defensor.tipo}: {defensor.vida}HP")

    def tomar_pocao(self, pocoes, defensor):
        if pocoes > 0:
            n = super().tomar_pocao(defensor=defensor)

            if self.vida >= self.vidamax:
                self.vida = self.vidamax
                
                print("Vida máxima atingida.", end=' ')
                if n <= 25:
                    self.vida -= defensor.ataque
                    print(f"Dano recebido de {defensor.tipo}.")
            
            print(f"Sua vida: {self.vida}HP\n"
                  f"Poções restantes: {pocoes-1}\n")
            sleep(1)
        else:
            print("Você não tem mais poções disponíveis nesta luta.")
            sleep(1)

    def conquista(self, defensor):
        if isinstance(defensor, lobo):
            if self.itens["Couro de Lobo"] < 0:
                print(f"Ao derrotar {defensor.tipo} você aprendeu a esfolar seu couro.")
                self.itens["Couro de Lobo"] = 0

            if self.hc6 == True:
                n = randint(1, 100)
                
                if n <= 20:
                    self.itens["Couro de Lobo"] += 4
                    print("Item obtido: Couro de Lobo x4\n")
                elif n <= 60:
                    self.itens["Couro de Lobo"] += 3
                    print("Item obtido: Couro de Lobo x3\n")
                else:
                    self.itens["Couro de Lobo"] += 2
                    print("Item obtido: Couro de Lobo x2\n")
            
            elif self.hc4 == True:
                n = randint(1, 100)

                if n <= 15:
                    self.itens["Couro de Lobo"] += 3
                    print("Item obtido: Couro de Lobo x3\n")
                else:
                    self.itens["Couro de Lobo"] += 2
                    print("Item obtido: Couro de Lobo x2\n")

            else:
                self.itens["Couro de Lobo"] += 1
                print("Item obtido: Couro de Lobo x1\n")
        
        if isinstance(defensor, esqueleto):
            if self.itens["Ossos de Esqueleto"] < 0:
                print(f"Ao derrotar {defensor.tipo} você aprendeu a remover seus ossos restantes.")
                self.itens["Ossos de Esqueleto"] = 0
            
            if self.hc4 == True:
                n = randint(1, 100)
                
                if n <= 15:
                    self.itens["Ossos de Esqueleto"] += 6
                    print("Item obtido: Ossos de Esqueleto x6\n")
                else:
                    self.itens["Ossos de Esqueleto"] += 4
                    print("Item obtido: Ossos de Esqueleto x4\n")
            
            elif self.hc6 == True:
                n = randint(1, 100)

                if n <= 20:
                    self.itens["Ossos de Esqueleto"] += 8
                    print("Item obtido: Ossos de Esqueleto x8\n")
                elif n <= 60:
                    self.itens["Ossos de Esqueleto"] += 6
                    print("Item obtido: Ossos de Esqueleto x6\n")
                else:
                    self.itens["Ossos de Esqueleto"] += 4
                    print("Item obtido: Ossos de Esqueleto x4\n")
                    
            else:
                self.itens["Ossos de Esqueleto"] += 2
                print("Item obtido: Ossos de Esqueleto x2\n")
        
        if isinstance(defensor, vaelin):
            if self.itens["Rubi de Vaelin"] == False:
                print(f"Ao derrotar Vaelin ele cumpre sua parte do acordo e lhe entrega o Rubi da Cripta Perdida.")

            self.itens["Rubi de Vaelin"] = True
            print("Item obtido: Rubi de Vaelin\n")

        if isinstance(defensor, wizzle):
            if self.itens["Pedra Mística do Wizzle"] == False:
                print(f"Ao deter a ameaça de Wizzle você pega para si sua relíquia, A Pedra Mística.")

            self.itens["Pedra Mística do Wizzle"] = True
            print("Item obtido: Pedra Mística do Wizzle\n")
        
        if isinstance(defensor, malikard):
            if self.itens["Cristais de Malikard"] == False:
                print(f"Ao derrotar Malikard você encontra a primeira parte da herança dos Satoro. Um conjunto de belos e resistentes cristais agora estão em suas mãos.")

            self.itens["Cristais de Malikard"] = True
            print("Item obtido: Cristais de Malikard\n")

        if isinstance(defensor, kiravin):
            if self.itens["Cristais de Kiravin"] == False:
                print(f"Ao derrotar Kiravin você pega a segunda parte da herança dos Satoro, um conjunto mais brilhante de cristais, duros como diamante.")

            self.itens["Cristais de Kiravin"] = True
            print("Item obtido: Cristais de Kiravin\n")

        if isinstance(defensor, malikard):
            if self.itens["Tesouro dos Satoro"] == False:
                print(f"Ao derrotar Malikard você encontra a primeira parte da herança dos Satoro. Um conjunto de belos e resistentes cristais agora estão em suas mãos.")

            self.itens["Tesouro dos Satoro"] = True
            print("Item obtido: Tesouro dos Satoro\n")


#-----------------------------------------------------------------------------------------------------------#
     
class monstro(ser_vivo):
    def __init__(self, vida, ataque, tipo, loot):
        super().__init__(vida, ataque)
        self.tipo: str = tipo
        self.loot: int = loot

    def saquear(self):
        if self.loot == 1:
            moedas = randint(2, 7)
            
        elif self.loot == 2:    
            moedas = randint(10, 17)
            
        elif self.loot == 3:
            moedas = randint(20, 27)
            
        elif self.loot == 4:
            moedas = randint(30, 37)
            
        elif self.loot == 5:
            moedas = randint(40, 47)

        print(f"Você encontrou {moedas} moedas.")
        return moedas
        
    def experiencia(self):
        if self.loot == 1:
            xp = randint(50, 70)
           
        elif self.loot == 2:    
            xp = randint(80, 100)
            
        elif self.loot == 3:
            xp = randint(100, 150)
            
        elif self.loot == 4:
            xp = randint(170, 250)
            
        elif self.loot == 5:
            xp = randint(300, 400)
            
        print(f"XP adiquirdo: {xp}.")
        return xp

       # if isinstance(self, lobo):
            
        sleep(1)

#-----------------------------------------------------------------------------------------------------------#

class lobo(monstro):
    def __init__(self, vida, ataque, tipo, forca, loot):
        super().__init__(vida, ataque, tipo, loot)
        self.forca: float = forca

#-----------------------------------------------------------------------------------------------------------#

class goblin(monstro):
    def __init__(self, vida, ataque, tipo, inteligencia, loot):
        super().__init__(vida, ataque, tipo, loot)
        self.inteligencia: int = inteligencia

#-----------------------------------------------------------------------------------------------------------#

class esqueleto(monstro):
    def __init__(self, vida, ataque, tipo, agilidade, loot):
        super().__init__(vida, ataque, tipo, loot)
        self.agilidade: int = agilidade

#-----------------------------------------------------------------------------------------------------------#

class demonio(monstro):
    def __init__(self, vida, ataque, tipo, loot):
        super().__init__(vida, ataque, tipo, loot)

#-----------------------------------------------------------------------------------------------------------#

class troll(monstro):
    def __init__(self, vida, ataque, tipo, regeneracao, inteligencia, loot):
        super().__init__(vida, ataque, tipo, loot)
        self.regeneracao: int = regeneracao
        self.inteligencia: int = inteligencia

#-----------------------------------------------------------------------------------------------------------#

class orc(monstro):
    def __init__(self, vida, ataque, tipo, resistencia, loot):
        super().__init__(vida, ataque, tipo, loot)
        self.resistencia: int = resistencia

#-----------------------------------------------------------------------------------------------------------#

class dragao(monstro):
    def __init__(self, vida, ataque, tipo, loot):
        super().__init__(vida, ataque, tipo, loot)

#-----------------------------------------------------------------------------------------------------------#







class boss(monstro):
    def __init__(self, vida, ataque, tipo):
        super().__init__(vida, ataque, tipo)
        
#-----------------------------------------------------------------------------------------------------------#

class vaelin(boss):
    pass

#-----------------------------------------------------------------------------------------------------------#

class wizzle(boss):
    pass

#-----------------------------------------------------------------------------------------------------------#

class malikard(boss):
    pass

#-----------------------------------------------------------------------------------------------------------#

class kiravin(boss):
    pass

#-----------------------------------------------------------------------------------------------------------#
