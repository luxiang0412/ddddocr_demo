FROM python:3.9.18-slim-bookworm

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "main.py"]