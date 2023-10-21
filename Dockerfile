FROM python:3.12.0-alpine3.17

COPY main.py run.sh requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

ENTRYPOINT [ "/app/run.sh" ]