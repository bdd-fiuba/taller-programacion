FROM python:3.9-bullseye

WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN apt install git -y
RUN pip install --upgrade pip \
    && pip install poetry

RUN poetry install

COPY . .

EXPOSE 9000

ENTRYPOINT ["poetry", "run", "uvicorn", "webserver.main:app", "--reload", "--host", "0.0.0.0", "--port", "9000"]
