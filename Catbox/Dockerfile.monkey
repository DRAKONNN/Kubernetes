FROM python:3
COPY monkeybox.py /app/monkeybox.py
WORKDIR /app
CMD ["python", "monkeybox.py"]