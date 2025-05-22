import random
from models.monstro import Monstro

prefixos = ["O Estuprado", "O Grande", "O Terrível", "O Mestre", "O Guardião"]
sufixos = ["Maldito", "Fantasma", "Morto", "Demônio", "Lorde", "Sombra", "Matador", "Sangue-Suga", "Maluco", "Da Silva"]

def gerar_monstro(nivel_dificuldade=1):
    prefixo = random.choice(prefixos)
    sufixo = random.choice(sufixos)
    nome = f"{prefixo} {sufixo}"

    # Cria o monstro
    monstro = Monstro(nome=nome)
    
    # Ajusta as estatísticas com base no nível
    monstro.ataque = 5 + nivel_dificuldade * 2
    monstro.defesa = 5 + nivel_dificuldade * 1

    return monstro