import random  # Biblioteca para gerar números aleatórios
import sys
import os

sys.path.append(
    os.path.dirname(os.path.abspath(__file__))
)  # Adiciona o diretório atual no caminho de importação
import time  # Biblioteca para lidar com tempo (pausas)
from Personagem import *  # Importa tudo da classe Personagem
from Entrada import *  # Importa funções de entrada (presumivelmente)
import ctypes  # Usado para manipular janelas no Windows

# Função para imprimir texto "digitando" letra a letra, com uma pausa entre caracteres
def digitar(texto, velocidade=0.03):
    for char in texto:
        sys.stdout.write(char)  # Escreve caractere sem quebra de linha
        sys.stdout.flush()  # Garante que apareça imediatamente
        time.sleep(velocidade)  # Pausa para efeito de digitação
    print()  # Quebra de linha no final


# Função para fechar o prompt/terminal (especialmente no Windows)
def fechar_prompt():
    if os.name == "nt":  # Se for Windows
        hwnd = (
            ctypes.windll.kernel32.GetConsoleWindow()
        )  # Pega o handle da janela do console
        if hwnd != 0:
            ctypes.windll.user32.PostMessageW(
                hwnd, 0x0010, 0, 0
            )  # Envia mensagem para fechar a janela (WM_CLOSE)
    sys.exit()  # Sai do programa


# Função para criar um personagem com base na entrada do usuário
def criar_personagem(gerenciador):
    nome = input(
        "Digite o nome do seu personagem: "
    ).capitalize()  # Recebe nome e capitaliza
    exibir_mensagem_fixa()  # Exibe mensagem (função externa)
    sexo = input("Sexo do personagem: ").capitalize()  # Recebe sexo e capitaliza

    # Verifica se sexo está correto; caso contrário, exibe erro e fecha programa
    if sexo == "Masculino" or sexo == "Feminino":
        print("")
    else:
        exibir_mensagem_erro()
        time.sleep(3)
        fechar_prompt()

    # Menu para escolher modo de definir vida
    print("\nComo você quer definir a vida do personagem?")
    print("[F] Fixa (escolher entre valores pré-definidos até 600)")
    print("[A] Aleatória (entre 1 e 600)")
    print("[U] Usuário escolhe qualquer valor (até 600)")

    modo = (
        input("Escolha (F/A/U): ").strip().lower()
    )  # Recebe escolha do modo e converte para minúsculo

    if modo == "f":
        opcoes_fixas = [
            600,
            500,
            400,
            300,
            250,
            200,
            150,
            120,
            100,
            80,
            60,
            40,
            20,
            10,
            1,
        ]
        print("\nEscolha uma vida fixa:")
        # Mostra as opções numeradas para o usuário escolher
        for i, valor in enumerate(opcoes_fixas, 1):
            print(f"{i} - {valor} pontos de vida")

        try:
            escolha = int(
                input(f"Digite o número de 1 a {len(opcoes_fixas)}: ")
            )  # Recebe escolha
            if 1 <= escolha <= len(opcoes_fixas):
                vida = opcoes_fixas[escolha - 1]  # Seleciona o valor correspondente
            else:
                print("Escolha inválida. Definindo vida como 120.")  # Valor padrão
                vida = 120
        except ValueError:
            print(
                "Entrada inválida. Definindo vida como 120."
            )  # Caso o usuário não digite número
            vida = 120

    elif modo == "a":  # Modo aleatório
        vida = random.randint(1, 600)  # Gera valor aleatório de vida entre 1 e 600

    elif modo == "u":  # Modo usuário escolhe livremente
        try:
            vida = int(input("Digite a vida desejada (máximo 600): "))
            if vida > 600 or vida < 1:  # Valida limites
                print("Valor fora do limite. Definindo vida como 120.")
                vida = 120
        except ValueError:
            print("Entrada inválida. Definindo vida como 120.")
            vida = 120

    else:
        print("Modo inválido. Usando vida padrão 120.")  # Caso o modo seja inválido
        vida = 120

    # Cria a instância do personagem com nome, vida, sexo e o gerenciador de dados
    personagem = Personagem(nome, vida, sexo, gerenciador)
    personagem.modo_vida = modo  # Armazena o modo de vida escolhido
    print(
        f"\nFicha criada! {personagem.nome}, {personagem.sexo}, {personagem.vida} de vida.\n"
    )  # Mostra ficha criada para o usuário
    return personagem  # Retorna o objeto criado


# Função para limpar o terminal (tela do prompt)
def limpar_tela():
    """Limpa a tela do terminal"""
    os.system("cls" if os.name == "nt" else "clear")  # Comando para Windows e Unix


# Função para gerar uma chance/probabilidade
def chance(p):
    return random.randint(1, 100) <= p  # Retorna True se número aleatório <= p


# Função para tentar desviar de um ataque com uma porcentagem de sucesso
def tentar_desviar(porcentagem):
    return random.randint(1, 100) <= porcentagem  # Retorna True se desviar com sucesso

    
def jogar():
    while True:
        escolha = perguntar()   # <-- pega "Sim" ou "Não" do Tkinter
        if escolha == "Não":
            time.sleep(3)
            fechar_prompt()
        elif escolha == "Sim":
            time.sleep(5)
            limpar_tela()
            gerenciador = GerenciadorDado()
            heroi = criar_personagem(gerenciador)  # <-- agora chama de fato
            vida_inicial = heroi.vida
            # Saudação personalizada baseada no sexo
            if heroi.sexo == "Feminino":  # se o sexo for feminino
                print(f"Bem-vinda, {heroi.nome}!")
            else:
                print(f"Bem-vindo, {heroi.nome}!")
            while True:
                digitar('"Vamos começar nossa aventura!" Entravam na caverna e logo tinha dois caminhos.')
                digitar("Qual será nosso caminho?")
                digitar("1° Com som de música | 2° Com uma risada sinistra!")

                # Agora pede a escolha
                escolha = input(">> ").strip()

                if escolha in ["1", "2"]:
                    escolha = int(escolha)
                    break
                else:
                    print("⚠️ Escolha inválida! Digite 1 ou 2.")
            if escolha == 1:  # caso escolha 1
                digitar("Caimos num buraco")
                digitar(f'"Morremos de forma ridicula {heroi.nome} vamos tentar de novo? [S/N]: "')
                resposta = input(">> ").strip().lower()
                if resposta == "s":  # se quiser recomeçar o jogo
                    digitar('"UFA! Eu não queria um final assim"')
                    time.sleep(3)  # Espera 3 segundos
                    continue
                elif resposta == "n":
                    digitar("COVARDE!Valeu por jogar! Até a próxima.")
                    time.sleep(3)
                    fechar_prompt()
                else:
                    continue  # volta pro início do loop sem executar o que vem abaixo
            elif escolha == 2:  # caso escolha 2
                digitar(
                    f"O caminho parecia tranquilo até que, de repente, ouviam novamente aquela risada macabra. "
                    f"Viravam rapidamente, no mesmo momento viram um goblin correndo em na direção deles e brandia uma adaga afiada. "
                    f"Logo {heroi.nome} puxar uma espada"
                )
                goblin = Personagem("Goblin", 50, "Monstro")  # objeto criado para ser o inimigo
                turno = 1
                while (heroi.esta_vivo() and goblin.esta_vivo()):  # continua enquanto o heroi ou o goblin estiver vivo
                    acao = input("Deseja atacar (1)? ")
                    if acao == "1":  # atacar o goblin
                        print(f"\n--- Turno {turno} ---")
                        heroi.atacar(goblin)
                    else:
                        print("⚠️ Escolha inválida! Digite 1")

                    if goblin.esta_vivo():  # se o goblin estiver vivo, então ele atacar

                        if tentar_desviar(
                            42
                        ):  ##usar método para desviar com  42 % de chance
                            print(f"{heroi.nome} desviou do ataque de {goblin.nome}!")
                        else:  # se não desviar vai receber dano
                            dano = random.randint(1, 10)  # de 1 a 10 de dano
                            heroi.vida -= dano  # diminuir  a vida do heroi
                            print(f"Goblin atacou {heroi.nome} e causou {dano} de dano!")
                            print(f"{heroi.nome} agora tem {heroi.vida} de vida.\n")

                            if (heroi.vida <= 0 and heroi.revive):  # se o heroi morrer e puder reviver
                                digitar("\n⚰️ O silêncio domina o campo de batalha...")
                                time.sleep(1)
                                digitar(f"{heroi.nome} cai de joelhos, sem forças, seus olhos se fechando lentamente.")
                                digitar("...")
                                time.sleep(2)
                                digitar("Mas então...")
                                digitar("🔥 Uma luz intensa irrompe do peito de seu corpo.")
                                digitar("As chamas douradas da lendária Poção da Fênix envolvem seu corpo em espirais flamejantes.")
                                digitar("Um grito ecoa não da sua boca, mas da própria alma. O mundo para por um instante.")
                                digitar(f"\n🕊️ {heroi.nome.upper()} RENASCEU!")

                                heroi.vida = (heroi.max_vida)  # voltar a vida a quantidade maxima
                                heroi.dano_max += 100  # buff permanente de dano
                                heroi.revive = False

                                digitar(f"\n💪 {heroi.nome} retorna com {heroi.vida} de vida e sua força amplificada em +100 de dano!")
                                time.sleep(1)
                                digitar("Agora, seus inimigos não enfrentam mais um aventureiro...")
                                time.sleep(1)
                                digitar("...eles enfrentam a ira de alguém que venceu a morte.")
                                digitar("⚡ Os céus tremem. Os monstros recuam. O verdadeiro jogo começou.\n")

                    turno += 1

            # Resultado final - só aparece uma vez
            print("\nCombate encerrado.")
            if heroi.esta_vivo():  # caso o heroi ainda continua vivo
                print(f"{heroi.nome} venceu!")
                heroi.tentar_ganhar_pocao()
            else:  # se o heroi estiver morto
                print(f"{goblin.nome} venceu!")
                if heroi.modo_vida == "f":  # se tiver escolhido o modo de vida f e tiver escolhido vida fixa inicial de 120
                    digitar(
                        "Mestre: Sei que escolheu esse modo, mas não é ridículo morrer para um simples goblin? Tipo você tinha capacidade de durar mais...Vamos tentar de novo! [S/N]: "
                    )
                    escolha = input(">> ").strip().lower()
                    if escolha == "s":  # se escolher continuar
                        digitar("Mestre Um conselho tomar poção se necessário")
                        time.sleep(3)  # Espera 3 segundos
                        continue  # voltar ao início do loop
                    elif escolha == "n":  # se quiser terminar o loop
                        if heroi.sexo == "Feminino":  # se o sexo for Feminino
                            digitar(
                                '"Trevor: Parece que você era uma convarde desde o início"'
                            )
                            time.sleep(3)
                            fechar_prompt() 
                        else:
                            digitar(
                                '"Trevor: Parece que você era um convarde desde o início"'
                            )
                            time.sleep(3)
                            fechar_prompt() 
                    else:
                        continue  # voltar ao início do loop
                elif heroi.modo_vida == "u":  # se tiver escolhido o modo de vida u
                    digitar(
                        "Mestre: Que pena...Mas você deveria ter escolhido uma vida maior. Esquecendo isso..Quer continuar? [S/N]: "
                    )
                    escolha = input(">> ").strip().lower()
                    if escolha == "s":  # se quiser recomeçar o jogo
                        digitar("Mestre: Legal dessa vez vai dar certo!")
                        time.sleep(3)  # Espera 3 segundos
                        continue  # voltar ao início do loop
                    elif (
                        escolha == "n"
                    ):  # se quiser terminar o loop#se quiser terminar o loop
                        if heroi.sexo == "Feminino":  # se o sexo for Feminino
                            digitar("Mestre: Entendi...Valeu por jogar...perdedora")
                            time.sleep(3)
                            fechar_prompt() 
                        else:
                            digitar("Mestre: Entendi...Valeu por jogar...perdedor")
                            time.sleep(3)
                            fechar_prompt() 
                    else:
                        continue  # voltar ao início do loop
                else:
                    digitar(
                        "Mestre: Valeu por tentar jogar, mas agora quer tentar de novo? [S/N]: "
                    )
                    escolha = input(">> ").strip().lower()
                    if escolha == "s":  # se quiser recomeçar o jogo
                        digitar(f"Mestre: Legal, vamos voltar {heroi.nome}")
                        time.sleep(3)  # Espera 3 segundos
                        continue  # voltar ao início do loop
                    elif escolha == "n":  # se quiser terminar o loop
                        digitar('"Trevor: Que decepção..."')
                        time.sleep(3)  # Espera 3 segundos
                        fechar_prompt() 
                    else:
                        continue  # voltar ao início do loop
            digitar(
                f"Depois de {heroi.nome} matar o Goblin voltavam a andar em buscar do tesouro. Até que aparece um slime na frente dos dois amigos"
            )
            slime = Personagem("slime", 20, "Monstro")  # objeto criado para ser o inimigo
            turno = 1
            while (
                heroi.esta_vivo() and slime.esta_vivo()
            ):  # continua enquanto o heroi ou o slime estiver vivo
                acao = input("Deseja atacar (1) ou tomar poção (2)? ")
                if acao == "1":  # atacar o slime
                    print(f"\n--- Turno {turno} ---")
                    heroi.atacar(slime)

                elif acao == "2":  # beber poção
                    heroi.tomar_pocao()

                else:
                    print("⚠️ Escolha inválida! Digite 1 ou 2")

                # Slime ataca, se estiver vivo
                if slime.esta_vivo():
                    dano = random.randint(1, 6)
                    if tentar_desviar(55):
                        print(f"{heroi.nome} desviou do ataque de {slime.nome}!")
                    else:
                        heroi.vida -= dano
                        print(f"Slime atacou {heroi.nome} e causou {dano} de dano!")
                        print(f"{heroi.nome} agora tem {heroi.vida} de vida.\n")

                        if heroi.vida <= 0 and heroi.revive:
                            digitar("\n⚰️ O silêncio domina o campo de batalha...")
                            time.sleep(1)
                            digitar(f"{heroi.nome} cai de joelhos, sem forças, seus olhos se fechando lentamente.")
                            digitar("...")
                            time.sleep(2)
                            digitar("Mas então...")
                            digitar("🔥 Uma luz intensa irrompe do peito de seu corpo.")
                            digitar("As chamas douradas da lendária Poção da Fênix envolvem seu corpo em espirais flamejantes.")
                            digitar("Um grito ecoa não da sua boca, mas da própria alma. O mundo para por um instante.")
                            digitar(f"\n🕊️ {heroi.nome.upper()} RENASCEU!")

                            heroi.vida = (heroi.max_vida)  # voltar a vida a quantidade maxima
                            heroi.dano_max += 100  # buff permanente de dano
                            heroi.revive = False

                            digitar(f"\n💪 {heroi.nome} retorna com {heroi.vida} de vida e sua força amplificada em +100 de dano!")
                            time.sleep(1)
                            digitar("Agora, seus inimigos não enfrentam mais um aventureiro...")
                            time.sleep(1)
                            digitar("...eles enfrentam a ira de alguém que venceu a morte.")
                            digitar("⚡ Os céus tremem. Os monstros recuam. O verdadeiro jogo começou.\n")
                turno += 1

            print("\nCombate encerrado.")
            if heroi.esta_vivo():
                print(f"{heroi.nome} venceu!")
                heroi.tentar_ganhar_pocao()

            else:
                print(f"{slime.nome} venceu!")
                if heroi.modo_vida == "f":
                    digitar(
                        "Mestre: Você escolheu esse modo, mas não! Tinha que ser morto por um slime! Um slime, sério? Vamos começar de novo logo, antes que eu perca mais tempo. [S/N]: "
                    )
                    escolha = input(">> ").strip().lower()
                    if escolha == "s":
                        if heroi.sexo == "Feminino":
                            digitar(
                                "Mestre: Agora, dessa vez, tenta ficar viva, heroína... não quero ter que te aguentar de novo."
                            )
                        else:
                            digitar(
                                "Mestre: Agora, dessa vez, tenta ficar vivo, heroizinho... não quero ter que ficar aguentando você de novo."
                            )
                            continue
                    elif escolha == "n":
                        if heroi.sexo == "Feminino":
                            digitar(
                                '"Trevor: Sua inútil, eu estava quase chegando no meu objetivo, era só você abrir o caminho e depois eu te mataria para ter meu tesouro, mas você falhou!"'
                            )
                            time.sleep(3)
                            fechar_prompt()
                        else:
                            digitar(
                                '"Trevor: Seu inútil, eu estava quase chegando no meu objetivo e era só você abrir o caminho e depois eu te mataria para ter meu tesouro, mas você falhou!"'
                            )
                            time.sleep(3)
                            fechar_prompt()
                    else:
                        continue
                elif heroi.modo_vida == "u":
                    digitar(
                        "Mestre: Que pena...Mas você deveria ter escolhido uma vida maior. Esquecendo isso..Quer continuar? [S/N]: "
                    )
                    escolha = input(">> ").strip().lower()
                    if escolha == "s":
                        digitar("Mestre: Legal dessa vez vai dar certo!")
                        continue
                    elif escolha == "n":
                        if heroi.sexo == "Feminino":
                            digitar("Mestre: Entendi...Valeu por jogar...perdedora")
                            time.sleep(3)
                            fechar_prompt()
                        else:
                            digitar("Mestre: Entendi...Valeu por jogar...perdedor")
                            time.sleep(3)
                            fechar_prompt()
                    else:
                        continue
                else:
                    digitar(
                        "Mestre: Valeu por tentar jogar, mas agora quer tentar de novo? [S/N]: "
                    )
                    escolha = input(">> ").strip().lower()
                    if escolha == "s":
                        digitar(f"Mestre: Legal, vamos voltar {heroi.nome}")
                        continue
                    elif escolha == "n":
                        digitar("Mestre: Que decepção...")
                        time.sleep(3)
                        fechar_prompt()
                    else:
                        continue

            paciencia_com = 0
            digitar(
                f'"Parabéns {heroi.nome} por limpar nosso caminho para o tesouro e agora o que desejar fazer?"'
            )
            while paciencia_com <= 100:
                print(
                        "1° procurar poção| 2° sentar e afiar espada | 3° Olhar inventário | 4° Continuar : "
                    )
                
                escolha = input(">> ")
                if escolha == "1":
                    heroi.tentar_ganhar_pocao()
                    paciencia_com += 5
                elif escolha == "2":
                    digitar(f"{heroi.nome} se sentar é começar a afiar a espada")
                    heroi.dano_max += 1
                    paciencia_com += 3
                    digitar("A sua espada fica mais afiada")
                elif escolha == "3":
                    digitar(f"{heroi.nome} se sentar para ver seu inventário")
                    heroi.ver_inventario()
                elif escolha == "4":
                    digitar(f"{heroi.nome} decidir continuar sua jornada")
                    paciencia_com += 100
                else:
                    digitar(f"{heroi.nome} ficou parado")
                    paciencia_com += 1
            digitar(f'"Entendi, vem {heroi.nome} vamos achar esse tesouro!"')
            digitar(
                "Estavam andando até que dava para ouvir um grunhido estranho e logo aparecia um orc verde que estava sorrindo."
            )
            digitar("ORC:" '"Que grande sorte dois humanos para devorar!"')
            orc = Personagem("Orc", 70, "Monstro")  # objeto criado para ser o inimigo
            turno = 1
            while heroi.esta_vivo() and orc.esta_vivo():
                acao = input("Deseja atacar (1) ou tomar poção (2)? ")
                if acao == "1":  # atacar o orc
                    print(f"\n--- Turno {turno} ---")
                    heroi.atacar(orc)

                elif acao == "2":  # beber poção
                    heroi.tomar_pocao()

                else:
                    print("⚠️ Escolha inválida! Digite 1 ou 2")

                # orc ataca, se estiver vivo
                if orc.esta_vivo():
                    dano = random.randint(1, 30)
                    if tentar_desviar(25):
                        print(f"{heroi.nome} desviou do ataque de {orc.nome}!")
                    else:
                        heroi.vida -= dano
                        print(f"Orc atacou {heroi.nome} e causou {dano} de dano!")
                        print(f"{heroi.nome} agora tem {heroi.vida} de vida.\n")

                        if heroi.vida <= 0 and heroi.revive:
                            digitar("\n⚰️ O silêncio domina o campo de batalha...")
                            time.sleep(1)
                            digitar(f"{heroi.nome} cai de joelhos, sem forças, seus olhos se fechando lentamente.")
                            digitar("...")
                            time.sleep(2)
                            digitar("Mas então...")
                            digitar("🔥 Uma luz intensa irrompe do peito de seu corpo.")
                            digitar("As chamas douradas da lendária Poção da Fênix envolvem seu corpo em espirais flamejantes.")
                            digitar("Um grito ecoa não da sua boca, mas da própria alma. O mundo para por um instante.")
                            digitar(f"\n🕊️ {heroi.nome.upper()} RENASCEU!")

                            heroi.vida = (heroi.max_vida)  # voltar a vida a quantidade maxima
                            heroi.dano_max += 100  # buff permanente de dano
                            heroi.revive = False

                            digitar(f"\n💪 {heroi.nome} retorna com {heroi.vida} de vida e sua força amplificada em +100 de dano!")
                            time.sleep(1)
                            digitar("Agora, seus inimigos não enfrentam mais um aventureiro...")
                            time.sleep(1)
                            digitar("...eles enfrentam a ira de alguém que venceu a morte.")
                            digitar("⚡ Os céus tremem. Os monstros recuam. O verdadeiro jogo começou.\n")
                            digitar("Orc: Como? ")
                turno += 1

            print("\nCombate encerrado.")
            if heroi.esta_vivo():
                print(f"{heroi.nome} venceu!")
                heroi.tentar_ganhar_pocao()
            else:
                print(f"{orc.nome} venceu!")
                if heroi.modo_vida == "f":
                    digitar(
                        " Mestre: Você escolheu esse modo, mas não! Tinha que ser morto por um Orc! Vamos começar de novo logo, antes que eu perca mais tempo. [S/N]: "
                    )
                    escolha = input(">> ").strip().lower()
                    if escolha == "s":
                        if heroi.sexo == "Feminino":
                            digitar(
                                "Mestre: Agora, dessa vez, tenta ficar viva, heroína... não quero ter que te aguentar de novo."
                            )
                        else:
                            digitar(
                                '"Agora, dessa vez, tenta ficar vivo, heroizinho... não quero ter que ficar aguentando você de novo."'
                            )
                            continue
                    elif escolha == "n":
                        if heroi.sexo == "Feminino":
                            digitar(
                                '"Trevor: Sua inútil, eu estava quase chegando no meu objetivo, era só você abrir o caminho e depois eu te mataria para ter meu tesouro, mas você falhou!"'
                            )
                            time.sleep(3)
                            fechar_prompt()
                        else:
                            digitar(
                                '"Trevor: Seu inútil, eu estava quase chegando no meu objetivo e era só você abrir o caminho e depois eu te mataria para ter meu tesouro, mas você falhou!"'
                            )
                            time.sleep(3)
                            fechar_prompt()
                    else:
                        continue
                elif heroi.modo_vida == "u":
                    digitar(
                        " Mestre: Que pena...Mas você deveria ter escolhido uma vida maior. Esquecendo isso..Quer continuar? [S/N]: "
                    )
                    escolha = input(">> ").strip().lower()
                    if escolha == "s":
                        digitar("Mestre: Legal dessa vez vai dar certo!")
                        continue
                    elif escolha == "n":
                        if heroi.sexo == "Feminino":
                            digitar("Mestre: Entendi...Valeu por jogar...perdedora")
                            time.sleep(3)
                            fechar_prompt()
                        else:
                            digitar("Mestre: Entendi...Valeu por jogar...perdedor")
                            time.sleep(3)
                            fechar_prompt()
                    else:
                        continue
                else:
                    digitar(
                        "Mestre: Valeu por tentar jogar, mas agora quer tentar de novo? [S/N]: "
                    )
                    escolha = input(">> ").strip().lower()
                    if escolha == "s":
                        digitar(f"Mestre: Legal, vamos voltar {heroi.nome}")
                        continue
                    elif escolha == "n":
                        digitar("Trevor: Que decepção...")
                        time.sleep(3)
                        fechar_prompt()
                    else:
                        continue
            digitar(
                f'"Uau {heroi.nome} parabéns por matar esse orc sujo, mas agora vamos continuar porque estamos quase chegando no nosso destino"'
            )
            digitar(
                "Enquanto andavam surgir uma pessoa com um um cajado com uma bola de cristal roxa e quando apontava para eles percebiam o que era"
            )
            print(f'"Cuidado {heroi.nome} ele é um necromante!"')
            necromante = Personagem("Necromante", 110, "Monstro")  # objeto criado para ser o Necromante
            turno = 1
            while heroi.esta_vivo() and necromante.esta_vivo():
                acao = input("Deseja atacar (1) ou tomar poção (2)? ")
                if acao == "1":  # atacar o necromante
                    print(f"\n--- Turno {turno} ---")
                    heroi.atacar(necromante)

                elif acao == "2":  # beber poção
                    heroi.tomar_pocao()

                else:
                    print("⚠️ Escolha inválida! Digite 1 ou 2")

                # necromante ataca, se estiver vivo
                if necromante.esta_vivo():
                    if chance(20):         # 20% de chance de se curar
                        cura = random.randint(5, 25)
                        necromante.vida += cura
                        print(f"{necromante.nome} se recuperou e ganhou {cura} de vida!")
                        print(f"Vida atual de {necromante.nome}: {necromante.vida}")
                    elif chance(30):
                        digitar('"Não lutarei contra você, mas meu soldado sim!"')
                        esqueleto = Personagem("Esqueleto", 40, "Monstro")
                        turno1 = 1
                        while heroi.esta_vivo() and esqueleto.esta_vivo():
                            acao1 = input("Deseja atacar (1) ou tomar poção (2)? ")
                            if acao1 =="1":  # atacar o esqueleto
                                print(f"\n--- Turno {turno} ---")
                                heroi.atacar(esqueleto)

                            elif acao1 == "2":  # beber poção
                                heroi.tomar_pocao()

                            else:
                                print("⚠️ Escolha inválida! Digite 1 ou 2")

                            if (
                                esqueleto.esta_vivo()
                            ):  # se o goblin estiver vivo, então ele atacar
                                dano = random.randint(1, 10)  # de 1 a 10 de dano
                                if tentar_desviar(50):
                                    print(
                                        f"{heroi.nome} desviou do ataque de {esqueleto.nome}!"
                                    )
                                else:
                                    heroi.vida -= dano  # diminuir  a vida do heroi
                                    print(
                                        f"Esqueleto atacou {heroi.nome} e causou {dano} de dano!"
                                    )
                                    print(f"{heroi.nome} agora tem {heroi.vida} de vida.\n")

                                    if heroi.vida <= 0 and heroi.revive:
                                        digitar("\n⚰️ O silêncio domina o campo de batalha...")
                                        time.sleep(1)
                                        digitar(f"{heroi.nome} cai de joelhos, sem forças, seus olhos se fechando lentamente.")
                                        digitar("...")
                                        time.sleep(2)
                                        digitar("Mas então...")
                                        digitar("🔥 Uma luz intensa irrompe do peito de seu corpo.")
                                        digitar("As chamas douradas da lendária Poção da Fênix envolvem seu corpo em espirais flamejantes.")
                                        digitar("Um grito ecoa não da sua boca, mas da própria alma. O mundo para por um instante.")
                                        digitar(f"\n🕊️ {heroi.nome.upper()} RENASCEU!")

                                        heroi.vida = (heroi.max_vida)  # voltar a vida a quantidade maxima
                                        heroi.dano_max += 100  # buff permanente de dano
                                        heroi.revive = False

                                        digitar(f"\n💪 {heroi.nome} retorna com {heroi.vida} de vida e sua força amplificada em +100 de dano!")
                                        time.sleep(1)
                                        digitar("Agora, seus inimigos não enfrentam mais um aventureiro...")
                                        time.sleep(1)
                                        digitar("...eles enfrentam a ira de alguém que venceu a morte.")
                                        digitar("⚡ Os céus tremem. Os monstros recuam. O verdadeiro jogo começou.\n")

                            turno1 += 1
                        if heroi.esta_vivo():
                            print('"Agora o necromante"')
                        else:
                            print(f"{esqueleto.nome} venceu!")
                            if heroi.modo_vida == "f":
                                digitar(
                                    "Mestre: Você escolheu esse modo, mas não! Tinha que ser morto por um simples esqueleto! Vamos começar de novo logo, antes que eu perca mais tempo. [S/N]: "
                                )
                                escolha = input(">> ").strip().lower()
                                if escolha == "s":
                                    if heroi.sexo == "Feminino":
                                        digitar(
                                            "Mestre: Agora, dessa vez, tenta ficar viva, heroína... não quero ter que te aguentar de novo."
                                        )
                                    else:
                                        digitar(
                                            "Mestre: Agora, dessa vez, tenta ficar vivo, heroizinho... não quero ter que ficar aguentando você de novo."
                                        )
                                        continue
                                elif escolha == "n":
                                    if heroi.sexo == "Feminino":
                                        digitar(
                                            '"Trevor: Sua inútil, eu estava quase chegando no meu objetivo, era só você abrir o caminho e depois eu te mataria para ter meu tesouro, mas você falhou!"'
                                        )
                                        time.sleep(3)
                                        fechar_prompt()
                                    else:
                                        digitar(
                                            '"Trevor: Seu inútil, eu estava quase chegando no meu objetivo e era só você abrir o caminho e depois eu te mataria para ter meu tesouro, mas você falhou!"'
                                        )
                                        time.sleep(3)
                                        fechar_prompt()
                                else:
                                    continue
                            elif heroi.modo_vida == "u":
                                digitar(
                                    "Mestre: Que pena...Mas você deveria ter escolhido uma vida maior. Esquecendo isso..Quer continuar? [S/N]: "
                                )
                                escolha = input(">> ").strip().lower()
                                if escolha == "s":
                                    digitar("Mestre: Legal dessa vez vai dar certo!")
                                    continue
                                elif escolha == "n":
                                    if heroi.sexo == "Feminino":
                                        digitar(
                                            "Mestre: Entendi...Valeu por jogar...perdedora"
                                        )
                                        time.sleep(3)
                                        fechar_prompt()
                                    else:
                                        digitar(
                                            "Mestre: Entendi...Valeu por jogar...perdedor"
                                        )
                                        time.sleep(3)
                                        fechar_prompt()
                                else:
                                    continue
                            else:
                                digitar(
                                    "Mestre: Valeu por tentar jogar, mas agora quer tentar de novo? [S/N]: "
                                )
                                escolha = input(">> ").strip().lower()
                                if escolha == "s":
                                    digitar(f"Mestre: Legal, vamos voltar {heroi.nome}")
                                    time.sleep(3)
                                    continue
                                elif escolha == "n":
                                    digitar("Trevor: Que decepção...")
                                    time.sleep(3)
                                    fechar_prompt()
                                else:
                                    continue
                    else:
                        if tentar_desviar(36):
                            print(f"{heroi.nome} desviou do ataque de {necromante.nome}!")
                        else:
                            digitar(f'"É tola tentativa de tentar me derrotar"')
                            dano = random.randint(1, 20)
                            heroi.vida -= dano
                            print(f"Necromante atacou {heroi.nome} e causou {dano} de dano!")
                            print(f"{heroi.nome} agora tem {heroi.vida} de vida.\n")

                            if heroi.vida <= 0 and heroi.revive:
                                digitar("\n⚰️ O silêncio domina o campo de batalha...")
                                time.sleep(1)
                                digitar(f"{heroi.nome} cai de joelhos, sem forças, seus olhos se fechando lentamente.")
                                digitar("...")
                                time.sleep(2)
                                digitar("Mas então...")
                                digitar("🔥 Uma luz intensa irrompe do peito de seu corpo.")
                                digitar("As chamas douradas da lendária Poção da Fênix envolvem seu corpo em espirais flamejantes.")
                                digitar("Um grito ecoa não da sua boca, mas da própria alma. O mundo para por um instante.")
                                digitar(f"\n🕊️ {heroi.nome.upper()} RENASCEU!")

                                heroi.vida = (heroi.max_vida)  # voltar a vida a quantidade maxima
                                heroi.dano_max += 100  # buff permanente de dano
                                heroi.revive = False

                                digitar(f"\n💪 {heroi.nome} retorna com {heroi.vida} de vida e sua força amplificada em +100 de dano!")
                                time.sleep(1)
                                digitar("Agora, seus inimigos não enfrentam mais um aventureiro...")
                                time.sleep(1)
                                digitar("...eles enfrentam a ira de alguém que venceu a morte.")
                                digitar("⚡ Os céus tremem. Os monstros recuam. O verdadeiro jogo começou.\n")
                                digitar("Necromante: Impossível!!!")

                turno += 1
            if heroi.esta_vivo():
                if heroi.sexo == "Feminino":  # se o sexo for feminino
                    digitar(f'"Você fez algo incrivel, grande {heroi.nome}"')
                else:
                    digitar(f"Você fez algo incrivel, grandioso {heroi.nome}!")
                heroi.tentar_ganhar_pocao()
            else:
                print(f"{necromante.nome} venceu!")
                if heroi.modo_vida == "f":
                    digitar(
                        "Mestre: Sei que escolheu esse modo, mas você sabia que teria de matar um Necromante né? Esquecendo disso... quer continuar? Talvez seja melhor diminuir a dificuldade [S/N]: "
                    )
                    escolha = input(">> ").strip().lower()
                    if escolha == "s":
                        digitar("Mestre: Um conselho Tome cuidado com seus poderes")
                        continue
                    elif escolha == "n":
                        if heroi.sexo == "Feminino":
                            digitar(
                                '"Trevor: Sério...Parece que você era uma fracote desde o início"'
                            )
                            time.sleep(3)
                            fechar_prompt()
                        else:
                            digitar(
                                '"Trevor: Sério...Parece que você era um fracote desde o início"'
                            )
                            time.sleep(3)
                            fechar_prompt()
                    else:
                        continue
                elif heroi.modo_vida == "u":
                    digitar(
                        " Mestre: Que pena...Mas você deveria ter escolhido uma vida maior. Esquecendo isso..Quer continuar? [S/N]: "
                    )
                    escolha = input(">> ").strip().lower()
                    if escolha == "s":
                        digitar("Mestre: Legal dessa vez vai dar certo!")
                        continue
                    elif escolha == "n":
                        if heroi.sexo == "Feminino":
                            digitar("Mestre: Entendi...Valeu por jogar...perdedora")
                            time.sleep(3)
                            fechar_prompt()
                        else:
                            digitar("Mestre: Entendi...Valeu por jogar...perdedor")
                            time.sleep(3)
                            fechar_prompt()
                    else:
                        continue
                else:
                    digitar(
                        "Mestre: Valeu por tentar jogar, mas agora quer tentar de novo? [S/N]: "
                    )
                    escolha = input(">> ").strip().lower()
                    if escolha == "s":
                        digitar(f"Mestre: Legal, vamos voltar {heroi.nome}")
                        time.sleep(3)
                        continue
                    elif escolha == "n":
                        digitar("Trevor: Que decepção...")
                        time.sleep(3)
                        fechar_prompt()
                    else:
                        continue

            digitar(f'"Mas finalmente estamos chegando no nosso destino!"')
            digitar(
                "Continuam aprofundando na caverna até que finalmente os dois se aproximam de um grande portão feito de ouro."
            )
            time.sleep(2)
            digitar(
                f'"Finalmente chegamos no nosso destino!"'
                "O meu companheiro transparencia um sorriso grande."
            )
            digitar(
                f"{heroi.nome} firmou as mãos sobre a porta e empurrava as portas e no mesmo momento abria o portão."
            )
            digitar(
                "Entravam dentro da sala do tesouro, enquanto entrava dava para ver montes de dinheiro."
            )
            time.sleep(2)
            dragao = Personagem("Dragão", 600, "monstro")
            dragao_dormindo = 0
            digitar(
                '"Olha ali!"'
                "Ele se escondia atrás de uma pilastra e olhava para o dragão que estava adormecido."
                '"O que você quer fazer antes dele acordar?"'
            )
            ja_tem_espada = False  # controle fora do loop
            while dragao_dormindo <= 100:
                print(
                        "1° Procurar uma nova espada| 2° Procurar poção| 3° Atacar o dragão | 4° Afiar a espada | 5° Desistir: | 6° Olhar inventário: "
                    )
                escolha = input(">> ")

                if escolha == "1":
                    heroi.encontrar_espada()
                    dragao_dormindo += 10
                    ja_tem_espada = True  # marca que já pegou a espada

                elif escolha == "2":
                    heroi.tentar_ganhar_pocao()
                    dragao_dormindo += 5

                elif escolha == "3":
                    print('"O QUE VOCÊ FEZ?"')
                    dragao_dormindo += 100
                    dragao.vida -= heroi.dano_max
                    print(
                        f"{heroi.nome} atacou {dragao.nome} e causou {heroi.dano_max} de dano!"
                    )

                elif escolha == "4":
                    digitar(f"{heroi.nome} se sentar é começar a afiar a espada")
                    heroi.dano_max += 2
                    dragao_dormindo += 2

                elif escolha == "5":
                    digitar(
                        "Trevor parava na minha frente com os braços estendidos"
                        '"VOCÊ NÃO VAI FUGIR!"'
                    )
                    dragao_dormindo += 20

                elif escolha == "6":
                    digitar(f"{heroi.nome} se sentar para ver seu inventário")
                    heroi.ver_inventario()
                    dragao_dormindo += 1

                elif escolha == "7":
                    heroi.tomar_pocao()
                    dragao_dormindo += 3

                else:
                    digitar(f"{heroi.nome} ficou parado")
                    dragao_dormindo += 1

            digitar(
                "De repente, um rugido profundo e estrondoso ecoou pela caverna, como um trovão que se aproximava. As paredes tremiam, e o ar ao nosso redor parecia vibrar com a força do som. Com um enorme estalo, as asas do dragão bateram, criando um vento tão forte que quase fomos derrubados. O monstro estava acordando."
            )
            digitar(
                f"O dragão abriu seus olhos, e sua voz, como o eco de uma montanha, preencheu a caverna."
            )
            time.sleep(2)
            digitar(
                f'"Quem ousa invadir meu domínio?!" Sua voz ressoava como um trovão distante, carregada de raiva e poder.Logo {heroi.nome} erguia a sua espada. "Vocês realmente acreditam que podem me enfrentar?"'
            )
            digitar(
                f"Com um movimento lento, ele se levantou, suas escamas brilhando de forma ameaçadora, e olhou diretamente para nós, seu olhar cortante como fogo."
            )
            digitar(f'"Vocês estão no meu território agora. Não haverá misericórdia."')
            turno = 1
            while heroi.esta_vivo() and dragao.esta_vivo():
                acao = input("Deseja atacar (1) ou tomar poção (2)? ")
                if acao == "1":  # atacar o dragão
                    print(f"\n--- Turno {turno} ---")
                    heroi.atacar(dragao)

                elif acao == "2":  # beber poção
                    heroi.tomar_pocao()

                else:
                    print("⚠️ Escolha inválida! Digite 1 ou 2")

                    # orc ataca, se estiver vivo
                if dragao.esta_vivo():
                    dano = random.randint(1, 100)
                    if tentar_desviar(30):
                        print(f"{heroi.nome} desviou do ataque de {dragao.nome}!")
                    else:
                        heroi.vida -= dano
                        print(f"Dragão atacou {heroi.nome} e causou {dano} de dano!")
                        print(f"{heroi.nome} agora tem {heroi.vida} de vida.\n")

                        if heroi.vida <= 0 and heroi.revive:
                            digitar("\n⚰️ O silêncio domina o campo de batalha...")
                            time.sleep(1)
                            digitar(f"{heroi.nome} cai de joelhos, sem forças, seus olhos se fechando lentamente.")
                            digitar("...")
                            time.sleep(2)
                            digitar("Mas então...")
                            digitar("🔥 Uma luz intensa irrompe do peito de seu corpo.")
                            digitar("As chamas douradas da lendária Poção da Fênix envolvem seu corpo em espirais flamejantes.")
                            digitar("Um grito ecoa não da sua boca, mas da própria alma. O mundo para por um instante.")
                            digitar(f"\n🕊️ {heroi.nome.upper()} RENASCEU!")

                            heroi.vida = (heroi.max_vida)  # voltar a vida a quantidade maxima
                            heroi.dano_max += 100  # buff permanente de dano
                            heroi.revive = False

                            digitar(f"\n💪 {heroi.nome} retorna com {heroi.vida} de vida e sua força amplificada em +100 de dano!")
                            time.sleep(1)
                            digitar("Agora, seus inimigos não enfrentam mais um aventureiro...")
                            time.sleep(1)
                            digitar("...eles enfrentam a ira de alguém que venceu a morte.")
                            digitar("⚡ Os céus tremem. Os monstros recuam. O verdadeiro jogo começou.\n")
                            digitar("Dragão: Como você tem essa poção? ")
                turno += 1

            if heroi.esta_vivo():
                digitar(f'"{heroi.nome} você...ganhou... de um Dragão!!!!!!"')

            else: 
                print(f"{dragao.nome} venceu!")          
                if heroi.modo_vida == "f":
                    digitar(
                        "Mestre: Sei que escolheu o modo infernal, mas você sabia que teria de matar um Dragão ancião!? Esquecendo disso quer continuar? Talvez seja melhor diminuir a dificuldade [S/N]: "
                    )
                    escolha = input(">> ").strip().lower()
                    if escolha == "s":
                        digitar("Mestre: Um conselho seja mais forte")
                        continue
                    elif escolha == "n":
                        if heroi.sexo == "Feminino":
                            digitar(
                                '"Trevor: Sério...Parece que você era uma fracote desde o início"'
                            )
                            time.sleep(3)
                            fechar_prompt()
                        else:
                            digitar(
                                '"Trevor: Sério...Parece que você era um fracote desde o início"'
                            )
                            time.sleep(3)
                            fechar_prompt()
                    else:
                        continue
                elif heroi.modo_vida == "u":
                    digitar(
                        " Mestre: Que pena...Mas você deveria ter escolhido uma vida maior. Esquecendo isso..Quer continuar? [S/N]: "
                    )
                    escolha = input(">> ").strip().lower()
                    if escolha == "s":
                        print("Mestre: Legal dessa vez vai dar certo!")
                        continue
                    elif escolha == "n":
                        if heroi.sexo == "Feminino":
                            digitar("Mestre: Entendi...Valeu por jogar...perdedora")
                            time.sleep(3)
                            fechar_prompt()
                        else:
                            digitar("Mestre: Entendi...Valeu por jogar...perdedor")
                            time.sleep(3)
                            fechar_prompt()
                    else:
                        continue
                else:
                    digitar(
                        "Mestre: Valeu por tentar jogar, mas agora quer tentar de novo? [S/N]: "
                    )
                    escolha = input(">> ").strip().lower()
                    if escolha == "s":
                        digitar(f"Mestre: Legal, vamos voltar {heroi.nome}")
                        continue
                    elif escolha == "n":
                        digitar("Trevor: Que decepção...")
                        time.sleep(3)
                        fechar_prompt()
                    else:
                        continue

            digitar(
                '"Isso é fantástico, você conseguiu..."'
                f"Trevor te abraçava e no mesmo momento transparencia um sorriso maligna, então puxar uma espada estranha da sua bainha e te atravessar pela barriga"
            )
            heroi.vida -= heroi.vida // 2
            digitar(f"{heroi.nome} está com {heroi.vida} de vida")
            traidor = Personagem("Trevor", heroi.vida, "Masculino")
            digitar(
                f"Logo {heroi.nome} empurrar {traidor.nome} alguns metros de distância e mesmo começava a rir!"
                '"Acha mesmo que tudo seria como antes? Metade da sua vida já se foi — e a outra metade... vai comigo. Sua força agora é minha, sua vida também. Mas só um de nós vai sair daqui. E não vai ser você."'
            )
            time.sleep(2)
            digitar(
                '"Quando seu corpo cair, e o silêncio tomar este lugar... Eu vou fazer o que deveria ter feito há muito tempo. Vou arrancar o Coração do Dragão com as minhas próprias mãos. E ninguém mais vai me impedir."'
            )
            turno = 1
            while (
                heroi.esta_vivo() and traidor.esta_vivo()
            ):  # SE o heroi e o traidor estiver vivo
                acao = input("Deseja atacar (1) ou tomar poção (2)? ")
                if acao == "1":  # atacar o traidor
                    print(f"\n--- Turno {turno} ---")
                    heroi.atacar(traidor)

                elif acao == "2":  # beber poção
                    heroi.tomar_pocao()

                else:
                    print("⚠️ Escolha inválida! Digite 1 ou 2")

                    # traidor ataca, se estiver vivo
                if traidor.esta_vivo():
                    dano = random.randint(1, heroi.dano_max)
                    if tentar_desviar(30):
                        print(
                            f"{heroi.nome} desviou do ataque de {traidor.nome}!"
                            '"Impressionante, mas isso foi apenas sorte"'
                        )
                    else:
                        heroi.vida -= dano
                        print(
                            f"{traidor.nome} atacou {heroi.nome} e causou {dano} de dano!"
                        )
                        print(f"{heroi.nome} agora tem {heroi.vida} de vida.\n")

                        if heroi.vida <= 0 and heroi.revive:
                            digitar("\n⚰️ O silêncio domina o campo de batalha...")
                            time.sleep(1)
                            digitar(f"{heroi.nome} cai de joelhos, sem forças, seus olhos se fechando lentamente.")
                            digitar("...")
                            time.sleep(2)
                            digitar("Mas então...")
                            digitar("🔥 Uma luz intensa irrompe do peito de seu corpo.")
                            digitar("As chamas douradas da lendária Poção da Fênix envolvem seu corpo em espirais flamejantes.")
                            digitar("Um grito ecoa não da sua boca, mas da própria alma. O mundo para por um instante.")
                            digitar(f"\n🕊️ {heroi.nome.upper()} RENASCEU!")

                            heroi.vida = (heroi.max_vida)  # voltar a vida a quantidade maxima
                            heroi.dano_max += 100  # buff permanente de dano
                            heroi.revive = False

                            digitar(f"\n💪 {heroi.nome} retorna com {heroi.vida} de vida e sua força amplificada em +100 de dano!")
                            time.sleep(1)
                            digitar("Agora, seus inimigos não enfrentam mais um aventureiro...")
                            time.sleep(1)
                            digitar("...eles enfrentam a ira de alguém que venceu a morte.")
                            digitar("⚡ Os céus tremem. Os monstros recuam. O verdadeiro jogo começou.\n")
                            digitar(
                                f"{traidor.nome} começava a rir!"
                                '"Achou que eu não estava preparado? "'
                            )
                            traidor.vida = heroi.max_vida
                            traidor.dano_max += 100
                turno += 1
            if heroi.esta_vivo():  # SE o heroi estiver vivo
                time.sleep(3)
                digitar(f"{traidor.nome} estava ajoelhado no chão, o sangue escorrendo por entre os dedos trêmulos.")
                digitar(f"Ele ergueu o olhar para {heroi.nome}, esboçando um meio sorriso fraco e quebrado.")
                time.sleep(3)
                digitar(f'"No fim... eu nunca consegui te superar."')
                digitar("A cabeça dele tombou de leve, e a luz em seus olhos se apagou aos poucos.")
                digitar("Mas, com o último fôlego, ainda encontrou forças para sussurrar:")
                digitar('"Me desculpa... mãe."')
                digitar(f"\n😔 {heroi.nome} baixou a cabeça, os punhos cerrados com força, os dentes rangendo em silêncio.")
                time.sleep(3)
                digitar("💧 As lágrimas caíam, silenciosas, enquanto o campo mergulhava num silêncio sepulcral.")
                digitar("⚔️ Então, ele se abaixou e tomou em mãos a espada caída de quem um dia fora seu irmão de armas...")
                digitar("🔥 ...e com um movimento resoluto, arrancou o Coração do Dragão, ainda vibrando com o eco de eras passadas.")
                digitar("⛓️ Virando-se, afundou a espada no chão, junto ao corpo do guerreiro que um dia chamara de irmão.")
                digitar('"Que este seja o seu descanso final... meu velho amigo."')
                time.sleep(3)
                digitar("\n✨ O Coração do Dragão pulsou com uma luz incomum — como se sentisse a dor... e o arrependimento que pairavam no ar.")
                digitar("Por um breve momento, o mundo inteiro pareceu prender a respiração.")
                digitar("...")
                time.sleep(3)
                digitar(f"🕯️ Quando {heroi.nome} tornou a abrir os olhos, a caverna havia sumido.")
                digitar("Agora estava de joelhos sob o céu, e em suas mãos, o Coração do Dragão se transformava em cinzas.")
                digitar("☁️ O vento soprou leve... e as cinzas dançaram no ar, como se o próprio destino dissesse: 'já basta'.")

                time.sleep(3)
                exibir_mensagem_final()
                fechar_prompt()
                
            else:
                if heroi.sexo == "Feminino":  # se o sexo for Feminino
                    digitar(f"{traidor.nome} venceu!")
                    digitar('"Eu consegui..."')
                    digitar("...")
                    time.sleep(2)
                    digitar('"Mas matei minha única amiga."')
                    digitar("As lágrimas caíram.")
                    digitar("Ele não tentou escondê-las.")
                    digitar('"Não importa."')
                    digitar('"Com este coração... eu vou salvar minha mãe."')
                else:
                    digitar(f"{traidor.nome} venceu!")
                    digitar('"Eu consegui..."')
                    digitar("...")
                    time.sleep(2)
                    digitar('"Mas matei meu único amigo."')
                    digitar("As lágrimas caíram.")
                    digitar("Ele não tentou escondê-las.")
                    digitar('"Não importa."')
                    digitar('"Com este coração... eu vou salvar minha mãe."')
                if heroi.modo_vida == "f":
                    digitar(
                        "Mestre: Sei que escolheu o modo infernal, mas você deveria ter desconfiado do seu amigo? Talvez seja melhor diminuir a dificuldade [S/N]: "
                    )
                    escolha = input(">> ").strip().lower()
                    if escolha == "s":
                        digitar("Trevor: Por que vocÊ não aceita sua morte de uma vez?")
                        time.sleep(3)
                        continue
                    elif escolha == "n":
                            digitar(
                                '"Trevor: Obrigado por aceitar sua morte"'
                            )
                            time.sleep(3)
                            fechar_prompt()
                    else:
                        continue
                elif heroi.modo_vida == "u":
                    digitar(
                        "Mestre: Que pena...Mas você deveria ter escolhido uma vida maior. Esquecendo isso..Quer continuar? [S/N]: "
                    )
                    escolha = input(">> ").strip().lower()
                    if escolha == "s":
                        print("Mestre: Legal dessa vez vai dar certo!")
                        continue
                    elif escolha == "n":
                        digitar("Trevor: Obrigado por aceitar sua morte")
                        time.sleep(3)
                        fechar_prompt()
                    else:
                        continue
                else:
                    digitar(
                        "Mestre: Valeu por tentar jogar, mas agora quer tentar de novo? [S/N]: "
                    )
                    escolha = input(">> ").strip().lower()
                    if escolha == "s":
                        digitar(f"Trevor: Por que vocÊ não aceita sua morte de uma vez?")
                        time.sleep(3)
                        continue
                    elif escolha == "n":
                        digitar("Trevor: Obrigado por aceitar sua morte")
                        time.sleep(3)
                        fechar_prompt()
                    else:
                        time.sleep(3)
                        continue  # o jogo dentro de um loop
