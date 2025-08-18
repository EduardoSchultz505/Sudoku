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
    dif="0"

    while dif=="0":
        dificuldade = input()
        if dificuldade=="1":
            dif=24
        elif dificuldade=="2":
            dif=28
        elif dificuldade=="3":
            dif=34
        elif dificuldade=="4":
            while dif=="0":
                print("Adicione a média de casas para retirar: ")
                dif=(input())
                if dif.isalpha() or int(dif)>81 or int(dif)<=0:
                    print("Valor inválido")
                    dif="0"
            dif=int(dif)

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
        filaA = [8, 2, 7, 1, 5, 4, 3, 9, 6]
        filaB = [9, 6, 5, 3, 2, 7, 1, 4, 8]
        filaC = [3, 4, 1, 6, 8, 9, 7, 5, 2]
        filaD = [5, 9, 3, 4, 6, 8, 2, 7, 1]
        filaE = [4, 7, 2, 5, 1, 3, 6, 8, 9]
        filaF = [6, 1, 8, 9, 7, 2, 4, 3, 5]
        filaG = [7, 8, 6, 2, 3, 5, 9, 1, 4]
        filaH = [1, 5, 4, 7, 9, 6, 8, 2, 3]
        filaI = [2, 3, 9, 8, 4, 1, 5, 6, 7]

    elif jogo==2:
        filaA = [5, 3, 4, 6, 7, 8, 9, 1, 2]
        filaB = [6, 7, 2, 1, 9, 5, 3, 4, 8]
        filaC = [1, 9, 8, 3, 4, 2, 5, 6, 7]
        filaD = [8, 5, 9, 7, 6, 1, 4, 2, 3]
        filaE = [4, 2, 6, 8, 5, 3, 7, 9, 1]
        filaF = [7, 1, 3, 9, 2, 4, 8, 5, 6]
        filaG = [9, 6, 1, 5, 3, 7, 2, 8, 4]
        filaH = [2, 8, 7, 4, 1, 9, 6, 3, 5]
        filaI = [3, 4, 5, 2, 8, 6, 1, 7, 9]

    elif jogo==3:
        filaA = [4, 3, 5, 2, 6, 9, 7, 8, 1]  
        filaB = [6, 8, 2, 5, 7, 1, 4, 9, 3]  
        filaC = [1, 9, 7, 8, 3, 4, 5, 6, 2]  
        filaD = [8, 2, 6, 1, 9, 5, 3, 4, 7]  
        filaE = [3, 7, 4, 6, 8, 2, 9, 1, 5]  
        filaF = [9, 5, 1, 7, 4, 3, 6, 2, 8]  
        filaG = [5, 1, 9, 3, 2, 6, 8, 7, 4]  
        filaH = [2, 4, 8, 9, 5, 7, 1, 3, 6]  
        filaI = [7, 6, 3, 4, 1, 8, 2, 5, 9]  

    elif jogo==4:
        filaA = [8, 2, 7, 1, 5, 4, 3, 9, 6]  
        filaB = [9, 6, 5, 3, 2, 7, 1, 4, 8]  
        filaC = [3, 4, 1, 6, 8, 9, 7, 5, 2]  
        filaD = [5, 9, 3, 4, 6, 8, 2, 7, 1]  
        filaE = [4, 7, 2, 5, 1, 3, 6, 8, 9]  
        filaF = [6, 1, 8, 9, 7, 2, 4, 3, 5]  
        filaG = [7, 8, 6, 2, 3, 5, 9, 1, 4]  
        filaH = [1, 5, 4, 7, 9, 6, 8, 2, 3]  
        filaI = [2, 3, 9, 8, 4, 1, 5, 6, 7]

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
    tabuleiro=('''   1 2 3   4 5 6   7 8 9
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
    print(tabuleiro.format(*[valor for fila in matriz for valor in fila]))
    

def jogar (matriz, matrizOG):
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    while matriz!=matrizOG:
        mostrar_tabuleiro(matriz)
        print("Escolha uma linha para jogar (Letra, número e posição; a2 3) ou digite sair:")
        tentativa=input().replace(" ","").lower()
        os.system('cls' if os.name == 'nt' else 'clear')

        if tentativa.lower()=="sair":
            print("Obrigado por jogar! O tabuleiro correto era:")
            mostrar_tabuleiro(matrizOG)
            input()
            inicio()

        if len(tentativa) != 3 or tentativa[0] not in letras or not tentativa[1].isdigit() or not tentativa[2].isdigit():
            print("Posição incorreta")
            continue

        valor=tentativa[2]
        coluna=int(tentativa[1])-1
        linha=letras.index(tentativa[0])

        if int(valor)==matrizOG[linha][coluna]:
            (matriz[linha][coluna])=int(valor)

        else:
            print ("Jogada errada!")

    mostrar_tabuleiro(matriz)
    print("Parabéns! Você ganhou, digite qualquer tecla para voltar ao menu!")
    aleatorio=input()
    inicio()

inicio()

