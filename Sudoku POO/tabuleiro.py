import random
import copy
from dados import TABULEIROS

class Board:
    def __init__(self, dificuldade):
        self.matrizOG = copy.deepcopy(random.choice(TABULEIROS))
        self.matriz = copy.deepcopy(self.matrizOG)
        self.ocultar(dificuldade)

    def ocultar(self, dif):
        'Oculta valores aleatórios do tabuleiro'
        vazio = "."
        removidos = 0

        while removidos < dif:
            x = random.randrange(9)
            y = random.randrange(9)

            if self.matriz[x][y] != vazio:
                self.matriz[x][y] = vazio
                removidos += 1

    def mostrar(self):
        'Mostra o tabuleiro'
        print(self.formatar(self.matriz))

    def mostrar_final(self):
        'Mostra o tabuleiro se o usuário digitar sair durante o jogo'
        print(self.formatar(self.matrizOG))

    def completo(self):
        'Comparação para ver se o usuário já completou o tabuleiro'
        return self.matriz == self.matrizOG

    def jogada(self, linha, coluna, valor):
        "Retorna True se acertou."
        if self.matrizOG[linha][coluna] == valor:
            self.matriz[linha][coluna] = valor
            return True
        return False

    def formatar(self, matriz):
        'Define a cor dos valores, se certo ou errado'
        VERDE = "\033[92m"
        VERMELHO = "\033[91m"
        RESET = "\033[0m"

        itens = []
        for i in range(9):
            for j in range(9):
                valor = matriz[i][j]

                if valor == ".":
                    itens.append(".")
                else:
                    if valor == self.matrizOG[i][j]:
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

