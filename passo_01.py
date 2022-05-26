import pyautogui
import time


# print(pyautogui.KEYBOARD_KEYS)
# print(pyautogui.position())

pyautogui.alert('O código vai começar, não toque na máquina')
pyautogui.PAUSE = 0.7

time.sleep(0.7)

t = int(1)

while t < 4:
 pyautogui.hotkey('shift', 'winleft', 's')
 pyautogui.moveTo(949, 275)
 pyautogui.mouseDown()
 pyautogui.moveTo(1397, 909)
 pyautogui.mouseUp() # até aqui, recortar a plaquinha no tamanho certo
 pyautogui.moveTo(3734,322) # move para dentro da pág selecionada
 pyautogui.click(clicks = 2)
 pyautogui.hotkey('ctrl','v') # copia o arquivo na página
 pyautogui.moveTo(671,413) # mover para a tela das plaquinhas
 pyautogui.click(clicks=2)
 pyautogui.press('right')
 pyautogui.hotkey('shift', 'winleft', 's')
 pyautogui.moveTo(949,275)
 pyautogui.mouseDown()
 pyautogui.moveTo(1397, 909)
 pyautogui.mouseUp() # até aqui, recortar a plaquinha no tamanho certo
 pyautogui.moveTo(3734,322) # move para dentro da pág selecionada
 pyautogui.click(clicks = 2)
 pyautogui.hotkey('ctrl','v') # copia o arquivo na página
 pyautogui.moveTo(671,413) # mover para a tela das plaquinhas
 pyautogui.click(clicks=2)
 pyautogui.press('right')
 pyautogui.hotkey('shift', 'winleft', 's')
 pyautogui.moveTo(949,275)
 pyautogui.mouseDown()
 pyautogui.moveTo(1397, 909)
 pyautogui.mouseUp() # até aqui, recortar a plaquinha no tamanho certo
 pyautogui.moveTo(3734,322) # move para dentro da pág selecionada
 pyautogui.click(clicks = 2)
 pyautogui.hotkey('ctrl','v') # copia o arquivo na página
 pyautogui.moveTo(671, 413)  # mover para a tela das plaquinhas
 pyautogui.click(clicks=2)
 pyautogui.press('right')
 pyautogui.hotkey('shift', 'winleft', 's')
 pyautogui.moveTo(949, 275)
 pyautogui.mouseDown()
 pyautogui.moveTo(1397, 909)
 pyautogui.mouseUp()  # até aqui, recortar a plaquinha no tamanho certo
 pyautogui.moveTo(3734,322)  # move para dentro da pág selecionada
 pyautogui.click(clicks=2)
 pyautogui.hotkey('ctrl', 'v')  # copia o arquivo na página
 time.sleep(0.9)
 pyautogui.moveTo(3213, 826)  # move para a escolha de página do Word
 time.sleep(0.9)
 pyautogui.click(clicks = 3)
 time.sleep(0.9)
 pyautogui.press('backspace')
 time.sleep(0.9)
 pyautogui.write('+1')
 time.sleep(0.9)
 pyautogui.press('enter') # até aqui seleciona a página
 time.sleep(0.9)
 pyautogui.moveTo(671, 413)  # mover para a tela das plaquinhas
 pyautogui.click(clicks=2)
 pyautogui.press('right')
 t = t + 1

pyautogui.alert('O código terminou')