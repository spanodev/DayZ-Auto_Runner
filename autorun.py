import keyboard
from pynput import mouse
import tkinter as tk
import threading
import time

# Estado inicial
holding = False

# Atualiza o label na interface
def update_status():
    if holding:
        status_label.config(text="Ativado: Segurando W + SHIFT", fg="green")
    else:
        status_label.config(text="Desativado", fg="red")

# Função chamada no clique do mouse
def on_click(x, y, button, pressed):
    global holding
    if button == mouse.Button.x2 and pressed:  # Botão lateral do mouse (MouseButton5)
        holding = not holding  # alterna estado

        if holding:
            keyboard.press("w")
            keyboard.press("shift")
            print("Segurando W + SHIFT")
        else:
            keyboard.release("w")
            keyboard.release("shift")
            print("Soltou W + SHIFT")

        # Atualiza interface
        update_status()
        time.sleep(0.3)  # evita múltiplos cliques seguidos

# Rodar listener em uma thread separada
def start_listener():
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

# ----- Interface gráfica -----
root = tk.Tk()
root.title("Macro W + SHIFT")
root.geometry("300x120")
root.resizable(False, False)

status_label = tk.Label(root, text="Desativado", font=("Arial", 14), fg="red")
status_label.pack(pady=30)

# Inicia o listener do mouse em paralelo
thread = threading.Thread(target=start_listener, daemon=True)
thread.start()

root.mainloop()
