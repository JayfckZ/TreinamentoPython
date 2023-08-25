from SerVivo import *

def loja(heroi):    # A TERMINAR
    while True:
        print(f"Seu dinheiro: {heroi.moedas}G$")
        cmd = int(input("\n1- Armaduras"
                    "\n2- Espadas"
                    "\n3- Voltar"
                    "\nEscolha: "))
        
        if cmd == 1:
            print("\n-+-+-Armaduras-+-+-")
            cmd = int(input("\n 1- Armadura de Couro - 100G$"
                        "\n 2- Armadura de Couro Reforçada - 250G$ +  10 Couros de Lobo"
                        "\n 3- Armadura de Ferro - 400G$ + 25 Couros de Lobo"
                        "\n 4- Armadura de Aço - 700G$ + 50 Ossos de Esqueleto"
                        "\n 5- Armadura de Prata - 900G$ +  125 Ossos de Esqueleto"
                        "\n 6- Armadura de Ouro - 1.200G$ + Rubi de Vaelin"
                        "\n 7- Armadura de Obsidiana - 2.500G$ + Pedra Mística de Wizzle"
                        "\n 8- Armadura de Cristal- 3.500G$ + Cristais de Malikard"
                        "\n 9- Armadura de Diamante - 4.000 + Cristais de Kiravin"
                        "\n10- Armadura de Platina - 10.000G$ + Tesouro dos Satoro"
                        "\n\n-+-+-Armaduras de Dragões-+-+-"
                        "\n11- Armadura de Dragão - 8.000G$ + 10 Couros de Dragão"
                        "\n12- Armadura de Dragão Branco- 10.000G$ + 1 Couro de Dragão Branco"
                        "\n13- Armadura de Dragão Negro - 15.000G$ + 1 Couro de Dragão Negro"
                        "\n\n14- Voltar"
                        "\nEscolha: "))
            
            if cmd == 1:
                if heroi.moedas >= 100 and AC == False:
                    heroi.moedas -= 100
                    heroi.armadura = 5
                    AC = True
                    print("\nAgora você veste uma Armadura de Couro.")
                    print("Defesa +5")
                elif AC == True:
                    print("Você já comprou esta peça.")
                else:
                    print("Você não possui moedas suficientes para comprar esta peça.")
            
            elif cmd == 2:
                if heroi.moedas >= 250 and heroi.itens["Couro de Lobo"] >= 10 and ACR == False:
                    heroi.moedas -= 250
                    heroi.itens["Couro de Lobo"] -= 10
                    heroi.armadura = 10
                    ACR = True
                    print("\nAgora você veste uma Armadura de Couro Reforçada.")
                    print("Defesa +10")
                elif heroi.itens["Couro de Lobo"] < 10:
                    print("Você não tem os materiais necessários para fabricar esta peça.")
                elif ACR == True:
                    print("Você já comprou esta peça.")
                else:
                    print("Você não possui moedas suficientes para comprar esta peça.")

            elif cmd == 3:
                if heroi.moedas >= 450 and heroi.itens["Couro de Lobo"] >= 25 and AF == False:
                    heroi.moedas -= 400
                    heroi.itens["Couro de Lobo"] -= 25
                    heroi.armadura = 15
                    AF = True
                    print("\nAgora você veste uma Armadura de Ferro.")
                    print("Defesa +15")
                elif heroi.itens["Couro de Lobo"] < 25:
                    print("Você não tem os materiais necessários para fabricar esta peça.")
                elif AF == True:
                    print("Você já comprou esta peça.")
                else:
                    print("Você não possui moedas suficientes para comprar esta peça.")

            elif cmd == 4:
                if heroi.moedas >= 700 and heroi.itens["Ossos de Esqueletos"] >= 50 and AA == False:
                    heroi.moedas -= 700
                    heroi.itens["Ossos de Esqueletos"] -= 50
                    heroi.armadura = 20
                    AA = True
                    print("\nAgora você veste uma Armadura de Aço.")
                    print("Defesa +20")
                elif heroi.itens["Ossos de Esqueletos"] < 50:
                    print("Você não tem os materiais necessários para fabricar esta peça.")
                elif AA == True:
                    print("Você já comprou esta peça.")
                else:
                    print("Você não possui moedas suficientes para comprar esta peça.")            

            elif cmd == 5:
                if heroi.moedas >= 900 and heroi.itens["Ossos de Esqueletos"] >= 125 and AP == False:
                    heroi.moedas -= 900
                    heroi.itens["Ossos de Esqueletos"] -= 125
                    heroi.armadura = 25
                    AP = True
                    print("\nAgora você veste uma Armadura de Prata.")
                    print("Defesa +25")
                elif heroi.itens["Ossos de Esqueleto"] < 125:
                    print("Você não tem os materiais necessários para fabricar esta peça.")
                elif AP == True:
                    print("Você já comprou esta peça.")
                else:
                    print("Você não possui moedas suficientes para comprar esta peça.")

            elif cmd == 6:
                if heroi.moedas >= 1200 and heroi.itens["Rubi de Vaelin"] == True and AO == False:
                    heroi.moedas -= 1200
                    heroi.armadura = 30
                    AO = True
                    print("\nAgora você veste uma Armadura de Ouro.")
                    print("Defesa +30")
                elif heroi.itens["Rubi de Vaelin"] != False:
                    print("Você não tem os materiais necessários para fabricar esta peça.")
                elif AO == True:
                    print("Você já comprou esta peça.")
                else:
                    print("Você não possui moedas suficientes para comprar esta peça.")


            sleep(1.5)
        
        elif cmd == 3:
            break


def classes(heroi):
    g1 = g2 = ma1 = ma2 = c1 = c2 = False
    while True:
        print(f"\nNível de Classe Primária: {heroi.nvl1}"
              f"\nNível de Classe Secundária: {heroi.nvl2}"
              f"\nPontos de Experiência: {heroi.xp}\n")
        
        if heroi.classes[0] == "Guerreiro":
            print("1- Guerreiro (Primária)")
            g1 = True
        elif heroi.classes[1] == "Guerreiro":
            print("1- Guerreiro (Secundária)") 
            g2 = True
        else:
            print("1- Guerreiro: Seja treinado nas artes de combate.")

        if heroi.classes[0] == "Mago":
            print("2- Mago (Primária)")
            ma1 = True
        elif heroi.classes[1] == "Mago":
            print("2- Mago (Secundária)")
            ma2 = True 
        else:
            print("2- Mago: Se torne um poderoso mago na luta contra o mal.")

        if heroi.classes[0] == "Cacador":
            print("3- Caçador (Primária)")
            c1 = True
        elif heroi.classes[1] == "Cacador":
            print("3- Caçador (Secundária)") 
            c2 = True
        else:
            print("3- Caçador: Mostre suas habilidades como um verdadeiro caçador.")

 #       if heroi.classes[0] == "Mercador":
 #           print("4- Mercador (Primária)")
 #           me1 = True
 #       elif heroi.classes[1] == "Mercador":
 #           print("4- Mercador (Secundária)")
 #           me2 = True 
 #       else:
 #           print("4- Mercador: Sabe bem como conduzir um grande negócio.")
        
        print("4- Voltar")

        cmd = int(input("Escolha: "))

        if cmd == 1:
            if heroi.classes[0] == "":
                cmd = int(input("\nDeseja atribuir Guerreiro para sua classe primária?"
                            "\n1- Sim"
                            "\n2- Não"
                            "\nEscolha: "))
                if cmd == 1:
                    heroi.classes[0] = "Guerreiro"
                elif cmd == 2:
                    pass
                else:
                    print("Opção inválida")
                    sleep(1)
            
            elif heroi.classes[1] == "" and heroi.classes[0] != "Guerreiro":
                cmd = int(input("\nDeseja atribuir Guerreiro para sua classe secundária?"
                            "\n1- Sim"
                            "\n2- Não"
                            "\nEscolha: "))
                if cmd == 1:
                    heroi.classes[1] = "Guerreiro"
                elif cmd == 2:
                    pass
                else:
                    print("Opção inválida")
                    sleep(1)

            elif heroi.classes[0] != "Guerreiro" and heroi.classes[1] != "Guerreiro":
                print("\nVocê já possui uma Classe Primária e uma Secundária.")
                sleep(1.5)
                
            else:
                if g1:
                    if heroi.nvl1 == 0 :
                        cmd = int(input("\n1- Melhorar para: Guerreiro Preparado (250XP)\n"
                                    "        Ataque +2 e Vida +2"
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 250:
                            heroi.xp -= 250
                            heroi.nvl1 += 1
                            heroi.ataque += 2
                            heroi.vidamax += 2
                            heroi.vida += 2
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl1 == 1 :
                        cmd = int(input("\n1- Melhorar para: Guerreiro Fortificado (1.250XP)\n"
                                    "        Ataque +4 e Vida +3"
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 1250:
                            heroi.xp -= 1250
                            heroi.nvl1 += 1
                            heroi.ataque += 4
                            heroi.vidamax += 3
                            heroi.vida += 3
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl1 == 2:
                        cmd = int(input("\n1- Melhorar para: Guerreiro da Vanguarda (2.500XP)\n"
                                    "        Ataque +5 e Vida +5"
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 2500:
                            heroi.xp -= 2500
                            heroi.nvl1 += 1
                            heroi.ataque += 5
                            heroi.vidamax += 5
                            heroi.vida += 5
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl1 == 3:
                        cmd = int(input("\n1- Melhorar para: Guerreiro do Alto Escalão (5.000XP)\n"
                                    "        Ataque +10 e Vida +10"
                                    "\n Escudo Nobre: Chance de 20% de esquivar de uma investida inimiga."
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 5000:
                            heroi.xp -= 5000
                            heroi.nvl1 += 1
                            heroi.ataque += 10
                            heroi.vidamax += 10
                            heroi.vida += 10
                            heroi.hg4 = True
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl1 ==  4:
                        cmd = int(input("\n1- Melhorar para: Líder do Exército (8.500XP)\n"
                                    "        Ataque +15 e Vida +25"
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 8500:
                            heroi.xp -= 8500
                            heroi.nvl1 += 1
                            heroi.ataque += 15
                            heroi.vidamax += 25
                            heroi.vida += 25
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl1 == 5:
                        cmd = int(input("\n1- Melhorar para: Herói (12.750XP)\n"
                                    "        Ataque +25 e Vida +30 | Habilidade Especial:"
                                    "\n Golpe Sangrento: Chance de 10% de, ao esquivar de uma investida inimiga, causar imenso dano."
                                    "\n Escudo Nobre: Aumento de chance para 35%."
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 12750:
                            heroi.xp -= 12750
                            heroi.nvl1 += 1
                            heroi.ataque += 25
                            heroi.vidamax += 30
                            heroi.vida += 30
                            heroi.hg6 = True
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl1 == 6:
                        print("\nNível máximo atingido.")
                        sleep(1.5)

                elif g2:
                    if heroi.nvl2 == 0 :
                        cmd = int(input("\n1- Melhorar para: Guerreiro Preparado (250XP)\n"
                                    "        Ataque +2 e Vida +2"
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 250:
                            heroi.xp -= 250
                            heroi.nvl2 += 1
                            heroi.ataque += 2
                            heroi.vidamax += 2
                            heroi.vida += 2
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl2 == 1 :
                        cmd = int(input("\n1- Melhorar para: Guerreiro Fortificado (1250XP)\n"
                                    "        Ataque +4 e Vida +3"
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 1250:
                            heroi.xp -= 1250
                            heroi.nvl2 += 1
                            heroi.ataque += 4
                            heroi.vidamax += 3
                            heroi.vida += 3
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl2 == 2:
                        print("\nNível máximo atingido.")
                        sleep(1.5)

        elif cmd == 2:
            if heroi.classes[0] == "":
                cmd = int(input("\nDeseja atribuir Mago para sua classe primária?"
                            "\n1- Sim"
                            "\n2- Não"
                            "\nEscolha: "))
                if cmd == 1:
                    heroi.classes[0] = "Mago"
                elif cmd == 2:
                    pass
                else:
                    print("Opção inválida")
                    sleep(1)
            
            elif heroi.classes[1] == "" and heroi.classes[0] != "Mago":
                cmd = int(input("\nDeseja atribuir Mago para sua classe secundária?"
                            "\n1- Sim"
                            "\n2- Não"
                            "\nEscolha: "))
                if cmd == 1:
                    heroi.classes[1] = "Mago"
                elif cmd == 2:
                    pass
                else:
                    print("Opção inválida")
                    sleep(1)

            elif heroi.classes[0] != "Mago" and heroi.classes[1] != "Mago":
                print("\nVocê já possui uma Classe Primária e uma Secundária.")
                sleep(1.5)
                
            else:
                if ma1:
                    if heroi.nvl1 == 0 :
                        cmd = int(input("\n1- Melhorar para: Aprendiz (250XP)\n"
                                    "        Ataque +2 e Vida +5"
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 250:
                            heroi.xp -= 250
                            heroi.nvl1 += 1
                            heroi.ataque += 2
                            heroi.vidamax += 5
                            heroi.vida += 5
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl1 == 1 :
                        cmd = int(input("\n1- Melhorar para: Magia Básica (1.100XP)\n"
                                    "        Ataque +5 e Vida +5"
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 1100:
                            heroi.xp -= 1100
                            heroi.nvl1 += 1
                            heroi.ataque += 5
                            heroi.vidamax += 5
                            heroi.vida += 5
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl1 == 2:
                        cmd = int(input("\n1- Melhorar para: Curandeiro (2.250XP)\n"
                                    "        Ataque +5 e Vida +15"
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 2250:
                            heroi.xp -= 2250
                            heroi.nvl1 += 1
                            heroi.ataque += 5
                            heroi.vidamax += 15
                            heroi.vida += 15
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl1 == 3:
                        cmd = int(input("\n1- Melhorar para: Alquimista (5.800XP)\n"
                                    "        Ataque +5 e Vida +15"
                                    "\n Alquimia Avançada: Prepara 9 poções para as batalhas ao invés de 6."
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 5800:
                            heroi.xp -= 5800
                            heroi.nvl1 += 1
                            heroi.ataque += 5
                            heroi.vidamax += 10
                            heroi.vida += 10
                            heroi.hma4 = True
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl1 ==  4:
                        cmd = int(input("\n1- Melhorar para: Magia Vital (10.500XP)\n"
                                    "        Ataque +10 e Vida +45"
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 10500:
                            heroi.xp -= 10500
                            heroi.nvl1 += 1
                            heroi.ataque += 15
                            heroi.vidamax += 45
                            heroi.vida += 45
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl1 == 5:
                        cmd = int(input("\n1- Melhorar para: Mago Renascido (30.666XP)\n"
                                    "        Ataque +30 e Vida +100 | Habilidade Especial:"
                                    "\n Checkpoint: O Mago possui mais uma vida para acabar com o mal."
                                    "\n Alquimia Avançada: Aumenta o número de poções para 12, e maior chance de Poção Melhorada e Abençoada."
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 30666:
                            heroi.xp -= 30666
                            heroi.nvl1 += 1
                            heroi.ataque += 30
                            heroi.vidamax += 100
                            heroi.vida += 100
                            heroi.hma6 = True
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl1 == 6:
                        print("\nNível máximo atingido.")
                        sleep(1.5)

                elif ma2:
                    if heroi.nvl2 == 0 :
                        cmd = int(input("\n1- Melhorar para: Aprendiz (250XP)\n"
                                    "        Ataque +2 e Vida +5"
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 250:
                            heroi.xp -= 250
                            heroi.nvl2 += 1
                            heroi.ataque += 2
                            heroi.vidamax += 5
                            heroi.vida += 5
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl2 == 1 :
                        cmd = int(input("\n1- Melhorar para: Magia Básica (1100XP)\n"
                                    "        Ataque +5 e Vida +5"
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 1100:
                            heroi.xp -= 1100
                            heroi.nvl2 += 1
                            heroi.ataque += 5
                            heroi.vidamax += 5
                            heroi.vida += 5
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl2 == 2:
                        print("\nNível máximo atingido.")
                        sleep(1.5)    

        elif cmd == 3:
            if heroi.classes[0] == "":
                cmd = int(input("\nDeseja atribuir Caçador para sua classe primária?"
                            "\n1- Sim"
                            "\n2- Não"
                            "\nEscolha: "))
                if cmd == 1:
                    heroi.classes[0] = "Cacador"
                elif cmd == 2:
                    pass
                else:
                    print("Opção inválida")
                    sleep(1)
            
            elif heroi.classes[1] == "" and heroi.classes[0] != "Cacador":
                cmd = int(input("\nDeseja atribuir Caçador para sua classe secundária?"
                            "\n1- Sim"
                            "\n2- Não"
                            "\nEscolha: "))
                if cmd == 1:
                    heroi.classes[1] = "Cacador"
                elif cmd == 2:
                    pass
                else:
                    print("Opção inválida")
                    sleep(1)

            elif heroi.classes[0] != "Cacador" and heroi.classes[1] != "Cacador":
                print("\nVocê já possui uma Classe Primária e uma Secundária.")
                sleep(1.5)
                
            else:
                if c1:
                    if heroi.nvl1 == 0 :
                        cmd = int(input("\n1- Melhorar para: Iniciante (250XP)\n"
                                    "        Ataque +5 e Vida +2"
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 250:
                            heroi.xp -= 250
                            heroi.nvl1 += 1
                            heroi.ataque += 5
                            heroi.vidamax += 2
                            heroi.vida += 2
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl1 == 1 :
                        cmd = int(input("\n1- Melhorar para: Sobrevivente (1.000XP)\n"
                                    "        Ataque +8 e Vida +3"
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 1000:
                            heroi.xp -= 1000
                            heroi.nvl1 += 1
                            heroi.ataque += 8
                            heroi.vidamax += 3
                            heroi.vida += 3
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl1 == 2:
                        cmd = int(input("\n1- Melhorar para: Experiente (2.900XP)\n"
                                    "        Ataque +10 e Vida +3"
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 2900:
                            heroi.xp -= 2900
                            heroi.nvl1 += 1
                            heroi.ataque += 10
                            heroi.vidamax += 3
                            heroi.vida += 3
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl1 == 3:
                        cmd = int(input("\n1- Melhorar para: Caçador da Selva (7.000XP)\n"
                                    "        Ataque +25 e Vida +10"
                                    "\n Faca de Caça: 75% de chance de pegar o dobro de loot de inimigos mortos."
                                    "\n  15% de chance de pegar o triplo de loot de inimigos mortos."
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 7000:
                            heroi.xp -= 7000
                            heroi.nvl1 += 1
                            heroi.ataque += 25
                            heroi.vidamax += 10
                            heroi.vida += 10
                            heroi.hc4 = True
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl1 ==  4:
                        cmd = int(input("\n1- Melhorar para: Caçador Inóspito (7.650XP)\n"
                                    "        Ataque +35 e Vida +15"
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 7650:
                            heroi.xp -= 7650
                            heroi.nvl1 += 1
                            heroi.ataque += 35
                            heroi.vidamax += 15
                            heroi.vida += 15
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl1 == 5:
                        cmd = int(input("\n1- Melhorar para: Lenda Caçadora (15.800XP)\n"
                                    "        Ataque +55 e Vida +30"
                                    "\n Indomável: Chance de 60% de esquivar de uma investida inimiga."
                                    "\n Faca de Caça: Aumento de chance para 40% para dobro, 40% para triplo e 20% para quadruplo."
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 15800:
                            heroi.xp -= 15800
                            heroi.nvl1 += 1
                            heroi.ataque += 55
                            heroi.vidamax += 30
                            heroi.vida += 30
                            heroi.hc6 = True
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl1 == 6:
                        print("\nNível máximo atingido.")
                        sleep(1.5)

                elif c2:
                    if heroi.nvl2 == 0 :
                        cmd = int(input("\n1- Melhorar para: Iniciante (250XP)\n"
                                    "        Ataque +5 e Vida +2"
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 250:
                            heroi.xp -= 250
                            heroi.nvl2 += 1
                            heroi.ataque += 5
                            heroi.vidamax += 2
                            heroi.vida += 2
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl2 == 1 :
                        cmd = int(input("\n1- Melhorar para: Sobrevivente (1000XP)\n"
                                    "        Ataque +8 e Vida +3"
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 1000:
                            heroi.xp -= 1000
                            heroi.nvl2 += 1
                            heroi.ataque += 8
                            heroi.vidamax += 3
                            heroi.vida += 3
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl2 == 2:
                        print("\nNível máximo atingido.")
                        sleep(1.5)

        elif cmd == 4:
            break

        """if cmd == 4:
            if heroi.classes[0] == "":
                cmd = int(input("\nDeseja atribuir Mercador para sua classe primária?"
                            "\n1- Sim"
                            "\n2- Não"
                            "\nEscolha: "))
                if cmd == 1:
                    heroi.classes[0] = "Mercador"
                elif cmd == 2:
                    pass
                else:
                    print("Opção inválida")
                    sleep(1)
            
            elif heroi.classes[1] == "" and heroi.classes[0] != "Mercador":
                cmd = int(input("\nDeseja atribuir Mercador para sua classe secundária?"
                            "\n1- Sim"
                            "\n2- Não"
                            "\nEscolha: "))
                if cmd == 1:
                    heroi.classes[1] = "Mercador"
                elif cmd == 2:
                    pass
                else:
                    print("Opção inválida")
                    sleep(1)

            elif heroi.classes[0] != "Mercador" and heroi.classes[1] != "Mercador":
                print("\nVocê já possui uma Classe Primária e uma Secundária.")
                sleep(1.5)
                
            else:
                if me1:
                    if heroi.nvl1 == 0 :
                        cmd = int(input("\n1- Melhorar para: Novato (250XP)\n"
                                    "    Moedas Insta +1000 e Bônus de Moedas +25"
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 250:
                            heroi.xp -= 250
                            heroi.nvl1 += 1
                            heroi.moedas += 1000
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl1 == 1 :
                        cmd = int(input("\n1- Melhorar para: Medíocre (1.000XP)\n"
                                    "        Moedas Insta + 1500 e Bônus de Moedas +75"
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 1000:
                            heroi.xp -= 1000
                            heroi.nvl1 += 1
                            heroi.moedas += 1500
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl1 == 2:
                        cmd = int(input("\n1- Melhorar para: Profissional (2.500XP)\n"
                                    "        Moedas Insta + 2500 e Bônus de Moedas +120"
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 2500:
                            heroi.xp -= 2500
                            heroi.nvl1 += 1
                            heroi.moedas += 2500
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl1 == 3:
                        cmd = int(input("\n1- Melhorar para: Mercador Regional (5.000XP)\n"
                                    "        Moedas Insta + 3500 e Bônus de Moedas +200"
                                    "\n Táticas Mercantes: Garante 25% de desconto em toda a loja."
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 5000:
                            heroi.xp -= 5000
                            heroi.nvl1 += 1
                            heroi.moedas += 3500
                            heroi.hg4 = True
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl1 ==  4:
                        cmd = int(input("\n1- Melhorar para: Barganhador (10.500XP)\n"
                                    "        Moedas Insta + 5900 e Bônus de Moedas +350"
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 10500:
                            heroi.xp -= 10500
                            heroi.nvl1 += 1
                            heroi.moedas += 5900
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl1 == 5:
                        cmd = int(input("\n1- Melhorar para: Líder dos Negócios (15.750XP)\n"
                                    "        Moedas Insta + 10000 e Bônus de Moedas +500"
                                    "\n Táticas Mercantes: Garante 50% de desconto em toda a loja."
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 15750:
                            heroi.xp -= 15750
                            heroi.nvl1 += 1
                            heroi.moedas += 10000
                            heroi.hg6 = True
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl1 == 6:
                        print("\nNível máximo atingido.")
                        sleep(1.5)

                elif me2:
                    if heroi.nvl2 == 0 :
                        cmd = int(input("\n1- Melhorar para: Novato (250XP)\n"
                                    "    Moedas Insta +1000 e Bônus de Moedas +25"
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 250:
                            heroi.xp -= 250
                            heroi.nvl2 += 1
                            heroi.moedas += 1000
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl2 == 1 :
                        cmd = int(input("\n1- Melhorar para: Medíocre (1.000XP)\n"
                                    "        Moedas Insta + 1500 e Bônus de Moedas +75"
                                    "\n2- Voltar"
                                    "\nEscolha: "))
                        if cmd == 1 and heroi.xp >= 1000:
                            heroi.xp -= 1000
                            heroi.nvl2 += 1
                            heroi.moedas += 1500
                        elif cmd == 1:
                            print("\nXP insuficiente!\n")
                            sleep(1.5)

                    if heroi.nvl2 == 2:
                        print("\nNível máximo atingido.")
                        sleep(1.5)"""

        
