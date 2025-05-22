from models.jogador import Guerreiro
from utils.gerar_monstros import gerar_monstro
import random
import time
from colorama import init, Fore, Back, Style

# Inicializa o colorama
init(autoreset=True)

player = Guerreiro('Luca', 10, 15)
monstro = gerar_monstro(2)

print(Fore.CYAN + Style.BRIGHT + f"O monstro gerado é {monstro}!")
time.sleep(1)
turno = 1

while player.vida > 0 and monstro.vida > 0:
    print(Fore.YELLOW + Style.BRIGHT + f"\n--- Turno {turno} ---")
    time.sleep(0.5)
    
    # Atualiza status do jogador (cooldowns e buffs)
    status_msg = player.atualizar_status()
    if status_msg:
        print(Fore.BLUE + status_msg)
        time.sleep(0.8)
    
    # Mostra informações de cooldown
    if player.cooldown_habilidade > 0:
        cooldown_info = f"Cooldown da habilidade: {player.cooldown_habilidade} turnos"
        print(Fore.RED + cooldown_info)
    else:
        print(Fore.GREEN + "Habilidade pronta!")
    time.sleep(0.5)
    
    # Mostra inventário
    print(Fore.MAGENTA + f"Inventário: {player.inventario['poção_de_vida']} poções de vida, {player.inventario['poção_atk']} poções de ataque")
    time.sleep(0.5)
    
    # Status do jogador e monstro
    print(f"\n{Fore.GREEN + player.nome}: {player.vida} HP | {Fore.RED + monstro.nome}: {monstro.vida} HP")
    time.sleep(0.5)
    
    escolha = input(Fore.CYAN + "\nEscolha:\n" + 
                   Fore.WHITE + "[1] Atacar\n" + 
                   Fore.WHITE + "[2] Usar Habilidade\n" + 
                   Fore.WHITE + "[3] Usar Poção de Vida\n" + 
                   Fore.WHITE + "[4] Usar Poção de Ataque\n" + 
                   Fore.CYAN + "> ")
    try:
        if escolha == "1":
            player.atacar(monstro)
            time.sleep(1)
        elif escolha == "2":
            resultado = player.habilidade(monstro)
            print(Fore.BLUE + resultado)
            time.sleep(1)
        elif escolha == "3":
            resultado = player.usar_pocao_vida()
            print(Fore.GREEN + resultado)
            time.sleep(1)
        elif escolha == "4":
            resultado = player.usar_pocao_atk()
            print(Fore.YELLOW + resultado)
            time.sleep(1)
        else:
            print(Fore.RED + "Opção inválida, você perdeu o turno!")
            time.sleep(1)

        if monstro.vida <= 0:
            print(Fore.GREEN + Style.BRIGHT + "\n★★★ Você venceu! ★★★")
            break

        print(Fore.RED + "\nO monstro se prepara para atacar...")
        time.sleep(1)
        monstro.atacar(player)
        time.sleep(1)
        
        if player.vida <= 0:
            print(Fore.RED + Style.BRIGHT + "\n☠ Você foi derrotado... ☠")
            break
            
        turno += 1
        
    except ValueError as e:
        print(Fore.RED + f"Erro: {e}")
        time.sleep(1)
        continue