import os
from tabuleiro import Board

class JogoBase:
    """Abstração por contrato."""
    def inicio(self):
        raise NotImplementedError()

    def jogar(self, board: Board):
        raise NotImplementedError()


class Jogo(JogoBase):
    """Classe principal do Sudoku."""

    def __init__(self):
        self.letras = ['a','b','c','d','e','f','g','h','i']

    def limpar(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def inicio(self):
        self.limpar()
        print("Bem-vindo ao Sudoku!\n")
        print("Escolha a dificuldade:")
        print("1 - Fácil")
        print("2 - Médio")
        print("3 - Difícil")
        print("4 - Customizado")
        print("5 - Sair")

        board = None
        while not board:
            escolha = input(" ")
            if escolha == "1":
                board = Board(24)
            elif escolha == "2":
                board = Board(28)
            elif escolha == "3":
                board = Board(34)
            elif escolha == "4":
                while True:
                    n = input("Quantidade de casas para ocultar: ")
                    if not n.isdigit() or int(n) <= 0 or int(n) > 81:
                        print("Valor inválido.")
                    else:
                        board = Board(int(n))
                        break
            elif escolha == "5":
                self.limpar()
                exit()
            else:
                print("Opção inválida!")

        self.jogar(board)

    def jogar(self, board: Board):
        self.limpar()
        while not board.completo():
            board.mostrar()
            print("Digite jogada (ex: a3 9) ou 'sair':")
            tentativa = input().replace(" ", "").lower()
            self.limpar()

            if tentativa == "sair":
                print("Tabuleiro correto era:")
                board.mostrar_final()
                return

            if len(tentativa) != 3 or tentativa[0] not in self.letras:
                print("Entrada inválida.")
                continue

            linha = self.letras.index(tentativa[0])
            coluna = int(tentativa[1]) - 1
            valor = tentativa[2]

            if not valor.isdigit():
                print("Valor inválido.")
                continue

            correto = board.jogada(linha, coluna, int(valor))
            if not correto:
                board.colocar_valor(linha, coluna, int(valor))
                print("Errado!")
            else:
                print("Correto!")

        board.mostrar()
        print("Parabéns! Você completou o Sudoku!")


if __name__ == "__main__":
    Jogo().inicio()
