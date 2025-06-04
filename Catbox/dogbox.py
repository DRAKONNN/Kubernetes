import time
import random

# Definir los tipos de gato
dogs = {
    "adorable": "🐶 Borf!",
    "serious": "🐺 Woof"
}

# Elegir un tipo de gato aleatoriamente
dog_type = random.choice(list(dogs.keys()))
mensaje_gato = dogs[dog_type]

print(f"Dog type 2.1.1 selected: {dog_type}")

# Bucle infinito que imprime el mensaje del gato seleccionado
while True:
    print(mensaje_gato, flush=True)
    time.sleep(random.randint(3, 9))