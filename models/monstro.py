import random

class Monstro:

    def __init__(self, nome) -> None:
        self.nome = nome
        self.ataque = 5
        self.defesa = 5
        self.vida = 200

    def apresentar(self):
        return f"{self.nome} (Ataque: {self.ataque}, Defesa: {self.defesa})"
    
    def __str__(self) -> str:
        return self.apresentar()
    
    def status(self):
        return f'{self.nome} está com {self.vida} de vida!'
    
    def atacar(self, inimigo):
        ataque_base = self.ataque * random.randint(1, 10)
        dano = max(ataque_base - inimigo.defesa, 0)
        if dano >= 50:
            print(f"DANO CRITICO: {self.nome} causou {dano} de dano!")
            inimigo.vida -= dano
            return
        print(f"{self.nome} atacou {inimigo.nome} e causou {dano} de dano!")
        inimigo.vida -= dano


# def atacar(self, inimigo):
#         ataque_base = self.ataque * random.randint(1,10)
#         dano = max(ataque_base - inimigo.defesa, 0)
#         if dano >= 50:
#             print(f"DANO CRITICO: Você causou {dano} de dano!")
#             return
#         print(f"Você atacou {inimigo.nome} e causou {dano} de dano!")
#         inimigo.vida -= dano