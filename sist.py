from time import sleep
from datetime import datetime
from random import randint, shuffle

cont = 0
contl = 0
arq = "register.txt"
arq2 = "users.txt"


def geraCod():
    letras = 'x'
    numeros = '0102030405060708090'
    cont = 0
    cod = []

    while cont != 15:
        ales = randint(1, 5)
        if ales == 1:
            ale = randint(0, len(letras) - 1)
            cod.append(letras[ale])
            cont += 1
        else:
            ale = randint(0, len(numeros) - 1)
            cod.append(numeros[ale])
            cont += 1

    shuffle(cod)
    return "".join(cod)


def registra(arq, name, op, cod, valor):
    try:
        a = open(arq, 'at')
    except:
        print("Houve um erro interno.")
    else:
        try:
            if str(valor).isnumeric():
                a.write(f"{cod};{op};R${valor:.2f};{name};{datetime.now().replace(microsecond=0)}\n")
            else:
                a.write(f"{cod};{op};{valor};{name};{datetime.now().replace(microsecond=0)}\n")
        except:
            print("Houve um erro ao registrar os dados")
        else:
            a.close()


def registraUser(name, senha, saldo="00.00"):
    try:
        a = open(arq2, "rt")
        conta = sum((1 for linhas in a), 1)
        a = open(arq2, 'at')
    except:
        print("Houve um erro interno.")
    else:
        try:
            a.write(f"{name};{senha};{saldo};{conta}\n")
        except:
            print("Houve um erro ao registrar os dados")
        else:
            a.close()


def semDuplicata(cod):
    try:
        a = open(arq, "rt")
    except:
        print("Houve um erro ao verificar duplicata.")
    else:
        for linha in a:
            dado = linha.split(';')
            if cod == dado[0]:
                return True
            else:
                return False


def atualiza(arq, index, user, senha, saldo):
    a = open(arq, 'r')
    linha = a.readlines()
    a.close()
    a = open(arq, 'w')
    for i in linha:
        if linha.index(i) == index:
            a.write(f"{user};{senha};{saldo};{index}" + '\n')
        else:
            a.write(i)
    a.close()


def programa(name, sen, sal):
    user, senha, saldo = name, sen, float(sal)
    cont = 0
    while True:
        try:
            print("-" * 45)
            print(f"{'TOGURO`s BANK':^45}")
            print("-" * 45)
            op = int(input("Qual operação deseja realizar?\n"
                           "1- Saque\n"
                           "2- Depósito\n"
                           "3- Consulta\n"
                           "4- Histórico\n"
                           "5- Transferência\n"
                           "6- Sair\n"
                           "Sua escolha: "))
        except (ValueError, KeyboardInterrupt):
            print("\n\033[1;31mValor inválido.\033[m\n Reiniciando operação...")
            sleep(2)
        else:
            if op == 1:
                print("-" * 45)
                print(f"{'SAQUE':^45}")
                print("-" * 45)
                valor = float(input("Informe o valor que deseja sacar: "))
                confer = input("Digite a senha: ")
                print("Conferindo dados...")
                sleep(1.5)

                if confer != senha:
                    print("\nTransação não aprovada. Senha incorreta.\n Reiniciando operação...")
                    sleep(2)
                elif valor > saldo:
                    print("\nTransação não aprovada. Saldo insuficiente.\n Reiniciando operação...")
                    sleep(2)
                else:
                    print("Realizando transação...")
                    sleep(2)
                    saldo -= valor
                    cod = geraCod()

                    while True:
                        if semDuplicata(cod):
                            cod = geraCod()
                        else:
                            break

                    print("Saque realizado com sucesso!")
                    registra(arq, user, 'Saque', cod, int(valor))
                    print(f"\033[3;37m  Operação ({cod})\033[m")
                    cmd = input("\nDeseja realizar outra operação? [S/N] ").upper()[0]

                    while cmd not in "SN":
                        cmd = input("Comando inválido. Deseja realizar outra operação? [S/N] ").upper()[0]
                    if cmd == 'N':
                        break
                    else:
                        print("\n Reiniciando operação...")
                        sleep(2)

            elif op == 2:
                print("-" * 45)
                print(f"{'DEPÓSITO':^45}")
                print("-" * 45)
                valor = float(input("Informe o valor que deseja depositar: "))
                confer = input("Digite a senha: ")
                print("Conferindo dados...")
                sleep(1.5)

                if confer != senha:
                    print("\nTransação não aprovada. Senha incorreta.\n Reiniciando operação...")
                    sleep(2)
                else:
                    print("Realizando depósito...")
                    sleep(2)
                    saldo += valor
                    cod = geraCod()

                    while True:
                        if semDuplicata(cod):
                            cod = geraCod()
                        else:
                            break

                    print("Depósito realizado com sucesso!")
                    registra(arq, user, 'Depósito', cod, int(valor))
                    print(f"\033[3;37m  Operação ({cod})\033[m")
                    cmd = input("\nDeseja realizar outra operação? [S/N] ").upper()[0]

                    while cmd not in "SN":
                        cmd = input("Comando inválido. Deseja realizar outra operação? [S/N] ").upper()[0]
                    if cmd == 'N':
                        break
                    else:
                        print("\n Reiniciando operação...")
                        sleep(2)

            elif op == 3:
                print("-" * 45)
                print(f"{'SALDO':^45}")
                print("-" * 45)
                print(f"\nSeu saldo é de \033[1mR${saldo:.2f}\033[m")
                cod = geraCod()

                while True:
                    if semDuplicata(cod):
                        cod = geraCod()
                    else:
                        break

                registra(arq, user, 'Consulta', cod, 'Sem valor')
                print(f"\033[3;37m  Operação ({cod})\033[m")

                cmd = input("\nDeseja realizar outra operação? [S/N] ").upper()[0]
                while cmd not in "SN":
                    cmd = input("Comando inválido. Deseja realizar outra operação? [S/N] ").upper()[0]
                if cmd == 'N':
                    break
                else:
                    print("\n Reiniciando operação...")
                    sleep(2)

            elif op == 4:
                try:
                    a = open(arq, "rt")
                    a.close()
                except:
                    print("Não foi possível abrir o histórico.")
                else:
                    while True:
                        try:
                            a = open(arq, "rt")
                            print("-" * 45)
                            print(f"{'HISTÓRICO':^45}")
                            print("-" * 45)
                            op = int(input("Qual busca deseja realizar?\n"
                                           "1- Geral\n"
                                           "2- Depósito\n"
                                           "3- Saques\n"
                                           "4- Consultas\n"
                                           "5- Transferências\n"
                                           "6- Busca por Código\n"
                                           "7- Voltar\n"
                                           "Sua escolha: "))

                        except (ValueError, KeyboardInterrupt):
                            print("\n\033[1;31mValor inválido.\033[m\n Reiniciando operação...")
                            sleep(2)
                        else:
                            if op == 1:
                                print("-" * 45)
                                for linha in a:
                                    dado = linha.split(";")
                                    dado[len(dado) - 1] = dado[len(dado) - 1].replace("\n", "")
                                    if user in dado[3]:
                                        print(
                                            f"Código: {dado[0]} | Operação: {dado[1]} | Valor: {dado[2]} | Usuário: {dado[3]} | Data: {dado[4]}")
                                        cont += 1
                                if cont == 0:
                                    print("Não há dados no histórico.")
                                cont = 0
                                input("Clique [ENTER] para continuar.")

                            elif op == 2:
                                print("-" * 45)
                                for linha in a:
                                    dado = linha.split(";")
                                    dado[len(dado) - 1] = dado[len(dado) - 1].replace("\n", "")
                                    if dado[1] == "Depósito" and dado[3] == user:
                                        print(
                                            f"Código: {dado[0]} | Operação: {dado[1]} | Valor: {dado[2]} | Usuário: {dado[3]} | Data: {dado[4]}")
                                        cont += 1
                                if cont == 0:
                                    print("Não há dados de depósito no histórico.")
                                cont = 0
                                input("Clique [ENTER] para continuar.")

                            elif op == 3:
                                print("-" * 45)
                                for linha in a:
                                    dado = linha.split(";")
                                    dado[len(dado) - 1] = dado[len(dado) - 1].replace("\n", "")
                                    if dado[1] == "Saque" and dado[3] == user:
                                        print(
                                            f"Código: {dado[0]} | Operação: {dado[1]} | Valor: {dado[2]} | Usuário: {dado[3]} | Data: {dado[4]}")
                                        cont += 1
                                if cont == 0:
                                    print("Não há dados de saque no histórico.")
                                cont = 0
                                input("Clique [ENTER] para continuar.")

                            elif op == 4:
                                print("-" * 45)
                                for linha in a:
                                    dado = linha.split(";")
                                    dado[len(dado) - 1] = dado[len(dado) - 1].replace("\n", "")
                                    if dado[1] == "Consulta" and dado[3] == user:
                                        print(
                                            f"Código: {dado[0]} | Operação: {dado[1]} | Valor: {dado[2]} | Usuário: {dado[3]} | Data: {dado[4]}")
                                        cont += 1
                                if cont == 0:
                                    print("Não há dados de consulta no histórico.")
                                cont = 0
                                input("Clique [ENTER] para continuar.")

                            elif op == 5:
                                print("-" * 45)
                                for linha in a:
                                    dado = linha.split(";")
                                    dado[len(dado) - 1] = dado[len(dado) - 1].replace("\n", "")
                                    if dado[1] == "Transferência" and user in dado[3]:
                                        print(
                                            f"Código: {dado[0]} | Operação: {dado[1]} | Valor: {dado[2]} | {dado[3]} | Data: {dado[4]}")
                                        cont += 1
                                if cont == 0:
                                    print("Não há dados de consulta no histórico.")
                                cont = 0
                                input("Clique [ENTER] para continuar.")

                            elif op == 6:
                                print("-" * 45)
                                cod = input("Digite o código de protocolo para busca: ")
                                for linha in a:
                                    dado = linha.split(";")
                                    dado[len(dado) - 1] = dado[len(dado) - 1].replace("\n", "")
                                    if cod == dado[0] and dado[3] == user:
                                        print(
                                            f"Código: {dado[0]} | Operação: {dado[1]} | Valor: {dado[2]} | Usuário: {dado[3]} | Data: {dado[4]}")
                                        cont += 1
                                if cont == 0:
                                    print("Não há dados com este código no histórico.")
                                cont = 0
                                input("Clique [ENTER] para continuar.")

                            elif op == 7:
                                print("Retornando...")
                                sleep(0.5)
                                a.close()
                                break

                            else:
                                print("\n\033[1;31mValor inválido.\033[m\n Reiniciando operação.")
                                sleep(2)

            elif op == 5:
                print("-" * 45)
                print(f"{'TRANSFERÊNCIA':^45}")
                print("-" * 45)
                print(f"Seu saldo: R${saldo:.2f}")
                receb = input("Digite o número da conta que deseja transferir: ")

                try:
                    a = open(arq2, "rt")
                except:
                    print("Houve um erro interno.")

                else:
                    for linha in a:
                        dado = linha.split(";")
                        dado[len(dado) - 1] = dado[len(dado) - 1].replace("\n", "")
                        if dado[3] == receb:
                            cont += 1
                            break
                    if cont == 0:
                        print("Não há usuários com esse código.")
                        sleep(1)
                    else:
                        trans = float(input("Informe o valor que deseja transferir: "))
                        senhaconf = input("Digite sua senha: ")
                        if senha != senhaconf:
                            print("Senha incorreta!\n Retornando para o menu...")
                        elif trans > saldo:
                            print("Saldo insuficiente.\n Retornando para o menu...")
                        sleep(1)
                        break

                        try:
                            a = open(arq2, "rt")
                        except:
                            print("Houve um erro interno.")

                        else:
                            for linha in a:
                                dado = linha.split(";")
                                dado[len(dado) - 1] = dado[len(dado) - 1].replace("\n", "")
                                if dado[3] == receb:
                                    print("Transferindo...")
                                    sleep(2)
                                    saldo -= trans
                                    saldotemp = float(dado[2])
                                    saldotemp += trans
                                    cod = geraCod()

                                    while True:
                                        if semDuplicata(cod):
                                            cod = geraCod()
                                        else:
                                            break

                                    atualiza(arq2, int(dado[3]), dado[0], dado[1], saldotemp)
                                    registra(arq, f"Transferência de {user} para {dado[0]}", "Transferência", cod, trans)
                                    print("Transferência realizada!")
                                    cont += 1
                                    break
                            if cont == 0:
                                print("Não há usuários com esse código.")
                                sleep(1)


            elif op == 6:
                break

            else:
                print("\n\033[1;31mValor inválido.\033[m\n Reiniciando operação.")
                sleep(2)
    return saldo


while True:
    print("-" * 45)
    print(f"{'TOGURO`s BANK':^45}")
    print("-" * 45)
    op = int(input("Qual operação deseja realizar?\n"
                   "1- Entrar\n"
                   "2- Cadastrar\n"
                   "3- Sair\n"
                   "Sua escolha: "))

    if op == 1:
        print("-" * 45)
        print(f"{'LOGIN':^45}")
        print("-" * 45)
        user = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")

        try:
            a = open(arq2, "rt")
        except:
            print("Houve um problema com o sistema.")
        else:
            for linha in a:
                dado = linha.split(";")
                dado[len(dado) - 1] = dado[len(dado) - 1].replace("\n", "")
                if user == dado[0] and senha == dado[1]:
                    print("Acesso concedido!")
                    sleep(0.5)
                    a.close()
                    saldo = programa(dado[0], dado[1], dado[2])
                    cont += 1
                    atualiza(arq2, contl, user, senha, saldo)
                    break
                contl += 1
            contl = 0

            if cont == 0:
                print("As informações de credenciais estão incorretas!")
                cont = 0

    elif op == 2:
        print("-" * 45)
        print(f"{'REGISTRAR':^45}")
        print("-" * 45)
        user = input("Digite o nome de usuário: ")
        senha = input("Digite a senha para o cadastro: ")
        senhaconf = input("Confirme a senha para cadastro: ")
        while senha != senhaconf:
            print("As senhas não coincidem.")
            senhaconf = input("Confirme a senha para cadastro: ")
        registraUser(user, senha)
        sleep(1)

        print("Usuário registrado com sucesso!")
    elif op == 3:
        break

    else:
        print("\n\033[1;31mValor inválido.\033[m\n Reiniciando operação.")
        sleep(2)
