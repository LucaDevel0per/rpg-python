import random
from colorama import Fore, Style

class Monstro:

    def __init__(self, nome) -> None:
        self.nome = nome
        self.ataque = 5
        self.defesa = 5
        self.vida = 50
        self.xp_valor = 30  # XP base que o monstro concede ao morrer

    def apresentar(self):
        return f"{self.nome} (Ataque: {self.ataque}, Defesa: {self.defesa})"
    
    def __str__(self) -> str:
        return self.apresentar()
    
    def status(self):
        if self.vida > 35:
            cor = Fore.RED
        elif self.vida > 15:
            cor = Fore.YELLOW
        else:
            cor = Fore.GREEN
        return f'{cor}{self.nome} está com {self.vida} de vida!'
    
    def atacar(self, inimigo):
        # Chance de defesa perfeita do jogador
        if random.random() < 0.15:  # 15% de chance do jogador esquivar
            print(Fore.CYAN + f"{inimigo.nome} desviou do ataque de {self.nome}!")
            return
            
        ataque_base = self.ataque * random.randint(1, 10)
        dano = max(ataque_base - inimigo.defesa, 0)
        if dano >= 50:
            print(Fore.RED + Style.BRIGHT + f"DANO CRÍTICO: {self.nome} causou {dano} de dano!")
            inimigo.vida -= dano
            return
        print(Fore.RED + f"{self.nome} atacou {inimigo.nome} e causou {dano} de dano!")
        inimigo.vida -= dano
    
    def ajustar_dificuldade(self, nivel):
        """Ajusta as estatísticas do monstro com base no nível do jogador"""
        multiplicador = max(1, nivel * 0.4)  # A partir do nível 3, monstros começam a ficar mais fortes
        self.ataque = int(self.ataque * multiplicador)
        self.defesa = int(self.defesa * multiplicador)
        self.vida = int(self.vida * multiplicador)
        self.xp_valor = int(self.xp_valor * multiplicador)  # XP aumenta com base no nível


# def atacar(self, inimigo):
#         ataque_base = self.ataque * random.randint(1,10)
#         dano = max(ataque_base - inimigo.defesa, 0)
#         if dano >= 50:
#             print(f"DANO CRITICO: Você causou {dano} de dano!")
#             return
#         print(f"Você atacou {inimigo.nome} e causou {dano} de dano!")
#         inimigo.vida -= dano