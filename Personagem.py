import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import random
from ResultadoDado import MainWindow
from utils import garantir_qt_app


class GerenciadorDado:
    def __init__(self):
        # Cria a aplicação Qt se ainda não existir, evitando múltiplas instâncias
        self.app = garantir_qt_app()
        # Cria uma única janela do dado para reutilizar durante todo o programa
        self.janela = MainWindow()

    def rolar(self, dano_min=1, dano_max=15):
        # Método para iniciar a rolagem do dado, recebendo dano mínimo e máximo para calcular o resultado
        return self.janela.rolar_dado(dano_min=dano_min, dano_max=dano_max)


class Personagem:
    def __init__(self, nome, vida, sexo, gerenciador_dado=None):
        self.nome = nome
        self.vida = vida
        self.sexo = sexo
        self.pocoes = []  # Lista para armazenar as poções do personagem
        self.max_pocoes = 8  # Limite máximo de poções que o personagem pode carregar
        self.dano_max = 15  # Dano máximo padrão para ataques
        self.revive = True  # Indica se o personagem tem uma "Poção da Fênix" disponível
        self.max_vida = vida  # Vida máxima do personagem para referência
        self.gerenciador_dado = (
            gerenciador_dado  # Referência ao gerenciador do dado para realizar rolagens
        )

    def esta_vivo(self):
        # Garante que a vida nunca fique negativa e retorna se o personagem está vivo (> 0)
        self.vida = max(0, self.vida)
        return self.vida > 0

    def atacar(self, inimigo):
        # Verifica se o personagem atacante está vivo
        if not self.esta_vivo():
            print(f"{self.nome} não pode atacar porque foi derrotado.")
            return

        # Verifica se o inimigo está vivo para atacar
        if not inimigo.esta_vivo():
            print(f"{inimigo.nome} já está derrotado.")
            return

        # Mensagem informando que o personagem vai rolar o dado para atacar
        print(
            f"{self.nome} vai rolar o dado para atacar {inimigo.nome} (dano máximo {self.dano_max})..."
        )
        print("Pressione 'Enter' para parar o dado...")

        # Realiza a rolagem do dado usando o gerenciador de dado, passando o dano máximo atual
        dano = self.gerenciador_dado.rolar(dano_min=1, dano_max=self.dano_max)

        # Caso a rolagem retorne None, o ataque é cancelado ou ocorreu erro
        if dano is None:
            print("Ataque cancelado ou erro.")
            return

        # Gera um número aleatório para chance de acerto (60%)
        chance = random.randint(1, 100)
        if chance <= 60:
            # Acertou o ataque, subtrai o dano da vida do inimigo e garante que não fique negativa
            inimigo.vida -= dano
            inimigo.vida = max(0, inimigo.vida)
            print(f"{self.nome} atacou {inimigo.nome} e causou {dano} de dano!")
        else:
            # Errou o ataque
            print(f"{self.nome} errou o ataque contra {inimigo.nome}!")

        # Verifica se o inimigo foi derrotado após o ataque
        if not inimigo.esta_vivo():
            print(f"{inimigo.nome} foi derrotado!")
        else:
            print(f"{inimigo.nome} agora tem {inimigo.vida} de vida.\n")

    def tomar_pocao(self):
        # Verifica se o personagem possui poções para usar
        if not self.pocoes:
            print(f"{self.nome} não tem mais poções!")
            return

        # Remove a primeira poção da lista para usar
        tipo = self.pocoes.pop(0)

        # Define a quantidade de cura baseada no tipo da poção
        if tipo == "lendaria":
            cura = 100
        elif tipo == "poderosa":
            cura = 50
        elif tipo == "comum":
            cura = 20
        elif tipo == "misteriosa":
            cura = self.max_vida // 2
        else:
            cura = 0

        # Aplica a cura na vida atual do personagem
        self.vida += cura
        print(f"{self.nome} tomou uma poção {tipo} e recuperou {cura} de vida!")
        print(f"Agora tem {self.vida} de vida.")
        print(f"Poções restantes: {len(self.pocoes)}\n")

    def tentar_ganhar_pocao(self):
        # Gera chance para o personagem encontrar poções enquanto explora
        chance = random.randint(1, 100)

        print(f"\n🔍 {self.nome} está explorando em busca de poções...")

        if chance <= 40:
            # 40% das vezes não encontra poções
            print(f"{self.nome} não encontrou nenhuma poção.")
            return

        # Verifica se o personagem já está com o máximo de poções
        if len(self.pocoes) >= self.max_pocoes:
            print(
                f"{self.nome} encontrou uma poção, mas já está com o máximo de {self.max_pocoes}."
            )
            return

        # Define o tipo de poção encontrada com base em probabilidade
        tipo_pocao = random.randint(1, 100)

        if tipo_pocao <= 10:
            self.pocoes.append("lendaria")
            print(f"{self.nome} encontrou uma 💎 poção lendária!")
        elif tipo_pocao <= 30:
            self.pocoes.append("poderosa")
            print(f"{self.nome} encontrou uma 🔥 poção poderosa!")
        elif tipo_pocao <= 80:
            self.pocoes.append("comum")
            print(f"{self.nome} encontrou uma 🧪 poção comum.")
        else:
            self.pocoes.append("misteriosa")
            print(f"{self.nome} encontrou uma 🌙 poção misteriosa!")

        # 5% de chance de encontrar uma Poção da Fênix, que protege da morte
        if not self.revive and random.randint(1, 100) <= 5:
            self.revive = True
            print(
                f"{self.nome} encontrou uma 🕊️ Poção da Fênix! Agora está protegido da morte novamente."
            )

    def encontrar_espada(self):
        # Chance de encontrar espadas com efeitos variados
        chance = random.randint(1, 100)

        print(f"\n🔍 {self.nome} está explorando em busca de espadas...")
        if chance <= 1:
            # Espada lendária e abençoada - aumenta muito dano e vida
            print(f"⬜ Você encontrou: Espada Branca(Lendária/Abençoada)!")
            print("Ela irradia poder... mas há algo especial nela.")
            self.dano_max += 50
            dano_vida = random.randint(10, 40)
            self.vida += dano_vida
            self.vida = max(0, self.vida)
            print("🗡️ Dano aumentado em +50!")
            print(f"🌀 A benção deu {dano_vida} de vida!")
            print(f"❤️ Vida atual: {self.vida}")

        if chance <= 10:
            # Espada lendária maldita - aumenta dano, mas causa dano na vida também
            print(f"🟨 Você encontrou: Espada Negra (Lendária/Maldita)!")
            print("⚠️ Ela irradia poder... mas há algo sinistro nela.")
            self.dano_max += 40
            dano_maldicao = random.randint(10, 40)
            self.vida -= dano_maldicao
            self.vida = max(0, self.vida)
            print("🗡️ Dano aumentado em +40!")
            print(f"💀 A maldição causou {dano_maldicao} de dano!")
            print(f"❤️ Vida atual: {self.vida}")

        elif chance <= 20:
            # Espada épica
            print(f"🟪 Você encontrou: Espada Escura (Épica)!")
            self.dano_max += 30
            print("🗡️ Dano aumentado em +30!")

        elif chance <= 30:
            # Espada rara
            print(f"🟦 Você encontrou: Espada Brilhante (Rara)!")
            self.dano_max += 20
            print("🗡️ Dano aumentado em +20!")

        elif chance <= 50:
            # Espada comum
            print(f"🟫 Você encontrou: Espada Nova (Comum)!")
            self.dano_max += 10
            print("🗡️ Dano aumentado em +10!")

        else:
            # Nenhuma espada encontrada
            print("🙁 Nenhuma espada foi encontrada dessa vez.")

    def ver_inventario(self):
        # Exibe o inventário de poções e status da Poção da Fênix
        print(f"\n🎒 Inventário de {self.nome}:")

        if self.pocoes:
            print(f"🧪 Poções disponíveis ({len(self.pocoes)}):")
            for i, tipo in enumerate(self.pocoes, start=1):
                print(f"  {i}. Poção {tipo}")
        else:
            print("🧪 Nenhuma poção no momento.")

        if self.revive:
            print("🕊️ Poção da Fênix: DISPONÍVEL (revive o herói automaticamente)")
        else:
            print("🕊️ Poção da Fênix: já usada ou não encontrada")

        print("")  # Linha em branco para separar visualmente
