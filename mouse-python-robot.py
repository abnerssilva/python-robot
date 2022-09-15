import pyautogui
from time import sleep

n = int(input("Quantos minutos vc quer que o robo atue?: "))
h = n * 10
counter = 0
while counter <= h:
    if counter != 0:
        if counter % 10 == 0:
            if counter / 10 == 1:
                print(f"Ja se passou aproximadamente 1 minuto dos {n} solicitados.")
            else:    
                print(f"Ja se passaram aproximadamente {counter/10:.0f} minutos dos {n} solicitados.")
    else:
        print(f"Iniciando contagem de {n} minutos.")
    pyautogui.move(0, 50, duration=1)
    pyautogui.move(50, 0, duration=1)
    pyautogui.move(0, -50, duration=1)
    pyautogui.move(-50, 0, duration=1)
    pyautogui.click()
    sleep(0.25)
    counter += 1
print(f"Fim de {n} minutos solicitados.")
pyautogui.keyDown("alt")
pyautogui.press("tab")
pyautogui.keyUp("alt")
