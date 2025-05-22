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
        
    
    def habilidade(self, inimigo):
        chance_de_errar = random.randint(1,10)
        if chance_de_errar >= 7:
            return f"Você errou seu ataque e perdeu sua vez!"
        dano_adicional = random.randint(9,13)
        dano_total = dano_adicional * self.ataque
        inimigo.vida -= dano_adicional
        return f'Você usou sua habilidade especial: Estrondo! e causou {dano_total} de dano no adversário!'



