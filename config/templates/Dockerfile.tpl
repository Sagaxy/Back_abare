FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN echo pwd && ls -la
COPY .env /app
COPY src /app
RUN echo pwd && ls -la

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "(PORT)"]