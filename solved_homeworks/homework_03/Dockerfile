# docker run -it -P app

FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY app.py .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host=0.0.0.0" ,"--port=8000"]