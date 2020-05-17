from time import sleep
import pyautogui
import webbrowser
import os
from platform import system


def timer(): # counter for the next twitch box
    for m in range(13, -1, -1):
        for s in range(59, -1, -1):
                countdown = f'{m:0=2d}:{s:0=2d}'
                print(countdown, end='\r')
                sleep(1)


def box_twitch():
    sum = 0
    x = pyautogui.size()[0] # resolution coordinate x
    y = pyautogui.size()[1] # resolution coordinate y
    print('Procurando a caixa de recompensa...')
    while True:
        if system == 'Windows': # windows path to working directory is slightly different 
            box_local = pyautogui.locateOnScreen(fr'{wd}\\box.tiny.png', region=(x-380, y-126, 380, 126),confidence=0.9) # region to find the box
        else:
            box_local = pyautogui.locateOnScreen(fr'{wd}/box.tiny.png') # no region defined, you might wanna check if its clicking on the right box
        offline_local = pyautogui.locateOnScreen(fr'{wd}/offline.twitch.png') # locate the offline 
        if box_local:
            print('~'*40)
            box_center = pyautogui.center(box_local) #locate the center of the box 
            pyautogui.click(box_center) # click on the center of the box
            sum += 1
            print('Caixa de recompensa recolhida com sucesso! +50 pontos pra você.')
            print(f'Minutos para a próxima caixa:')
            timer()
        if offline_local:  # it stops when the stream is over, it can go wrong if the streamer gank another person
            print(f'Pontos recolhidos = inscrito: {sum*100}, seguidor: {sum*50}.')
            print('A live foi encerrada.')
            break


print('~'*40)
print(f'{"BEM-VINDO AO FARM TWITCH":^40}')

while True:
    print('~'*40)
    print('Você precisa estar logado na Twitch.')
    channel = str(input('Digite o canal da Twitch que você gostaria de assistir ou "info!" para informações sobre o código: '
                        '\033[4;37mhttps://www.twitch.tv/\033[m'))
    url = (f'https://www.twitch.tv/{channel}')
    print('~'*40)
    if channel == 'info!':
        print('\nComo funciona?'
        '\nEste código foi criado com o intuito de farmar as caixas de recompensas e resgatar o bônus do seu streamer favorito.' 
        '\nEstas caixas aparecem de 15 em 15 minutos e dão 50 pontos se você for um seguidor, ou 100 se você for inscrito. Algu-'
        '\nmas condições são necessarias para este codigo funcionar. Primeiro você precisa estar logado e seguir o streamer, se-'
        '\ngundo você precisa deixar o chat de transmissao exposto. Em tela cheia, modo teatro ou chat oculto este codigo não fun-'
        '\nciona. Lembre-se sempre de deixar a aba da stream aberta, você pode checar no codigo o tempo que falta para a proxima'  
        '\ncaixa. Duvidas, comentarios ou sugestões são sempre aceitos. Obrigada pela atenção.'
        '\nPs.: Este código funciona melhor no VScode, alguns erros podem aparecer em outras IDLES.'
        '\ntwitter: @quenhebarbara\n') 
    else:
        webbrowser.open(url)
        break 


system = system()
wd = os.path.dirname(os.path.realpath(__file__))
sleep(2)
print('O código começou.')
box_twitch()
