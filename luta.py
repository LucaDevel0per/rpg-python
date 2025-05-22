from models.jogador import Guerreiro
from utils.gerar_monstros import gerar_monstro
import random

player = Guerreiro('Luca', 10, 15)
monstro = gerar_monstro(2)

print(f"O monstro gerado é {monstro}!")
turno = 1


while player.vida > 0 and monstro.vida > 0:
    print(f"\n--- Turno {turno} ---")

    status_msg = player.atualizar_status()
    if status_msg:
        print(status_msg)

    cooldown_info = f"Cooldown de habilidade: {player.cooldown_habilidade} turnos" if player.cooldown_habilidade > 0 else "Habilidade pronta!"
    print(cooldown_info)

    print(f"Inventário: {player.inventario['poção_de_vida']} poções de vida, {player.inventario['poção_atk']} poções de ataque")


    escolha = input("Escolha:\n[1] Atacar\n[2] Usar Habilidade\n[3] Usar Poção de vida\n[4] Usar Poção de ataque\n")
    try:
        if escolha == "1":
            player.atacar(monstro)
        elif escolha == "2":
            print(player.habilidade(monstro))
        elif escolha == '3':
            print(player.usar_pocao_vida())
        elif escolha == '4':
            print(player.usar_pocao_atk())
        else:
            print("Opção invalida!")


        if monstro.vida <=0:
            print("Você venceu!")
            break

        monstro.atacar(player)

        print(player.status())
        print(monstro.status())
        
        if player.vida <= 0:
            print("Você foi derrotado...")
            break

        turno +=1
    except ValueError:
        print("Ocorreu um erro. Tente novamente.")
        continue