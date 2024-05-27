# Jogo de batalha naval

## Passo a passo

- Definir o tamanho do tabuleiro
  - 10x10
- Definição (quantidade x tamanho) dos navios
  - 4x1
  - 3x2
  - 2x3
  - 1x4
- Posicionar os navios nos tabuleiros (meu e do oponente) de forma "aleatória", seguinto as regras:
  - O navio deve estar inteiro dentro do tabuleiro
  - Ao redor de um navio não podem existir outros navios
  - Os navios podem estar na horizontal ou vertical
  - Os navios não podem se sobrepôr em uma mesma casa do tabuleiro
- Esconder os navios do oponente
- Imprimir os dois tabuleiros na tela (meu e do oponente)
- Escolher quem vai jogar primeiro
- Solicitar coordenadas do jogador. Cada tiro será apenas 1 coordenada! Opção: bomba com cordenadas em cruz!
  - Verificar se coordenada já foi jogada ou não
    - Se coordenada não foi jogada anteriormente
      - Verificar se coordenada acertou ou não um navio
        - Se acertou um navio: marca com um acerto no tabuleiro e jogador faz outra jogada
          - Verificar se todos os navios já foram atingidos (fim de jogo!)
        - Se acertou água: marca com um erro e passa a jogada para outro jogador