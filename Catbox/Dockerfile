FROM python:3.10-slim

WORKDIR /app

# Copiar primero solo los archivos de dependencias
COPY requirements.txt .

# Instalar dependencias primero (esto se cachea)
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código (esto invalida cache si cambia algo como catbox.py)
COPY . .

CMD ["python", "catbox.py"]
