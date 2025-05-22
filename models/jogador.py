import random
from abc import ABC, abstractmethod
from colorama import Fore, Style

class Jogador:
    def __init__(self, nome, ataque, defesa):
        self.nome = nome
        self.vida = 100
        self.ataque = ataque
        self.defesa = defesa
        self.xp = 0
        self.nivel = 1
        self.xp_proximo_nivel = 100  # XP necessário para chegar ao nível 2

    def atacar(self, inimigo):
        # Chance de defesa perfeita do inimigo
        if random.random() < 0.1:  # 10% de chance
            print(Fore.CYAN + f"{inimigo.nome} desviou do seu ataque!")
            return

        ataque_base = self.ataque * random.randint(1,10)
        dano = max(ataque_base - inimigo.defesa, 0)
        if dano >= 50:
            print(Fore.YELLOW + Style.BRIGHT + f"DANO CRÍTICO: Você causou {dano} de dano!")
            inimigo.vida -= dano
            return
        print(Fore.GREEN + f"Você atacou {inimigo.nome} e causou {dano} de dano!")
        inimigo.vida -= dano

    @abstractmethod
    def habilidade(self):
        pass

    def status(self):
        if self.vida > 70:
            cor = Fore.GREEN
        elif self.vida > 30:
            cor = Fore.YELLOW
        else:
            cor = Fore.RED
        return f'{cor}{self.nome} está com {self.vida} de vida!'

    def __str__(self):
        return f'Nome: {self.nome} - {self.ataque} de ataque - {self.defesa} de defesa - Nível: {self.nivel}'
    
    def ganhar_xp(self, quantidade):
        """Adiciona XP ao jogador e verifica se subiu de nível"""
        self.xp += quantidade
        mensagem = f"Você ganhou {quantidade} pontos de XP!"
        
        # Verifica se o jogador subiu de nível
        while self.xp >= self.xp_proximo_nivel:
            self.nivel += 1
            # Aumenta os atributos do personagem
            self.ataque += 2
            self.defesa += 1
            self.vida = min(self.vida + 20, 100 + (self.nivel - 1) * 10)  # Aumenta vida máxima por nível
            
            # Atualiza o XP necessário para o próximo nível (aumenta 50% a cada nível)
            self.xp -= self.xp_proximo_nivel
            self.xp_proximo_nivel = int(self.xp_proximo_nivel * 1.5)
            
            mensagem += f"\n{Fore.YELLOW + Style.BRIGHT}LEVEL UP! Agora você é nível {self.nivel}!"
            mensagem += f"\n+2 de ataque, +1 de defesa, +10 de vida máxima!"
        
        return mensagem

class Guerreiro(Jogador):
    def __init__(self, nome, ataque, defesa):
        super().__init__(nome, ataque, defesa)
        self.cooldown_habilidade = 0
        self.inventario ={
            "poção_de_vida": 2,
            "poção_atk": 1
        }

        self.buff_ataque = 0
        self.valor_buff = 0
    
    def habilidade(self, inimigo):
        if self.cooldown_habilidade > 0:
            return f'Habilidade em cooldown! Espere mais {self.cooldown_habilidade} turnos para usar a habilidade.'

        chance_de_errar = random.randint(1,10)
        if chance_de_errar >= 7:
            self.cooldown_habilidade = 2
            return f"Você errou seu ataque e perdeu sua vez!"
            
        dano_adicional = random.randint(9,13)
        dano_total = dano_adicional * self.ataque
        # Corrigindo o bug: agora usando dano_total em vez de dano_adicional
        inimigo.vida -= dano_total
        self.cooldown_habilidade = 3
        return f'Você usou sua habilidade especial: Estrondo! e causou {dano_total} de dano no adversário!'
    
    def usar_pocao_vida(self):
        if self.inventario["poção_de_vida"] <= 0:
            return "Você não tem poções de vida!"
        
        cura = random.randint(15, 30)
        vida_maxima = 100 + (self.nivel - 1) * 10  # Vida máxima aumenta com o nível
        self.vida = min(self.vida + cura, vida_maxima)
        self.inventario["poção_de_vida"] -= 1
        return f"Você usou uma poção de vida e recuperou {cura} de vida! Agora está com {self.vida}/{vida_maxima} HP!"
    
    def usar_pocao_atk(self):
        if self.inventario['poção_atk'] <= 0:
            return "Você não tem poções de ataque!"

        self.valor_buff = random.randint(5, 10)
        self.buff_ataque = 3
        self.inventario['poção_atk'] -=1
        return f'Você usou uma poção de ataque e ganhou +{self.valor_buff} de ataque por 3 turnos!'
    
    def atualizar_status(self):
        if self.cooldown_habilidade > 0:
            self.cooldown_habilidade -=1

        ataque_original = self.ataque
        if self.buff_ataque > 0:
            self.ataque = ataque_original + self.valor_buff
            self.buff_ataque -=1
            if self.buff_ataque == 0:
                self.ataque = ataque_original
                self.valor_buff = 0
                return f'O efeito da poção de ataque acabou!'
            return f"Buff de ataque: +{self.valor_buff} por mais {self.buff_ataque} turnos."
        return None




