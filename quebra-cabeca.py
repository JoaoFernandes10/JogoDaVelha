#!/usr/bin/python3.6
from random import randint
from os import system
num = [[], [[]], [[]], [[]], [[]]]
mist = [[], [[]], [[]], [[]], [[]]]



def main():
    criarSequencia()
    misturarnum()
    tela()
    jogar()
    if num == mist:
        print('Parabéns! Você Venceu')
    
def jogar():
    while num != mist:
        pos1 = int(input('Informe a jogada: '))
        if not bool(pos1):
            print('Game Over')
            break
        else:
            linha = int(str(pos1)[0])
            coluna = int(str(pos1)[1])
            if jogadaValida(linha, coluna):
                pos2 = posicaoAtual()
                trocarnum(pos1, pos2, mist)
                tela()
    
def posicaoAtual():
    for i in range(1, 5):# percorre linha
        for j in range(1, 5):# percorre coluna
            if mist[i][j] == "<|>":
                pos = "{}{}".format(str(i), str(j))
    return int(pos)

def jogadaValida(linha, coluna, matriz=mist):
    pos = posicaoAtual()
    if is_vizinha(linha, coluna, pos):
        return True
    else:
        return False

def is_vizinha(linha, coluna, pos):
    el = str(pos)
    l = int(el[0])
    c = int(el[1])
    if linha > 0 < coluna and linha < 5 > coluna: 
        if l == linha and c - 1 == coluna: # vizinha
            return True
        if l == linha and c + 1 == coluna: # vizinha
            return True
        if c == coluna and l - 1 == linha: # vizinha
            return True
        if c == coluna and l + 1 == linha: # vizinha
            return True
    return False

def criarSequencia():
    i = a = 1
    while a <= 16:
        num[i].append(a)
        mist[i].append(a)
        if a == 16:
            mist[4].pop()
            num[4].pop()
            num[4].append('<|>')
            mist[4].append('<|>')
        if a % 4 == 0:
            i += 1
        
        a += 1
        

def trocarnum(pos1, pos2, matriz=mist):
    global num
    el1 = matriz[pos1 // 10][pos1 % 10]
    el2 = matriz[pos2 // 10][pos2 % 10]
    matriz[pos1 // 10][pos1 % 10] = el2
    matriz[pos2 // 10][pos2 % 10] = el1


def misturarnum():
    trocarnum(randint(11, 14), randint(21, 24))
    trocarnum(randint(31, 34), randint(41, 43))
    trocarnum(randint(11, 14), randint(21, 24))
    trocarnum(randint(31, 34), randint(41, 43))

def tela():
    system('clear')
    print("=" * 40)
    print('|{:^38}|'.format('Digite 0 pra encerrar o jogo'))
    print("=" * 40)
    for i in range(1, 5):
        print("=" * 40)
        print("|{:^9}|{:^8}|{:^9}|{:^9}|".format(mist[i][1], mist[i][2], mist[i][3], mist[i][4]))
    print("=" * 40)
    print("=" * 40)

main()
