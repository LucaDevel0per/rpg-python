import random
from models.monstro import Monstro

prefixos = [ "O Grande", "O Terrível", "O Mestre", "O Guardião", "O Cruel", "O Sangrento", "O Implacável"]
sufixos = ["Maldito", "Fantasma", "Morto", "Demônio", "Lorde", "Sombra", "Matador", "Sangue-Suga", "Maluco", "Da Silva", 
          "Sombrio", "Noturno", "Assassino", "Devorador", "Impiedoso", "Brutal"]

# Tipos de monstros por área
tipos_monstros = {
    "floresta": ["Lobo", "Urso", "Javali", "Aranha Gigante", "Goblin"],
    "caverna": ["Troll", "Kobold", "Morcego Gigante", "Slime", "Esqueleto"],
    "montanha": ["Ogro", "Harpia", "Golem", "Yeti", "Grifo"],
    "pântano": ["Lodo", "Crocodilo", "Planta Carnívora", "Lesma Gigante", "Zumbi"]
}

def gerar_monstro(nivel_dificuldade=1, area="floresta"):
    """Gera um monstro com base no nível de dificuldade e na área"""
    # Escolhe aleatoriamente entre usar um tipo específico ou o formato prefixo+sufixo
    if random.random() < 0.5 and area in tipos_monstros:
        tipo = random.choice(tipos_monstros[area])
        prefixo = random.choice(prefixos)
        nome = f"{prefixo} {tipo}"
    else:
        prefixo = random.choice(prefixos)
        sufixo = random.choice(sufixos)
        nome = f"{prefixo} {sufixo}"

    # Cria o monstro
    monstro = Monstro(nome=nome)
    
    # Usa o método de ajuste de dificuldade
    monstro.ajustar_dificuldade(nivel_dificuldade)
    
    return monstro