FROM python:3.11.7
RUN mkdir /code2
WORKDIR /code2
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src .
COPY pyproject.toml .
