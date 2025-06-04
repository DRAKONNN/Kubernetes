import time
import random

# Definir los tipos de gato
gatos = {
    "normal": "🐱 Miau!",
    "miedoso": "🙀 Miaaauu!",
    "triste": "😿 Meu...",
    "amoroso": "😻 Maauu"
}

# Elegir un tipo de gato aleatoriamente
tipo_gato = random.choice(list(gatos.keys()))
mensaje_gato = gatos[tipo_gato]

print(f"Tipo de gato 2.2.3 seleccionado: {tipo_gato}")

# Bucle infinito que imprime el mensaje del gato seleccionado
while True:
    print(mensaje_gato, flush=True)
    time.sleep(random.randint(3, 9))