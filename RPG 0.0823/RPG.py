from SerVivo import *
from Funcoes import *

from time import sleep
from copy import copy
from sys import exit
        
def fazpocoes():
    if jogador.hma4 == True:
        if jogador.hma6 == True:
            pocoes = 12
        else:
            pocoes = 9
    else:
        pocoes = 6

    return pocoes

#======================= AREA DE TESTES =======================#

jogador = heroi(vida=150, vidamax=300, ataque=45, nome="Jay")

goblin_verde = goblin(vida=75, ataque=15, tipo="Goblin Verde", inteligencia=10, loot=1)
goblin_azul = goblin(vida=115, ataque=35, tipo="Goblin Azul", inteligencia=25, loot=2)
goblin_vermelho = goblin(vida=190, ataque=85, tipo="Goblin Vermelho", inteligencia=35, loot=3)
goblin_roxo = goblin(vida=175, ataque=75, tipo="Goblin Roxo", inteligencia=50, loot=4)
goblin_possuido = goblin(vida=350, ataque=140, tipo="Goblin Possuído", inteligencia=75, loot=5)

lobo_floresta = lobo(vida=55, ataque=30, tipo="Lobo das Florestas", forca=1.3, loot=1)
lobo_montanha = lobo(vida=55, ataque=35, tipo="Lobo das Montanhas", forca=1.7, loot=1)
lobo_neve = lobo(vida=65, ataque=40, tipo="Lobo das Neves", forca=2.1, loot=3)
lobo_infernal = lobo(vida=110, ataque=95, tipo="Lobo Infernal", forca=2.5, loot=4)

esqueleto_espada = esqueleto(vida=60, ataque=45, tipo="Esqueleto", agilidade=1, loot=2)
esqueleto_arqueiro = esqueleto(vida=60, ataque=60, tipo="Esqueleto Arqueiro", agilidade=4, loot=3)
esqueleto_machado = esqueleto(vida=100, ataque=95, tipo="Esqueleto Lenhador", agilidade=2, loot=4)
esqueleto_morte = esqueleto(vida=125, ataque=105, tipo="Esqueleto Ceifador", agilidade=5, loot=5)

troll_floresta = troll(vida=1000, ataque=60, tipo="Troll da Floresta", regeneracao=150, inteligencia=10, loot=101)
troll_montanha = troll(vida=1150, ataque=85, tipo="Troll da Montanha", regeneracao=150, inteligencia=10, loot=102)
troll_neve = troll(vida=1500, ataque=100, tipo="Troll das Neves", regeneracao=300, inteligencia=35, loot=103)
troll_pantano = troll(vida=2500, ataque=133, tipo="Troll do Pântano", regeneracao=750, inteligencia=25, loot=104)
troll_guardiao = troll(vida=2500, ataque=130, tipo="Troll Guardião", regeneracao=200, inteligencia=35, loot=105)







goblins = [goblin_verde, goblin_azul, goblin_vermelho, goblin_roxo, goblin_possuido]
lobos = [lobo_floresta, lobo_montanha, lobo_neve, lobo_infernal]
esqueletos = [esqueleto_espada, esqueleto_arqueiro, esqueleto_machado, esqueleto_morte]
trolls = [troll_floresta, troll_montanha, troll_neve, troll_pantano, troll_guardiao]
orcs = []
demonios = []
dragoes = []



#goblin_possuido.atacar(goblin_azul)
jogador.xp = 1000000
while jogador.vida >= 0:
    cmd = int(input("\n------------------------"
                    "\n1- Atacar Vila de Goblins"
                    "\n2- Caçar Lobos"
                    "\n3- Atacar Masmorra dos Esqueletos"
                    "\n4- Caçar Trolls"
                    "\n8- Loja (NÃO DISPONÍVEL)"
                    "\n9- Classes"
                    "\n0- Ler Compêndio (INCOMPLETO)"  
                    "\nEscolha uma opção: "))
    print("------------------------\n")

    sleep(1)
    if cmd == 1:
        defensor = copy(goblins[randint(0, len(goblins)-1)])
        print("x"*40)
        print(f"Um inimigo apareceu: {defensor.tipo}.")
        print("x"*40)

        pocoes = fazpocoes()

        while (jogador.vida > 0):
            cmd = jogador.round()    

            sleep(0.5)
            if cmd == 1:    
                jogador.atacar(defensor)
            elif cmd == 2:
                jogador.tomar_pocao(pocoes, defensor)
                pocoes -= 1
            elif cmd == 3:
                print()
                print("x"*72)
                print(f"Ao fugir de {defensor.tipo} você encontra outro inimigo: ", end='')
                defensor = copy(goblins[randint(0, len(goblins)-1)])
                print(f"{defensor.tipo}.")
                print("x"*72)

                pocoes = fazpocoes()

            else:
                break
            
            if defensor.vida <= 0:
                jogador.moedas += defensor.saquear()
                jogador.xp += defensor.experiencia()
                defensor = copy(goblins[randint(0, len(goblins)-1)])
                print(f"\nUm novo inimigo apareceu: {defensor.tipo}.")

                pocoes = fazpocoes()

            if jogador.vida <= 0:
                if jogador.hma6 == True:
                    sleep(2)
                    print("Você morreu...")
                    sleep(1.5)
                    print("Como um verdadeiro mago você retornará ao mundo dos vivos mais uma vez.")
                    jogador.vida = 100
                    jogador.hma6 = False
                    sleep(1.5)  
                else:
                    print("\n\n\n\n\nVOCÊ MORREU!")
                    exit()
                    
    
    elif cmd == 2:
        defensor = copy(lobos[randint(0, len(lobos)-1)])
        print("x"*40)
        print(f"Um inimigo apareceu: {defensor.tipo}.")
        print("x"*40)

        pocoes = fazpocoes()

        while (jogador.vida > 0):
            cmd = jogador.round()    

            sleep(0.5)
            if cmd == 1:    
                jogador.atacar(defensor)
            elif cmd == 2:
                jogador.tomar_pocao(pocoes, defensor)
                pocoes -= 1
            elif cmd == 3:
                print()
                print("x"*72)
                print(f"Ao fugir de {defensor.tipo} você encontra outro inimigo: ", end='')
                defensor = copy(lobos[randint(0, len(lobos)-1)])
                print(f"{defensor.tipo}.")
                print("x"*72)

                pocoes = fazpocoes()
            else:
                break
            
            if defensor.vida <= 0:
                jogador.moedas += defensor.saquear()
                jogador.xp += defensor.experiencia()
                jogador.conquista(defensor)
                defensor = copy(lobos[randint(0, len(lobos)-1)])
                print("x"*40)
                print(f"Um novo inimigo apareceu: {defensor.tipo}.")
                print("x"*40)

                pocoes = fazpocoes()

            if jogador.vida <= 0:
                if jogador.hma6 == True:
                    sleep(2)
                    print("Você morreu...")
                    sleep(1.5)
                    print("Como um verdadeiro mago você retornará ao mundo dos vivos mais uma vez.")
                    jogador.vida = 100
                    jogador.hma6 = False
                    sleep(1.5)  
                else:
                    print("\n\n\n\n\nVOCÊ MORREU!")
                    exit()


    elif cmd == 3:
        defensor = copy(esqueletos[randint(0, len(esqueletos)-1)])
        print("x"*40)
        print(f"Um inimigo apareceu: {defensor.tipo}.")
        print("x"*40)

        pocoes = fazpocoes()

        while (jogador.vida > 0):
            cmd = jogador.round()    

            sleep(0.5)
            if cmd == 1:    
                jogador.atacar(defensor)
            elif cmd == 2:
                jogador.tomar_pocao(pocoes, defensor)
                pocoes -= 1
            elif cmd == 3:
                print()
                print("x"*72)
                print(f"Ao fugir de {defensor.tipo} você encontra outro inimigo: ", end='')
                defensor = copy(esqueletos[randint(0, len(esqueletos)-1)])
                print(f"{defensor.tipo}.")
                print("x"*72)

                pocoes = fazpocoes()

            else:
                break
            
            if defensor.vida <= 0:
                jogador.moedas += defensor.saquear()
                jogador.xp += defensor.experiencia()
                defensor = copy(esqueletos[randint(0, len(esqueletos)-1)])
                print(f"\nUm novo inimigo apareceu: {defensor.tipo}.")

                pocoes = fazpocoes()

            if jogador.vida <= 0:
                if jogador.hma6 == True:
                    sleep(2)
                    print("Você morreu...")
                    sleep(1.5)
                    print("Como um verdadeiro mago você retornará ao mundo dos vivos mais uma vez.")
                    jogador.vida = 100
                    jogador.hma6 = False
                    sleep(1.5)  
                else:
                    print("\n\n\n\n\nVOCÊ MORREU!")
                    exit()


    elif cmd == 4:
        defensor = copy(trolls[randint(0, len(trolls)-1)])
        print("x"*40)
        print(f"Um inimigo apareceu: {defensor.tipo}.")
        print("x"*40)

        pocoes = fazpocoes()

        while (jogador.vida > 0):
            cmd = jogador.round()    

            sleep(0.5)
            if cmd == 1:    
                jogador.atacar(defensor)
            elif cmd == 2:
                jogador.tomar_pocao(pocoes, defensor)
                pocoes -= 1
            elif cmd == 3:
                print()
                print("x"*72)
                print(f"Ao fugir de {defensor.tipo} você encontra outro inimigo: ", end='')
                defensor = copy(trolls[randint(0, len(trolls)-1)])
                print(f"{defensor.tipo}.")
                print("x"*72)

                pocoes = fazpocoes()

            else:
                break
            
            if defensor.vida <= 0:
                jogador.moedas += defensor.saquear()
                jogador.xp += defensor.experiencia()
                defensor = copy(trolls[randint(0, len(trolls)-1)])
                print(f"\nUm novo inimigo apareceu: {defensor.tipo}.")

                pocoes = fazpocoes()

            if jogador.vida <= 0:
                if jogador.hma6 == True:
                    sleep(2)
                    print("Você morreu...")
                    sleep(1.5)
                    print("Como um verdadeiro mago você retornará ao mundo dos vivos mais uma vez.")
                    jogador.vida = 100
                    jogador.hma6 = False
                    sleep(1.5)  
                else:
                    print("\n\n\n\n\nVOCÊ MORREU!")
                    exit()


    elif cmd == 8:
        print()
        if jogador.classes[0] == "Mercador" or jogador.classes[1] == "Mercador":
            print("="*49)
            print(f"{'LOJA':^49}")
            print("="*49)
            loja(jogador)
        else:
            print("A Loja chegará em futuras atualizações!")
            sleep(1.5)
            

    elif cmd == 9:
        print()
        print("="*49)
        print(f"{'TORRE DE CLASSES':^49}")
        print("="*49)
        classes(jogador)
        
    elif cmd == 0:
        print()
        print("="*49)
        print(f"{'COMPÊNDIO':^49}")
        print("="*49)
        print("Dos campos belos de Veryn aos montes gélidos de" 
              "\nPolora, esses monstros aterrorizam o nosso mundo."
              "\nEis aqui o que todo herói necessita: Um guia "
              "\nsobre os monstros que ele encontrará em seu caminho.\n"
              "\n\n--GOBLINS--\n\n"
              "\nGoblins são criaturas que sua mutação varia muito" 
              "\nde sua região. Enquanto Goblins Verdes são encontrados"
              "\npor toda Veryn, Goblin Vermelhos podem ser encontrados "
              "\nnas profundezas do mundo ou como guarda de fortalezas. "
              "\nOs Azuis são mais gélidos, encontrados majoritariamente "
              "\nem Polora. Os roxos possuem menos força que os vermelhos,"
              "\nmas sua inteligência não deve ser subestimada."
              "\n  E por fim, os Possuídos. Não se sabe por quem ou o quê."
              "\nMas estes são verdadeiras máquinas de matar. Se avistar um,"
              "\nfuja ou prepasse para sua morte iminente, neles são impiedosos,"
              "\ne se desafiados, nunca recuarão."
              "\nGoblins têm como atributo pessoal sua INTELIGÊNCIA, oque faz"
              "\ncom que revidem ataques e suas batalhas sejam mais desafiadoras.\n"
              "\n\n-CARACTERÍSTICAS INDIVIDUAIS-\n\n\n"
              "                   HP   DAN   INT\n"
              "Goblin Verde:      75 |  15 |  10\n"
              "Goblin Azul:      115 |  35 |  25\n"
              "goblin Vermelho:  190 |  85 |  35\n"
              "goblin Roxo:      175 |  75 |  50\n"
              "goblin Possuido:  350 | 140 |  75\n\n\n\n"
              "--LOBOS--\n\n"
              "Lobos são criaturas hostis que vivem em diversas áreas. Cada região"
              "\ntem sua própria variação do lobo, então quanto mais frio estiver a região mais"
              "\nresistente e forte eles serão. É possível encontrá-los em florestas, montanhas"
              "\nrochosas e nevadas."
              "\n   Há também o Lobo de Chamas, ou popularmente conhecido como Lobo Infernal."
              "\nEssa espécie ainda tem origem desconhecida, mas a força de sua mordida é incomparável"
              "\ncom os demais. Pode ser encontrado nas profundezas do mundo. Fique longe ou preparesse"
              "\npara um combate árduo.\n"
              "\nLobos têm como atributo pessoal sua FORÇA da mordida, oque faz"
              "\ncom que, quando aplicada, cause muito mais dano.\n"
              "\n\n-CARACTERÍSTICAS INDIVIDUAIS-\n\n\n"
              "                   HP   DAN    FOR\n"
              "Lobo da Floresta:  35 |  30 |  1.3\n"
              "Lobo da Montanha:  35 |  35 |  1.7\n"
              "Lobo das Neves:    45 |  40 |  2.5\n"
              "Lobo Infernal:     80 |  95 |  3.0\n")

        print("="*49)
        input("Aperte ENTER para continuar")