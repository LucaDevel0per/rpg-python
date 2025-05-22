# 🎮 RPG Adventure

![RPG Adventure Banner](https://img.shields.io/badge/RPG-Adventure-blue?style=for-the-badge)
![Python Version](https://img.shields.io/badge/Python-3.6+-green?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

## 📖 Visão Geral

**RPG Adventure** é um jogo de RPG de texto em português, desenvolvido para praticar e demonstrar conceitos fundamentais de Programação Orientada a Objetos (POO) e manipulação de funções em Python. O jogador embarca em uma aventura através de diferentes áreas, enfrentando monstros e evoluindo seu personagem.

> *"Uma jornada épica onde você enfrenta criaturas temíveis em busca de glória e honra."*

## ✨ Funcionalidades Principais

- **Sistema de Combate por Turnos**: Ataque, use habilidades especiais e itens para derrotar monstros
- **Progressão de Personagem**: Ganhe XP, suba de nível e melhore seus atributos
- **Sistema de Cooldown**: Gerencie o uso estratégico de habilidades poderosas
- **Inventário de Itens**: Colete e use poções de vida e poções de ataque
- **Múltiplas Áreas**: Explore diferentes regiões com monstros exclusivos
- **Mecânicas de Defesa**: Chance de esquivar ou realizar defesas perfeitas
- **Sistema de Salvamento**: Salve seu progresso e continue sua jornada mais tarde
- **Histórico de Jogos**: Acompanhe suas vitórias e derrotas passadas
- **Interface Colorida**: Visual aprimorado com o uso da biblioteca Colorama

## 🚀 Instalação

### Pré-requisitos
- Python 3.6 ou superior
- pip (gerenciador de pacotes Python)

### Configuração

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/rpg-adventure.git
   cd rpg-adventure
   ```

2. Instale as dependências:
   ```bash
   pip install colorama
   ```

3. Execute o jogo:
   ```bash
   python menu.py
   ```

## 🎮 Como Jogar

1. No menu principal, você pode:
   - Iniciar uma nova jornada
   - Carregar um jogo salvo
   - Ver histórico de partidas
   - Sair do jogo

2. Durante o combate:
   - Escolha entre atacar, usar habilidade, consumir poções ou tentar fugir
   - Gerencie seus recursos estrategicamente
   - Derrote todos os monstros de uma área para avançar

3. Progressão:
   - Ganhe XP ao derrotar monstros
   - Suba de nível para aumentar seus atributos
   - Colete itens para fortalecer seu personagem

## 📂 Estrutura do Projeto

```
rpg-adventure/
│
├── menu.py              # Ponto de entrada principal com menu do jogo
├── luta.py              # Sistema de combate e progressão de áreas
├── models/
│   ├── jogador.py       # Classes de personagens jogáveis
│   └── monstro.py       # Classes de inimigos
├── utils/
│   └── gerar_monstros.py # Geração procedural de monstros
├── saves/               # Jogos salvos (criado automaticamente)
├── historico/           # Registros de jogos (criado automaticamente)
└── README.md            # Este arquivo
```

## 🎯 Objetivos de Aprendizagem

Este projeto foi criado para praticar e demonstrar:

- **Programação Orientada a Objetos**: Herança, abstração, encapsulamento
- **Manipulação de Arquivos**: Salvar/carregar estados de jogo
- **Estruturas de Dados**: Dicionários, listas e objetos complexos
- **Funções e Módulos**: Organização modular de código
- **Tratamento de Exceções**: Manipulação robusta de erros
- **Interface de Terminal**: Melhorias visuais com colorama

## 🛣️ Melhorias Futuras

### Planejadas
- **Interface Gráfica Simples**: Implementação com Pygame ou Tkinter para maior imersão
- **Mais Classes de Personagens**: Magos, Arqueiros, Assassinos, cada um com habilidades únicas
- **Sistema de Missões**: Objetivos secundários com recompensas especiais
- **Lojas e Economia**: Compra e venda de itens com sistema de moeda
- **Combate Multiplayer**: Modo cooperativo ou competitivo
- **Chefes Especiais**: Inimigos únicos com mecânicas especiais
- **Sistema de Reputação**: Suas escolhas afetam como o mundo reage ao seu personagem

### Em Consideração
- **Geração Procedural de Dungeons**: Mapas aleatórios a cada jogo
- **Trilha Sonora**: Música e efeitos sonoros para maior imersão
- **Sistema de Conquistas**: Desbloqueie realizações especiais

## 💡 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fork este repositório
2. Criar uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adicionei uma nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abrir um Pull Request

## 📄 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE) - veja o arquivo LICENSE para detalhes.

## 🙏 Agradecimentos

- Todos os que contribuíram para este projeto
- A incrível comunidade Python

---

<p align="center">
  Feito com ❤️ para todos os amantes de RPG e entusiastas de Python
</p>
