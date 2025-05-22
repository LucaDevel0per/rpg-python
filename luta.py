from models.jogador import Guerreiro
from utils.gerar_monstros import gerar_monstro
import random
import time
from colorama import init, Fore, Back, Style

# Inicializa o colorama
init(autoreset=True)

# Definição das áreas do jogo e suas histórias
areas_jogo = [
    {
        "nome": "floresta",
        "titulo": "A Floresta Sussurrante",
        "descricao": "Uma floresta densa e sombria, onde os galhos das árvores parecem sussurrar segredos antigos.",
        "dificuldade": 1,
        "monstros_para_avancar": 3,
    },
    {
        "nome": "caverna",
        "titulo": "As Cavernas Esquecidas",
        "descricao": "Um labirinto de túneis escuros e úmidos, onde ecos de civilizações perdidas ainda ressoam.",
        "dificuldade": 2,
        "monstros_para_avancar": 4,
    },
    {
        "nome": "montanha",
        "titulo": "Os Picos Gelados",
        "descricao": "Montanhas íngremes e cobertas de neve, onde o ar é rarefeito e predadores espreitam a cada curva.",
        "dificuldade": 3,
        "monstros_para_avancar": 5,
    },
    {
        "nome": "pântano",
        "titulo": "O Pântano Nefasto",
        "descricao": "Uma região pantanosa e fétida, onde o solo traiçoeiro pode engolir os incautos e criaturas mutantes espreitam sob a superfície.",
        "dificuldade": 4,
        "monstros_para_avancar": 6,
    }
]

def iniciar_luta(player, area_atual=0, progresso_area=0):
    # Obtém a área atual
    area = areas_jogo[area_atual]
    
    # Se for a primeira luta na área, mostra a introdução
    if progresso_area == 0:
        print(Fore.CYAN + Style.BRIGHT + f"\n=== {area['titulo']} ===")
        print(Fore.CYAN + area['descricao'])
        time.sleep(2)
        print(Fore.YELLOW + f"\nVocê precisa derrotar {area['monstros_para_avancar']} monstros para avançar para a próxima área.")
        time.sleep(1.5)
    
    # Gera um monstro adequado para o nível do jogador e área
    monstro = gerar_monstro(max(player.nivel, area['dificuldade']), area['nome'])

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
        vida_maxima = 100 + (player.nivel - 1) * 10
        print(f"\n{Fore.GREEN + player.nome}: {player.vida}/{vida_maxima} HP | Nível: {player.nivel} | XP: {player.xp}/{player.xp_proximo_nivel}")
        print(f"{Fore.RED + monstro.nome}: {monstro.vida} HP")
        time.sleep(0.5)
        
        escolha = input(Fore.CYAN + "\nEscolha:\n" + 
                        Fore.WHITE + "[1] Atacar\n" + 
                        Fore.WHITE + "[2] Usar Habilidade\n" + 
                        Fore.WHITE + "[3] Usar Poção de Vida\n" + 
                        Fore.WHITE + "[4] Usar Poção de Ataque\n" + 
                        Fore.WHITE + "[5] Fugir\n" + 
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
                resultado = player.usar_pocao_ataque()
                print(Fore.YELLOW + resultado)
                time.sleep(1)
            elif escolha == "5":
                chance_fuga = random.randint(1, 10)
                if chance_fuga > 3:  # 70% de chance de sucesso
                    print(Fore.CYAN + "Você fugiu com sucesso!")
                    time.sleep(1)
                    return area_atual, progresso_area  # Mantém o mesmo progresso
                else:
                    print(Fore.RED + "Você falhou em fugir!")
                    time.sleep(1)
            else:
                print(Fore.RED + "Opção inválida, você perdeu o turno!")
                time.sleep(1)

            if monstro.vida <= 0:
                print(Fore.GREEN + Style.BRIGHT + "\n★★★ Você venceu! ★★★")
                
                # Ganhar XP
                xp_ganho = monstro.xp_valor
                mensagem_xp = player.ganhar_xp(xp_ganho)
                print(Fore.YELLOW + mensagem_xp)
                time.sleep(1.5)
                
                # Recompensa por vitória
                player.inventario["poção_de_vida"] += 1
                print(Fore.GREEN + "Você encontrou 1 poção de vida!")
                time.sleep(1)
                
                if random.random() < 0.3:  # 30% de chance
                    player.inventario["poção_atk"] += 1
                    print(Fore.YELLOW + "Você encontrou 1 poção de ataque!")
                    time.sleep(1)
                
                # Avança o progresso na área
                progresso_area += 1
                
                # Verifica se completou a área
                if progresso_area >= area['monstros_para_avancar']:
                    # Se não for a última área, avança para a próxima
                    if area_atual < len(areas_jogo) - 1:
                        area_atual += 1
                        progresso_area = 0
                        print(Fore.CYAN + Style.BRIGHT + "\n=== ÁREA CONCLUÍDA! ===")
                        print(Fore.YELLOW + "Você derrotou todos os monstros da área e pode avançar para a próxima região!")
                        time.sleep(2)
                    else:
                        # Se for a última área, mostra mensagem de vitória do jogo
                        print(Fore.CYAN + Style.BRIGHT + "\n\n★★★★★ PARABÉNS! ★★★★★")
                        print(Fore.YELLOW + "Você completou todas as áreas do jogo e provou seu valor como herói!")
                        time.sleep(3)
                
                return area_atual, progresso_area

            print(Fore.RED + "\nO monstro se prepara para atacar...")
            time.sleep(1)
            monstro.atacar(player)
            time.sleep(1)
            
            if player.vida <= 0:
                print(Fore.RED + Style.BRIGHT + "\n☠ Você foi derrotado... ☠")
                time.sleep(2)
                return area_atual, progresso_area
                
            turno += 1
            
        except ValueError as e:
            print(Fore.RED + f"Erro: {e}")
            time.sleep(1)
            continue
    
    return area_atual, progresso_area

# Função para iniciar a jornada do jogador
def iniciar_jornada(player):
    area_atual = 0
    progresso_area = 0
    continuar_jogando = True
    
    while continuar_jogando and player.vida > 0:
        area_atual, progresso_area = iniciar_luta(player, area_atual, progresso_area)
        
        # Após cada luta (exceto se morreu), pergunta se quer continuar
        if player.vida > 0:
            # Obtém informações da área atual
            area = areas_jogo[area_atual]
            print(Fore.YELLOW + Style.BRIGHT + f"\n=== Progresso na área: {progresso_area}/{area['monstros_para_avancar']} monstros derrotados ===")
            
            escolha = input(Fore.CYAN + "\nO que deseja fazer agora?\n" +
                            Fore.GREEN + Style.BRIGHT + "[1] Continuar lutando (próximo monstro)\n" +
                            Fore.RED + "[2] Salvar e voltar ao menu principal\n" +
                            Fore.CYAN + "> ")
            
            if escolha != "1":
                print(Fore.YELLOW + "\nSalvando progresso e retornando ao menu principal...")
                time.sleep(1)
                continuar_jogando = False
            else:
                print(Fore.GREEN + "\nPrepare-se para o próximo desafio!")
                time.sleep(1)
    
    return player

# Se o arquivo for executado diretamente, inicia uma luta de teste
if __name__ == "__main__":
    player = Guerreiro('Teste', 10, 15)
    iniciar_jornada(player)