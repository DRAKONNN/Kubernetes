FROM python:3.10-slim

WORKDIR /app

# Instalar dependencias primero (esto se cachea)
RUN pip install flask

# Copiar el resto del código (esto invalida cache si cambia algo como catbox.py)
COPY . .

CMD ["python", "src/app.py"]