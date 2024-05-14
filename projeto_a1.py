import random

def jogada():
    print ("Bem vindo ao jogo de pedra, papel e tesoura")
    vitorias = 0
    derrotas = 0
    rodadas = 0

    while True:
        usuario_escolha = input("Escolha pedra, papel ou tesoura (ou 'sair' para sair do jogo): ").lower()
        if usuario_escolha == "sair":
           print("Obrigada por jogar! Até a próxima")
           break
        elif usuario_escolha not in ['pedra', 'papel', 'tesoura']:
          print("Escolha inválida. Por favor, escolha pedra, papel ou tesoura.")
          continue

        computador_escolha = random.choice(['pedra', 'papel','tesoura'])

        print("Você escolheu:", usuario_escolha)
        print("O computador escolheu:", computador_escolha)

        if usuario_escolha == computador_escolha:
            print("Empate!")
        elif (usuario_escolha == 'pedra' and computador_escolha == 'tesoura') or \
             (usuario_escolha == 'papel' and computador_escolha == 'pedra') or \
             (usuario_escolha == 'tesoura' and computador_escolha == 'papel'):
            print("Você venceu!")
            vitorias += 1

        else:
            print("Você perdeu!")
            derrotas += 1

        rodadas += 1
        if rodadas == 3:
           break
    print(f"Total de vitórias: {vitorias}")
    print(f"Total de derrotas: {derrotas}")

if __name__ == "__main__":
    jogada()
