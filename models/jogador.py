import random
from abc import ABC, abstractmethod

class Jogador:
    def __init__(self, nome,ataque, defesa):
        self.nome = nome
        self.vida = 100
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, inimigo):
        ataque_base = self.ataque * random.randint(1,10)
        dano = max(ataque_base - inimigo.defesa, 0)
        if dano >= 50:
            print(f"DANO CRITICO: Você causou {dano} de dano!")
            inimigo.vida -= dano
            return
        print(f"Você atacou {inimigo.nome} e causou {dano} de dano!")
        inimigo.vida -= dano

    @abstractmethod
    def habilidade(self):
        pass

    def status(self):
        return f'{self.nome} está com {self.vida} de vida!'

    def __str__(self):
        return f'Nome: {self.nome} - {self.ataque} de ataque - {self.defesa} de defesa'

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
        inimigo.vida -= dano_adicional
        self.cooldown_habilidade = 3
        return f'Você usou sua habilidade especial: Estrondo! e causou {dano_total} de dano no adversário!'
    
    def usar_pocao_vida(self):
        if self.inventario["poção_de_vida"] <= 0:
            return "Você não tem poções de vida!"
        
        cura = random.randint(15, 30)
        self.vida = min(self.vida + cura, 100)
        self.inventario["poção_de_vida"] -= 1
        return f"Você usou uma poção de vida e recuperou {cura} de vida!"
    
    def usar_pocao_atk(self):
        if self.inventario['poção_atk'] <= 0:
            return "Você não tem poções de ataque!"

        self.valor_buff = random.randint(5, 10)
        self.buff_ataque = 3
        self.inventario['poção_atk'] -=1
        return f'Você usou uma poção de ataque e ganhou +{self.valor_buff} de ataque!'
    
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




