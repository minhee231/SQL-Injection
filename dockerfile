FROM python:3.11-alpine

WORKDIR /app

COPY . /app

RUN pip3 install --no-cache-dir -r requirements.txt

#포트지정
ENV FLASK_RUN_PORT=134

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]