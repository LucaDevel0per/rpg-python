import time
import os
import json
import pickle
from colorama import init, Fore, Back, Style
from models.jogador import Guerreiro
from luta import iniciar_jornada

# Inicializa o colorama
init(autoreset=True)

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_titulo():
    """Exibe o título do jogo"""
    titulo = """
    ╔══════════════════════════════════════════════════════╗
    ║                                                      ║
    ║   █▀█ █▀█ █▀▀   █▀█ █░█ █▀▀ █▄░█ ▀█▀ █░█ █▀█ █▀▀   ║
    ║   █▀▄ █▀▀ █▀▀   █▀█ ▀▄▀ █▀▀ █░▀█ ░█░ █░█ █▀▄ █▀▀   ║
    ║   ▀░▀ ▀░░ ▀▀▀   ▀░▀ ░▀░ ▀▀▀ ▀░░▀ ▀▀▀ ▀▀▀ ▀░▀ ▀▀▀   ║
    ║                                                      ║
    ╚══════════════════════════════════════════════════════╝
    """
    print(Fore.CYAN + Style.BRIGHT + titulo)
    time.sleep(0.5)

def exibir_menu():
    """Exibe o menu principal"""
    print(Fore.YELLOW + "\n════════ MENU PRINCIPAL ════════")
    print(Fore.WHITE + "[1] " + Fore.GREEN + "Iniciar Jornada")
    print(Fore.WHITE + "[2] " + Fore.BLUE + "Carregar Jornada")
    print(Fore.WHITE + "[3] " + Fore.MAGENTA + "Ver Histórico")
    print(Fore.WHITE + "[4] " + Fore.RED + "Sair")
    print(Fore.YELLOW + "═════════════════════════════\n")

def iniciar_nova_jornada():
    """Inicia uma nova jornada"""
    limpar_tela()
    print(Fore.GREEN + "Iniciando nova jornada...\n")
    time.sleep(1)
    
    nome = input(Fore.CYAN + "Digite o nome do seu herói: ")
    print(Fore.YELLOW + "\nCriando seu herói...")
    time.sleep(1)
    
    player = Guerreiro(nome, 10, 15)
    print(Fore.GREEN + f"\nHerói {player.nome} criado com sucesso!")
    print(Fore.WHITE + "Ataque: " + Fore.RED + f"{player.ataque}")
    print(Fore.WHITE + "Defesa: " + Fore.BLUE + f"{player.defesa}")
    print(Fore.WHITE + "Vida: " + Fore.GREEN + f"{player.vida}")
    time.sleep(2)
    
    print(Fore.CYAN + "\nVocê acorda em uma pequena clareira e se lembra da missão que lhe foi dada...")
    time.sleep(1.5)
    print(Fore.CYAN + "Derrotar os monstros que assolam a região e trazer paz novamente...")
    time.sleep(2)
    
    # Inicia a jornada
    player = iniciar_jornada(player)
    
    # Salvar jogo após a jornada (se o jogador sobreviver)
    if player.vida > 0:
        salvar_jogo(player)
        adicionar_ao_historico(player, True)
    else:
        adicionar_ao_historico(player, False)
    
    input(Fore.CYAN + "\nPressione Enter para voltar ao menu principal...")
    return

def carregar_jornada():
    """Carrega uma jornada salva"""
    limpar_tela()
    print(Fore.BLUE + "Carregando jornada salva...\n")
    time.sleep(1)
    
    if not os.path.exists("saves"):
        os.makedirs("saves")
    
    # Lista os jogos salvos
    saves = [f for f in os.listdir("saves") if f.endswith('.save')]
    
    if not saves:
        print(Fore.RED + "Nenhum jogo salvo encontrado!")
        time.sleep(2)
        input(Fore.CYAN + "\nPressione Enter para voltar ao menu principal...")
        return
    
    print(Fore.YELLOW + "Jogos salvos disponíveis:")
    for i, save in enumerate(saves, 1):
        nome = save.replace('.save', '')
        print(Fore.WHITE + f"[{i}] " + Fore.GREEN + f"{nome}")
    
    try:
        escolha = int(input(Fore.CYAN + "\nEscolha um jogo para carregar (0 para voltar): "))
        if escolha == 0:
            return
        
        if 1 <= escolha <= len(saves):
            arquivo = saves[escolha - 1]
            with open(f"saves/{arquivo}", 'rb') as f:
                player = pickle.load(f)
                print(Fore.GREEN + f"\nJogo de {player.nome} carregado com sucesso!")
                time.sleep(1)
                
                # Continua a jornada
                player = iniciar_jornada(player)
                
                # Salvar jogo após a jornada (se o jogador sobreviver)
                if player.vida > 0:
                    salvar_jogo(player)
                    adicionar_ao_historico(player, True)
                else:
                    adicionar_ao_historico(player, False)
        else:
            print(Fore.RED + "Escolha inválida!")
            time.sleep(2)
    except ValueError:
        print(Fore.RED + "Entrada inválida!")
        time.sleep(2)
    
    input(Fore.CYAN + "\nPressione Enter para voltar ao menu principal...")
    return

def salvar_jogo(player):
    """Salva o jogo atual"""
    if not os.path.exists("saves"):
        os.makedirs("saves")
    
    with open(f"saves/{player.nome}.save", 'wb') as f:
        pickle.dump(player, f)
    
    print(Fore.GREEN + f"\nJogo salvo com sucesso como {player.nome}.save!")
    time.sleep(1)

def adicionar_ao_historico(player, vitoria):
    """Adiciona uma entrada ao histórico de jogos"""
    if not os.path.exists("historico"):
        os.makedirs("historico")
        
    # Carregar histórico existente ou criar novo
    historico_file = "historico/historico.json"
    if os.path.exists(historico_file):
        with open(historico_file, 'r') as f:
            try:
                historico = json.load(f)
            except json.JSONDecodeError:
                historico = []
    else:
        historico = []
    
    # Adicionar nova entrada ao histórico
    nova_entrada = {
        "nome": player.nome,
        "data": time.strftime("%d/%m/%Y %H:%M:%S"),
        "vitoria": vitoria,
        "nivel_final": player.nivel,
        "vida_final": player.vida,
        "xp_final": player.xp
    }
    
    historico.append(nova_entrada)
    
    # Salvar histórico atualizado
    with open(historico_file, 'w') as f:
        json.dump(historico, f, indent=2)

def exibir_historico():
    """Exibe o histórico de jogos"""
    limpar_tela()
    print(Fore.MAGENTA + "Histórico de Jogadores\n")
    time.sleep(0.5)
    
    historico_file = "historico/historico.json"
    if not os.path.exists(historico_file):
        print(Fore.RED + "Nenhum histórico encontrado!")
        time.sleep(2)
        input(Fore.CYAN + "\nPressione Enter para voltar ao menu principal...")
        return
    
    try:
        with open(historico_file, 'r') as f:
            historico = json.load(f)
        
        if not historico:
            print(Fore.RED + "Histórico vazio!")
            time.sleep(2)
            input(Fore.CYAN + "\nPressione Enter para voltar ao menu principal...")
            return
        
        print(Fore.YELLOW + "╔═══════════════════════════════════════════════════════════════════════╗")
        print(Fore.YELLOW + "║  Nome       │ Data            │ Resultado  │ Nível │ Vida  │ XP      ║")
        print(Fore.YELLOW + "╠═══════════════════════════════════════════════════════════════════════╣")
        
        for entrada in historico:
            nome = entrada["nome"][:10].ljust(10)
            data = entrada["data"]
            resultado = "Vitória" if entrada["vitoria"] else "Derrota"
            nivel = str(entrada.get("nivel_final", 1)).ljust(5)
            vida = str(entrada.get("vida_final", 0)).ljust(5)
            xp = str(entrada.get("xp_final", 0)).ljust(7)
            
            cor = Fore.GREEN if entrada["vitoria"] else Fore.RED
            print(Fore.YELLOW + "║ " + cor + f"{nome} │ {data} │ {resultado.ljust(9)} │ {nivel} │ {vida} │ {xp}" + Fore.YELLOW + " ║")
        
        print(Fore.YELLOW + "╚═══════════════════════════════════════════════════════════════════════╝")
        
        input(Fore.CYAN + "\nPressione Enter para voltar ao menu principal...")
    
    except Exception as e:
        print(Fore.RED + f"Erro ao carregar histórico: {e}")
        time.sleep(2)
        input(Fore.CYAN + "\nPressione Enter para voltar ao menu principal...")

def main():
    """Função principal que gerencia o menu e o fluxo do jogo"""
    while True:
        limpar_tela()
        exibir_titulo()
        exibir_menu()
        
        try:
            escolha = input(Fore.CYAN + "Digite sua escolha: ")
            
            if escolha == "1":
                iniciar_nova_jornada()
            elif escolha == "2":
                carregar_jornada()
            elif escolha == "3":
                exibir_historico()
            elif escolha == "4":
                limpar_tela()
                print(Fore.CYAN + "Obrigado por jogar! Até a próxima aventura!")
                time.sleep(1)
                break
            else:
                print(Fore.RED + "Opção inválida! Por favor, tente novamente.")
                time.sleep(1)
        
        except KeyboardInterrupt:
            limpar_tela()
            print(Fore.CYAN + "\nJogo encerrado pelo usuário. Até a próxima aventura!")
            break
        except Exception as e:
            print(Fore.RED + f"Erro: {e}")
            time.sleep(2)

if __name__ == "__main__":
    main() 