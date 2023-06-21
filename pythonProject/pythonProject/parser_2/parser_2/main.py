import pyautogui as pag
import pyperclip
from time import sleep
pag.FAILSAFE = False

pag.moveRel(100,100,0.2)
pag.PAUSE = 1
pag.hotkey('command', 'tab', iterval=1)
pag.PAUSE = 1

for i in range(5045):
    #1
    pag.click(100,100)
    pag.hotkey('command', 'shift', 'c', iterval=1)
    pag.click(x=357, y=155, duration=1)
    pag.hotkey('command', 'c', iterval=1)
    with open('pars.txt','a') as f:
        f.write(pyperclip.paste() + '\n')

    #2
    pag.click()
    pag.hotkey('command', 'shift', 'c', iterval=1)
    pag.click(x=354, y=207, duration=0)
    pag.hotkey('command', 'c', iterval=0)
    with open('pars.txt', 'a') as f:
        f.write(pyperclip.paste() + '\n')

    #3
    pag.click()
    pag.hotkey('command', 'shift', 'c', iterval=1)
    pag.click(x=353, y=266, duration=0)
    pag.hotkey('command', 'c', iterval=0)
    with open('pars.txt', 'a') as f:
        f.write(pyperclip.paste() + '\n')

    #4
    pag.click()
    pag.hotkey('command', 'shift', 'c', iterval=1)
    pag.click(x=354, y=319, duration=0)
    pag.hotkey('command', 'c', iterval=0)
    with open('pars.txt','a') as f:
        f.write(pyperclip.paste() + '\n')

    #5
    pag.click()
    pag.hotkey('command', 'shift', 'c', iterval=1)
    pag.click(x=354, y=375, duration=0)
    pag.hotkey('command', 'c', iterval=0)
    with open('pars.txt','a') as f:
        f.write(pyperclip.paste() + '\n')

    #6
    pag.click()
    pag.hotkey('command', 'shift', 'c', iterval=1)
    pag.click(x=352, y=429, duration=0)
    pag.hotkey('command', 'c', iterval=0)
    with open('pars.txt','a') as f:
        f.write(pyperclip.paste() + '\n')

    #7
    pag.click()
    pag.hotkey('command', 'shift', 'c', iterval=1)
    pag.click(x=351, y=486, duration=0)
    pag.hotkey('command', 'c', iterval=0)
    with open('pars.txt','a') as f:
        f.write(pyperclip.paste() + '\n')

    #8
    pag.click()
    pag.hotkey('command', 'shift', 'c', iterval=1)
    pag.click(x=353, y=542, duration=0)
    pag.hotkey('command', 'c', iterval=0)
    with open('pars.txt','a') as f:
        f.write(pyperclip.paste() + '\n')

    #9
    pag.click()
    pag.hotkey('command', 'shift', 'c', iterval=1)
    pag.click(x=354, y=596, duration=0)
    pag.hotkey('command', 'c', iterval=0)
    with open('pars.txt','a') as f:
        f.write(pyperclip.paste() + '\n')

    #10
    pag.click()
    pag.hotkey('command', 'shift', 'c', iterval=1)
    pag.click(x=355, y=651, duration=0)
    pag.hotkey('command', 'c', iterval=0)
    with open('pars.txt','a') as f:
        f.write(pyperclip.paste() + '\n')

    #переход
    pag.click()
    pag.click(x=943, y=718)
    pag.sleep(4)