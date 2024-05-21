import pyautogui
import time

print("Posicione o mouse sobre o botão de compra e espere 5 segundos...")
time.sleep(5)
buy_position = pyautogui.position()
print(f"Posição do botão de compra: {buy_position}")

print("Posicione o mouse sobre o botão de venda e espere 5 segundos...")
time.sleep(5)
sell_position = pyautogui.position()
print(f"Posição do botão de venda: {sell_position}")
