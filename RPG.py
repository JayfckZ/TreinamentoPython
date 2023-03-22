'''
    Notas sobre essa versão do código:

    A função de ataque por enquanto funciona apenas se o atacante for um Herói, 
    monstros ainda não podem atacar entre si.

    Não há um sistema de regeneração e nem de morte. O que ocasiona vidas negativas.
    Exceto para monstros, que é dito sim quando morrem.

'''

from random import randint

class ser_vivo:
    def __init__(self, vida, ataque):
        self.vida: int = vida
        self.ataque: int = ataque

    def atacar(self, atacante, defensor):
        defensor.vida -= atacante.ataque
        print(f"{atacante.nome} causou {atacante.ataque} de dano.")
        
#       TESTE PARA VER SE O INIMIGO CONTRA-ATACA

        n = randint (0, 100)  
        if n <= 25:
            atacante.vida -= defensor.ataque
            print(f"{defensor.tipo} conseguiu revidar e causou {defensor.ataque} de dano!")
        
        if defensor.vida <= 0:
            print(f"Você derrotou {defensor.tipo} com sucesso!")
            print(f"Sua vida: {atacante.vida}HP")
        else:
            print(f"{atacante.nome}: {atacante.vida}HP\n"
                  f"{defensor.tipo}: {defensor.vida}HP")

class heroi(ser_vivo):
    def __init__(self, vida, ataque, nome):
        super().__init__(vida, ataque)
        self.nome: str = nome

class monstro(ser_vivo):
    def __init__(self, vida, ataque, tipo):
        super().__init__(vida, ataque)
        self.tipo: str = tipo

class lobo(monstro):
    def __init__(self, vida, ataque, tipo, forca):
        super().__init__(vida, ataque, tipo)
        self.forca: float = forca

class goblin(monstro):
    def __init__(self, vida, ataque, tipo, inteligencia):
        super().__init__(vida, ataque, tipo)
        self.inteligencia: int = inteligencia
        

#======================= AREA DE TESTES =======================#

jogador = heroi(vida=150, ataque=45, nome="Jay")

goblin_verde = goblin(vida=75, ataque=15, tipo="Goblin Verde", inteligencia=8)
goblin_azul = goblin(vida=115, ataque=35, tipo="Goblin Azul", inteligencia=9)
goblin_vermelho = goblin(vida=190, ataque=85, tipo="Goblin Vermelho", inteligencia=15)
goblin_roxo = goblin(vida=175, ataque=75, tipo="Goblin Roxo", inteligencia=30)
goblin_possuido = goblin(vida=350, ataque=140, tipo="Goblin Possuído", inteligencia=30)

lobo_floresta = lobo(vida=35, ataque=30, tipo="Lobo das Florestas", forca=1.3)
lobo_montanha = lobo(vida=35, ataque=35, tipo="Lobo das Montanhas", forca=1.7)
lobo_neve = lobo(vida=45, ataque=40, tipo="Lobo das Neves", forca=2.5)
lobo_infernal = lobo(vida=80, ataque=95, tipo="Lobo Infernal", forca=3.0)

jogador.atacar(jogador, goblin_verde)

jogador.atacar(jogador, goblin_verde)
