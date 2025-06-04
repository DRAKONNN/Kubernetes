import time
import random
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

# Monkey types
monkeys = {
    "normal": "🐱 Miau!",
    "miedoso": "🙀 Miaaauu!",
    "triste": "😿 Meu...",
    "amoroso": "😻 Maauu"
}

# Elegir un tipo de gato aleatoriamente por pod
monkey_type = random.choice(list(monkeys.keys()))
monkey_message = monkeys[monkey_type]
hostname = socket.gethostname()

print(f"Monkey type 2.1.1 selected: {monkey_type}", flush=True)

class CatHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        respuesta = f"{monkey_message} desde {hostname} (tipo: {monkey_type})"
        self.wfile.write(respuesta.encode())

if __name__ == '__main__':
    server = HTTPServer(('', 8080), CatHandler)
    print(f"Servidor monkeybox iniciado en el puerto 8080 en {hostname}", flush=True)
    server.serve_forever()
