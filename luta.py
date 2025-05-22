from models.jogador import Guerreiro
from utils.gerar_monstros import gerar_monstro
import random

player = Guerreiro('Luca', 10, 15)
monstro = gerar_monstro(2)

print(f"O monstro gerado é {monstro}!")


while player.vida > 0 and monstro.vida > 0:
    escolha = input("Escolha:\n[1] Atacar\n[2] Usar Habilidade\n")
    try:
        if escolha == "1":
            player.atacar(monstro)
        elif escolha == "2":
            print(player.habilidade(monstro))

        if monstro.vida <=0:
            print("Você venceu!")
            break

        monstro.atacar(player)

        print(player.status())
        print(monstro.status())
        
        if player.vida <= 0:
            print("Você foi derrotado...")
            break
    except ValueError:
        break