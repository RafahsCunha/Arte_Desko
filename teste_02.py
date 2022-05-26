import pyautogui
import time


# print(pyautogui.KEYBOARD_KEYS)
# print(pyautogui.position())

pyautogui.alert('O código vai começar, não toque na máquina')

pyautogui.PAUSE = 2


t = int(1)
while t < 3:
 pyautogui.hotkey('shift', 'winleft', 's')
 pyautogui.moveTo(949,273)
 pyautogui.mouseDown()
 pyautogui.moveTo(1398, 909)
 pyautogui.mouseUp() # até aqui, recortar a plaquinha no tamanho certo
 pyautogui.moveTo(3192, 827) # move para a escolha de página do Word
 pyautogui.click(clicks = 2)
 pyautogui.press('backspace')
 pyautogui.write('t')
 pyautogui.press('enter') # até aqui seleciona a página
 pyautogui.moveTo(3863,310) # move para dentro da pág selecionada
 pyautogui.click(clicks = 2)
 pyautogui.hotkey('ctrl','v') # copia o arquivo na página
 pyautogui.moveTo(671,413) # mover para a tela das plaquinhas
 pyautogui.click(clicks=2)
 pyautogui.press('right')
 pyautogui.hotkey('shift', 'winleft', 's')
 pyautogui.moveTo(949,273)
 pyautogui.mouseDown()
 pyautogui.moveTo(1398, 909)
 pyautogui.mouseUp() # até aqui, recortar a plaquinha no tamanho certo
 pyautogui.moveTo(3192, 827) # move para a escolha de página do Word
 pyautogui.click(clicks = 2)
 pyautogui.press('backspace')
 pyautogui.write('t')
 pyautogui.press('enter') # até aqui seleciona a página
 pyautogui.moveTo(3863,310) # move para dentro da pág selecionada
 pyautogui.click(clicks = 2)
 pyautogui.hotkey('ctrl','v') # copia o arquivo na página
 pyautogui.moveTo(671,413) # mover para a tela das plaquinhas
 pyautogui.click(clicks=2)
 pyautogui.press('right')
 pyautogui.hotkey('shift', 'winleft', 's')
 pyautogui.moveTo(949,273)
 pyautogui.mouseDown()
 pyautogui.moveTo(1398, 909)
 pyautogui.mouseUp() # até aqui, recortar a plaquinha no tamanho certo
 pyautogui.moveTo(3192, 827) # move para a escolha de página do Word
 pyautogui.click(clicks = 2)
 pyautogui.press('backspace')
 pyautogui.write('t')
 pyautogui.press('enter') # até aqui seleciona a página
 pyautogui.moveTo(3863,310) # move para dentro da pág selecionada
 pyautogui.click(clicks = 2)
 pyautogui.hotkey('ctrl','v') # copia o arquivo na página
 pyautogui.moveTo(671, 413)  # mover para a tela das plaquinhas
 pyautogui.click(clicks=2)
 pyautogui.press('right')
 pyautogui.hotkey('shift', 'winleft', 's')
 pyautogui.moveTo(949, 273)
 pyautogui.mouseDown()
 pyautogui.moveTo(1398, 909)
 pyautogui.mouseUp()  # até aqui, recortar a plaquinha no tamanho certo
 pyautogui.moveTo(3192, 827)  # move para a escolha de página do Word
 pyautogui.click(clicks=2)
 pyautogui.press('backspace')
 pyautogui.write('t')
 pyautogui.press('enter')  # até aqui seleciona a página
 pyautogui.moveTo(3863, 310)  # move para dentro da pág selecionada
 pyautogui.click(clicks=2)
 pyautogui.hotkey('ctrl', 'v')  # copia o arquivo na página
 pyautogui.moveTo(671,413) # mover para a tela das plaquinhas
 pyautogui.click(clicks=2)
 pyautogui.press('enter') # até aqui seleciona a página
 t = t + 1

pyautogui.alert('O código terminou')