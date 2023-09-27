FROM python:3.9-bullseye

WORKDIR /app/webserver

RUN pip install --upgrade pip \
    && pip install poetry

COPY . .

RUN poetry config virtualenvs.in-project false
RUN poetry install -v
RUN chmod +x entrypoint.sh

EXPOSE 9000

ENTRYPOINT ["./entrypoint.sh"]
