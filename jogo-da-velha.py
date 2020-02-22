#!/usr/bin/python3.6
from random import randint
from os import system
casa = ['',['','','',''],['','','',''],['','','','']]

jogador = velha = ''

def main():
    global jogador, velha
    tela()
    if not escolherJogador():
        return 0
    else:
        for i in range(1, 10):
            if i % 2 != 0:
                jog()
                tela()
                if jogador == vencedor():
                    print('Parabens! voce venceu')
                    break
            else:
                velh()
                tela()
                if velha == vencedor():
                    print('Deu Velha!')
                    break
            if i == 9:
                print('Deu Empate!')


def jog():
    global jogador
    pos = input('Informe a Posicao Para {}: '.format(jogador))
    while not jogadaValida(pos[0], int(pos[1])):
        pos = input('Informe a Posicao Para {}: '.format(jogador))
    escolherPosicao(pos[0], int(pos[1]), jogador)


def velh():
    global velha
    letra = chr(randint(65, 67))
    numero = randint(1, 3)
    while not jogadaValida(letra, numero):
        letra = chr(randint(65, 67))
        numero = randint(1, 3)
    escolherPosicao(letra, numero, velha)


def jogadaValida(letra, numero):
    l = letra.upper()
    if l == 'A':
        coluna = 1
    elif l == 'B':
        coluna = 2
    elif l == 'C':
        coluna = 3
    else:
        return False
    if '' == casa[numero][coluna]:
        return True
    else:
        return False

def tela():
    system('clear')
    print("{:^20}".format('Jogo da Velha'))
    print('⁼'*32)
    print('|{:^3}|{:^4}|{:^4}|{:^4}|'.format('||', 'A', 'B', 'C'))
    print('='*20)
    print('|{:^3}|{:^4}|{:^4}|{:^4}|'.format('1', casa[1][1], casa[1][2], casa[1][3]))
    print('-'*20)
    print('|{:^3}|{:^4}|{:^4}|{:^4}|'.format('2', casa[2][1], casa[2][2], casa[2][3]))
    print('-'*20)
    print('|{:^3}|{:^4}|{:^4}|{:^4}|'.format('3', casa[3][1], casa[3][2], casa[3][3]))
    print('-'*20)

def escolherJogador():
    global jogador
    global velha
    jog = input('Escolha o que jogar X/0 : ')
    jogador = jog.upper()
    if jogador == 'X':
        velha = '0'
        return True
    elif jogador == '0':
        velha = 'X'
        return True
    else:
        print('Caractere Inválido!\nVoce Perdeu por wo')
        return False
        

def escolherPosicao(letra, numero, jogador):
    l = letra.upper()
    if l == 'A':
        coluna = 1
    elif l == 'B':
        coluna = 2
    else:
        coluna = 3
    

    casa[numero][coluna] = jogador

def vencedor():
    venc = ''
    global jogador, velha, casa
    for i in range(1, 4):
        if '' != casa[i][1] == casa[i][2] == casa[i][3]:
            return casa[i][3]
        if '' != casa[1][i] == casa[2][i] == casa[3][i]:
            return casa[3][i]
    if '' != casa[1][1] == casa[2][2] == casa[3][3]:
        return casa[3][3]
    if '' != casa[1][3] == casa[2][2] == casa[3][1]:
        return casa[3][1]

def continuar():
    msg = input('comecar : 1 => sim / 0 => nao')
    while msg == '1':
        main ()
        continuar ()
continuar ()
