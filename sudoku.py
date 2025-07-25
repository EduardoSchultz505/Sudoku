import random
import os
import copy

def inicio():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
     █████████                 █████          █████                
     ███░░░░░███               ░░███          ░░███                 
    ░███    ░░░  █████ ████  ███████   ██████  ░███ █████ █████ ████
    ░░█████████ ░░███ ░███  ███░░███  ███░░███ ░███░░███ ░░███ ░███ 
     ░░░░░░░░███ ░███ ░███ ░███ ░███ ░███ ░███ ░██████░   ░███ ░███ 
     ███    ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███░░███  ░███ ░███ 
    ░░█████████  ░░████████░░████████░░██████  ████ █████ ░░████████
    ░░░░░░░░░    ░░░░░░░░  ░░░░░░░░  ░░░░░░  ░░░░ ░░░░░   ░░░░░░░░ 
            ''')
            
    print("Escolha a dificuldade:")
    print("1 - Fácil")
    print("2 - Médio")
    print("3 - Difícil")
    print("4 - Customizado")
    print("5 - Sair")
    dif=0

    while dif==0:
        dificuldade = input()
        if dificuldade=="1":
            dif=24
        elif dificuldade=="2":
            dif=28
        elif dificuldade=="3":
            dif=34
        elif dificuldade=="4":
            print("Adicione a média de casas para retirar: ")
            dif = int(input())
        elif dificuldade=="5" or dificuldade=="sair":
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()
        else:
            print("Dificuldade errada")

    selecionaTabuleiro(dif)  

def selecionaTabuleiro(dif):
    os.system('cls' if os.name == 'nt' else 'clear')
    jogo=random.randrange(5)
    if jogo==0:
        filaA = [5, 3, 4, 6, 7, 8, 9, 1, 2]
        filaB = [6, 7, 2, 1, 9, 5, 3, 4, 8]
        filaC = [1, 9, 8, 3, 4, 2, 5, 6, 7]
        filaD = [8, 5, 9, 7, 6, 1, 4, 2, 3]
        filaE = [4, 2, 6, 8, 5, 3, 7, 9, 1]
        filaF = [7, 1, 3, 9, 2, 4, 8, 5, 6]
        filaG = [9, 6, 1, 5, 3, 7, 2, 8, 4]
        filaH = [2, 8, 7, 4, 1, 9, 6, 3, 5]
        filaI = [3, 4, 5, 2, 8, 6, 1, 7, 9]
    
    elif jogo==1:
        filaA = [2, 4, 7, 9, 5, 1, 3, 6, 8]
        filaB = [9, 6, 3, 7, 2, 8, 1, 5, 4]
        filaC = [5, 1, 8, 4, 3, 6, 9, 7, 2]
        filaD = [6, 7, 4, 8, 9, 2, 5, 1, 3]
        filaE = [3, 8, 1, 6, 7, 5, 4, 2, 9]
        filaF = [7, 2, 9, 1, 4, 3, 6, 8, 5]
        filaG = [1, 9, 5, 3, 6, 7, 8, 4, 0]
        filaH = [8, 3, 6, 5, 1, 4, 2, 9, 7]
        filaI = [4, 5, 2, 0, 8, 9, 7, 3, 1]

    elif jogo==2:
        filaA = [4, 8, 3, 9, 2, 1, 7, 5, 6]
        filaB = [9, 6, 7, 3, 4, 5, 8, 2, 1]
        filaC = [2, 5, 1, 6, 7, 8, 9, 3, 4]
        filaD = [5, 4, 8, 1, 3, 2, 6, 9, 7]
        filaE = [7, 2, 9, 5, 6, 4, 1, 8, 3]
        filaF = [6, 1, 3, 7, 8, 9, 4, 0, 2]
        filaG = [8, 7, 6, 4, 1, 3, 2, 0, 9]
        filaH = [3, 9, 2, 8, 5, 7, 0, 1, 0]
        filaI = [1, 0, 5, 2, 9, 6, 3, 4, 8]

    elif jogo==3:
        filaA = [7, 1, 9, 5, 3, 4, 6, 8, 2]
        filaB = [3, 5, 4, 6, 8, 2, 7, 9, 1]
        filaC = [6, 8, 2, 9, 7, 1, 4, 5, 3]
        filaD = [1, 7, 5, 4, 2, 9, 3, 6, 8]
        filaE = [9, 4, 3, 7, 6, 8, 1, 2, 5]
        filaF = [2, 6, 8, 1, 5, 3, 9, 7, 4]
        filaG = [5, 9, 6, 3, 1, 7, 8, 4, 0]
        filaH = [8, 3, 7, 2, 4, 6, 5, 1, 9]
        filaI = [4, 2, 1, 8, 9, 5, 0, 3, 7]

    elif jogo==4:
        filaA = [4, 1, 5, 9, 6, 7, 2, 3, 8]
        filaB = [8, 2, 3, 1, 5, 4, 6, 9, 7]
        filaC = [6, 7, 9, 3, 2, 8, 4, 5, 1]
        filaD = [7, 3, 1, 6, 9, 5, 8, 4, 2]
        filaE = [2, 6, 4, 8, 7, 1, 9, 1, 5]
        filaF = [5, 9, 8, 2, 4, 3, 1, 7, 6]
        filaG = [1, 4, 2, 5, 3, 6, 7, 8, 9]
        filaH = [9, 8, 7, 4, 1, 2, 5, 6, 3]
        filaI = [3, 5, 6, 7, 8, 9, 1, 2, 4]

    matriz=[filaA,filaB,filaC,filaD,filaE,filaF,filaG,filaH,filaI]
    matrizOG=copy.deepcopy(matriz)
    ocultaValores(matriz,dif,matrizOG)

def ocultaValores(matriz, dif,matrizOG):
    vazio="."
    indice=0
    while indice!=dif:
        num1=int(random.randrange(9))
        num2=int(random.randrange(9))
        if matriz[num1][num2]==vazio:
            indice=indice-1
        matriz[num1][num2]=vazio
        indice=indice+1
    jogar(matriz, matrizOG)

def mostrar_tabuleiro(matriz):
    tabuleiro=('''
   1 2 3   4 5 6   7 8 9
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
   ――――――――――――――――――――――
          ''')
    print(tabuleiro.format(*[valor for fila in matriz for valor in fila]))
    

def jogar (matriz, matrizOG):
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    while matriz!=matrizOG:
        mostrar_tabuleiro(matriz)
        print("Escolha uma linha para jogar (d1, b3, i8) ou digite sair:")
        tentativa=input().replace(" ","").lower()
        os.system('cls' if os.name == 'nt' else 'clear')
        if tentativa.lower()=="sair":
            print("Obrigado por jogar! O tabuleiro correto era:")
            mostrar_tabuleiro(matrizOG)
            inicio()
        elif len(tentativa)!=3:
            print("Posição incorreta")
            continue

        valor=tentativa[2]
        coluna=int(tentativa[1])-1
        linha=letras.index(tentativa[0])

        if matriz[linha][coluna]==int(valor):
            print ("Local já preenchido")
        if int(valor)==matrizOG[linha][coluna]:
            (matriz[linha][coluna])=int(valor)

        else:
            print ("Jogou errado! Tentativas restantes")

    mostrar_tabuleiro(matriz)
    print('''
     █████   █████  ███   █████                        ███           
    ░░███   ░░███  ░░░   ░░███                        ░░░            
     ░███    ░███  ████  ███████    ██████  ████████  ████   ██████  
     ░███    ░███ ░░███ ░░░███░    ███░░███░░███░░███░░███  ░░░░░███ 
     ░░███   ███   ░███   ░███    ░███ ░███ ░███ ░░░  ░███   ███████ 
     ░░░█████░     ░███   ░███ ███░███ ░███ ░███      ░███  ███░░███ 
        ░░███      █████  ░░█████ ░░██████  █████     █████░░████████
        ░░░      ░░░░░    ░░░░░   ░░░░░░  ░░░░░     ░░░░░  ░░░░░░░░ 
          ''')
    print("Parabéns! Você ganhou, digite 1 para jogar novamente!")
    denovo=input()
    if denovo==1:
        inicio()

def sair ():
    a=1

inicio()
