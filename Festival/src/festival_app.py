from flask import Flask
import os

app = Flask(__name__)

# Lista de artistas del festival
artists = [
    "MUSE",
    "OLIVIA RODRIGO",
    "30 SECONDS TO MARS",
    "ARDE BOGOTA",
    "WEEZER",
    "ROYAL OTIS"
]

@app.route('/')
def get_artists():
    # Mostrar el nombre del pod (para demostrar el balanceo de carga)
    pod_name = os.getenv('HOSTNAME', 'unknown-pod')
    artists_str = " | ".join(artists)
    return f"Festival 2025: {artists_str} Served by: {pod_name}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)