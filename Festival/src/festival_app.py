from flask import Flask
import os

app = Flask(__name__)

# Lista de artistas del festival
artists = [
    "Coldplay",
    "Rosalía",
    "The Rolling Stones",
    "Dua Lipa",
    "Kendrick Lamar",
    "Arctic Monkeys"
]

@app.route('/')
def get_artists():
    # Mostrar el nombre del pod (para demostrar el balanceo de carga)
    pod_name = os.getenv('HOSTNAME', 'unknown-pod')
    artists_str = ", ".join(artists)
    return f"<h1>Artistas del Festival 2023</h1><p>{artists_str}</p><p>Served by: {pod_name}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)