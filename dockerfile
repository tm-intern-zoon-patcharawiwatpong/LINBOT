FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirement.txt

EXPOSE 8000

ENV ENV_FILE=".env"

CMD ["python", "main.py"]