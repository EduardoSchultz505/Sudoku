import os
from tabuleiro import Board

class Jogo:
    'Classe principal do jogo'
    def limpar(self):
        'Função para limpar a tela'
        os.system('cls' if os.name == 'nt' else 'clear')

    def inicio(self):
        'Função para iniciar o jogo, com seleção de dificuldade'
        self.limpar()
        print("""
     █████████                 █████          █████                
     ███░░░░░███               ░░███          ░░███                 
    ░███    ░░░  █████ ████  ███████   ██████  ░███ █████ █████ ████
    ░░█████████ ░░███ ░███  ███░░███  ███░░███ ░███░░███ ░░███ ░███ 
     ░░░░░░░░███ ░███ ░███ ░███ ░███ ░███ ░███ ░██████░   ░███ ░███ 
     ███    ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███░░███  ░███ ░███ 
    ░░█████████  ░░████████░░████████░░██████  ████ █████ ░░████████
    ░░░░░░░░░    ░░░░░░░░  ░░░░░░░░  ░░░░░░  ░░░░ ░░░░░   ░░░░░░░░ 
        """)

        print("Escolha a dificuldade:")
        print("1 - Fácil")
        print("2 - Médio")
        print("3 - Difícil")
        print("4 - Customizado")
        print("5 - Sair")

        dif = 0

        while dif == 0:
            escolha = input(" ")

            if escolha == "1":
                dif = 24
            elif escolha == "2":
                dif = 28
            elif escolha == "3":
                dif = 34
            elif escolha == "4":
                while dif == 0:
                    n = input("Quantidade de casas para ocultar: ")
                    if not n.isdigit() or int(n) <= 0 or int(n) > 81:
                        print("Valor inválido.")
                    else:
                        dif = int(n)
            elif escolha == "5":
                self.limpar()
                exit()
            else:
                print("Opção inválida!")

        board = Board(dif)
        self.jogar(board)

    def jogar(self, board: Board):
        'Inicia o jogo, onde o usuário adiciona suas tentativas'
        letras = ['a','b','c','d','e','f','g','h','i']

        self.limpar()
        print("Bem vindo ao Sudoku!")

        while not board.completo():
            board.mostrar()
            print("Digite jogada (ex: a3 9) ou 'sair':")
            tentativa = input().replace(" ", "").lower()
            self.limpar()

            if tentativa == "sair":
                print("Tabuleiro correto era:")
                board.mostrar_final()
                return

            if len(tentativa) != 3 or tentativa[0] not in letras:
                print("Entrada inválida.")
                continue

            linha = letras.index(tentativa[0])
            coluna = int(tentativa[1]) - 1
            valor = tentativa[2]

            if not valor.isdigit():
                print("Valor inválido.")
                continue

            correto = board.jogada(linha, coluna, int(valor))

            if not correto:
                board.matriz[linha][coluna] = int(valor)
                print("Errado!")
            else:
                print("Correto!")


        board.mostrar()
        print("Parabéns! Você completou o Sudoku!")
        return


if __name__ == "__main__":
    Jogo().inicio()
