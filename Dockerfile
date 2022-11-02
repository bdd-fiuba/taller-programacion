FROM python:3.10.2

WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install
COPY webserver/init.sh /app/init.sh

EXPOSE 8000

RUN chmod u+x /app/init.sh

ENTRYPOINT ["./init.sh"]
