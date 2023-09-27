FROM python:3.9-bullseye

WORKDIR /client

RUN apt install git -y
RUN pip install --upgrade pip \
    && pip install poetry
ENV PATH="${PATH}:/root/.local/bin"

COPY . .
RUN poetry install

ENTRYPOINT [ "tail" "-f", "/dev/null" ]
