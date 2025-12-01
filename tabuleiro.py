import random
import copy
from dados import TABULEIROS

class Board:
    """Classe do tabuleiro de Sudoku"""

    def __init__(self, dificuldade):
        self._matrizOG = copy.deepcopy(random.choice(TABULEIROS))
        self._matriz = copy.deepcopy(self._matrizOG)
        self.ocultar(dificuldade)

    def ocultar(self, dif):
        """Oculta valores aleatórios do tabuleiro."""
        vazio = "."
        removidos = 0
        while removidos < dif:
            x = random.randrange(9)
            y = random.randrange(9)
            if self._matriz[x][y] != vazio:
                self._matriz[x][y] = vazio
                removidos += 1

    def mostrar(self):
        """Mostra o tabuleiro com cores."""
        print(self.formatar(self._matriz))

    def mostrar_final(self):
        """Mostra o tabuleiro original."""
        print(self.formatar(self._matrizOG))

    def completo(self):
        """Verifica se o tabuleiro foi completado."""
        return self._matriz == self._matrizOG

    def jogada(self, linha, coluna, valor):
        """Retorna True se o valor estiver correto."""
        if self._matrizOG[linha][coluna] == valor:
            self._matriz[linha][coluna] = valor
            return True
        else:
            return False

    def colocar_valor(self, linha, coluna, valor):
        """Coloca um valor no tabuleiro sem verificar acerto."""
        self._matriz[linha][coluna] = valor

    def formatar(self, _matriz):
        """Formata o tabuleiro para exibição com cores."""
        VERDE = "\033[92m"
        VERMELHO = "\033[91m"
        RESET = "\033[0m"

        itens = []
        for i in range(9):
            for j in range(9):
                valor = _matriz[i][j]
                if valor == ".":
                    itens.append(".")
                else:
                    if valor == self._matrizOG[i][j]:
                        itens.append(f"{VERDE}{valor}{RESET}")
                    else:
                        itens.append(f"{VERMELHO}{valor}{RESET}")

        tabuleiro = ('''   1 2 3   4 5 6   7 8 9
  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
A ▏{} {} {} ▏ {} {} {} ▏ {} {} {} ▏  
B ▏{} {} {} ▏ {} {} {} ▏ {} {} {} ▏  
C ▏{} {} {} ▏ {} {} {} ▏ {} {} {} ▏  
  ▏――――――――――――――――――――――▏  
D ▏{} {} {} ▏ {} {} {} ▏ {} {} {} ▏  
E ▏{} {} {} ▏ {} {} {} ▏ {} {} {} ▏  
F ▏{} {} {} ▏ {} {} {} ▏ {} {} {} ▏  
  ▏――――――――――――――――――――――▏  
G ▏{} {} {} ▏ {} {} {} ▏ {} {} {} ▏  
H ▏{} {} {} ▏ {} {} {} ▏ {} {} {} ▏  
I ▏{} {} {} ▏ {} {} {} ▏ {} {} {} ▏  
   ――――――――――――――――――――――''')

        return tabuleiro.format(*itens)
