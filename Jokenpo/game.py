from time import sleep
from random import choice


print('=-=' * 20)
print('\033[1;35mEae, bora um JOKENPÔ?\033[m'.center(80))

jogadas = ['PEDRA', 'PAPEL', 'TESOURA']
contagem = 0
win = 0

while True:
    print()
    escolha = int(input('\033[33mDigite a sua jogada:\033[m\n\n'
    '[ \033[1;32m1\033[m ] \033[34mPedra\033[m           '
    '[ \033[1;32m2\033[m ] \033[36mPapel\033[m           '
    '[ \033[1;32m3\033[m ] \033[34mTesoura\033[m           '
    '[ \033[1;32m4\033[m ] \033[36mExit\033[m\n\n'))

    while escolha > 4 or escolha < 1:
        escolha = int(input('\033[1;31mDigite um valor adequado:\033[m '))
    if escolha == 1:
        play = 'PEDRA'
    elif escolha == 2:
        play = 'PAPEL'
    elif escolha == 3:
        play = 'TESOURA'
    elif escolha == 4:
        print('\033[1;31mFinalizando..\033[m')
        sleep(1.3)
        break

    a = '\033[1m.\033[m' * 40
    print(f'                    {a}')
    print(f'\033[3;32mJogada selecionada:\033[m \033[1;32m{play}\033[m'.center(100))
    print(f'                    {a}')
    sleep(0.7)
    print()
    print('\033[35mO computador está escolhendo uma jogada\033[m'.center(88))
    optionpc = choice(jogadas)
    sleep(1.3)

    print()
    print('\033[1m- - - - - - - - -\033[m'.center(86))
    print('\033[1;34mJO\033[m'.center(80))
    sleep(0.7)
    print('\033[1;31mKEN\033[m'.center(89))
    sleep(0.9)
    print('\033[1;33mPO\033[m'.center(97))
    print('\033[1m- - - - - - - - -\033[m'.center(86))

    print(f'\nO computador jogou:\033[1;33m {optionpc}\033[m',end='')
    print(f'O jogador lançou\033[1;33m {play}\033[m'.center(89))

    if escolha == 1:
        if optionpc == 'PEDRA':
            print('\033[1;33mEMPATE!'.center(88))
            contagem += 1
        elif optionpc == 'PAPEL':
            print('\033[1;31mVOCÊ PERDEU!\033[m'.center(89))
            contagem += 1
        else:
            print('\033[1;32mVOCÊ GANHOU!\033[m'.center(89))
            contagem += 1
            win += 1
        sleep(1.4)
    elif escolha == 2:
        if optionpc == 'PEDRA':
            print('\033[1;32mVOCÊ GANHOU!\033[m'.center(89))
            contagem += 1
            win += 1
        elif optionpc == 'PAPEL':
            print('\033[1;33mEMPATE!'.center(88))
            contagem += 1
        else:
            print('\033[1;31mVOCÊ PERDEU!\033[m'.center(89))
            contagem += 1
        sleep(1.4)
    elif escolha == 3:
        if optionpc == 'PEDRA':
            print('\033[1;31mVOCÊ PERDEU!\033[m'.center(89))
            contagem += 1
        elif optionpc == 'PAPEL':
            print('\033[1;32mVOCÊ GANHOU!\033[m'.center(89))
            contagem += 1
            win += 1
        else:
            print('\033[1;33mEMPATE!'.center(88))
            contagem += 1
        sleep(1.4)
print('.')
print('.')
print('.')
print('\033[3;31mJogo finalizado.\033[m')

dados = str(input('\033[1;33mDeseja ver os dados?\033[37m (Digite sim ou não)\n\033[m')).strip().upper()

while dados != 'SIM' and dados != 'NÃO' and dados != 'NAO':
    dados = str(input('\033[31mDigite entre \033[1mSIM\033[m \033[31mou \033[1mNÃO\033[m\033[31m:\033[m ')).strip().upper()
if dados == 'SIM':
    print()
    if win == 1:
        print('\n\033[35mVocê venceu apenas\033[1m 1 partida\033[m\033[35m. Boa sorte na próxima!\033[m')
    elif win == 0:
        print('\033[1;3;36mVocê não venceu\033[m\033[3;36m nenhuma partida\033[1m. Mas não desista por isso, confio em você!\033[m')
    else:
        print(f'\033[32mVocê venceu\033[1;32m {win} \033[m\033[32mpartidas contra o computador. \033[1;32mMeus parabéns!!\033[m')
    print(f'\033[1;33mTotal de partidas jogadas\033[m: {contagem}')
    print()
elif dados == 'NÃO' or dados == 'NAO':
    print()
    print('\033[36mBoa sorte na próxima\033[m'.center(78))
print('\033[1;32mVolte sempre!\033[m'.center(80))