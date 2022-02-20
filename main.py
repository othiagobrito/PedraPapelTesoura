from random import randint

op = ["Tesoura", "Pedra", "Papel"]
placar = [0, 0]

def game():
    try:
        escolha = int(input("Escolha sua jogada:\n1.Tesoura\t2. Pedra\t3. Papel\n> "))
    except:
        print("Entrada inválida. Tente novamente.\n")
    else:
        print()

        escolha -= 1

        bot = randint(0, 2)

        if escolha == bot:
            # Empate
            print(f"Bot jogou {op[bot]} e você {op[escolha]}. Resultado\nEmpate!\n")
        else:
            # Pedra vs Tesoura
            if escolha == 1 and bot == 0:
                print(f"Bot jogou {op[bot]} e você {op[escolha]}. Resultado\nVocê ganhou!\n")
                placar[0] += 1
            elif escolha == 0 and bot == 1:
                print(f"Bot jogou {op[bot]} e você {op[escolha]}. Resultado\nVocê perdeu!\n")
                placar[1] += 1
            
            # Tesoura vs Papel
            elif escolha == 0 and bot == 2:
                print(f"Bot jogou {op[bot]} e você {op[escolha]}. Resultado\nVocê ganhou!\n")
                placar[0] += 1
            elif escolha == 2 and bot == 0:
                print(f"Bot jogou {op[bot]} e você {op[escolha]}. Resultado\nVocê perdeu!\n")
                placar[1] += 1
            
            # Papel vs Pedra
            elif escolha == 2 and bot == 1:
                print(f"Bot jogou {op[bot]} e você {op[escolha]}. Resultado\nVocê ganhou!\n")
                placar[0] += 1
            elif escolha == 1 and bot == 2:
                print(f"Bot jogou {op[bot]} e você {op[escolha]}. Resultado\nVocê perdeu!\n")
                placar[1] += 1
            
        print(f"Placar: Jogador {placar[0]} - {placar[1]} Bot\n")

while True:
    game()

    try:
        novamente = input("Jogar novamente (S/N): ").lower()
    except:
        print("Entrada inválida! Digite novamente.\n")
    else:
        if novamente == "n":
            print("\nObrigado por jogar.")
            break
