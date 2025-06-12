FROM python:3.10-slim

WORKDIR /app

# Instalar dependencias primero (esto se cachea)
RUN pip install flask

# Copiar el resto del código (esto invalida cache si cambia algo como el python)
COPY . .

CMD ["python", "src/festival_app.py"]