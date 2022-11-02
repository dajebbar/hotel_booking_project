FROM python:3.9-slim

ENV PYTHONUNBUFFERED=TRUE

RUN pip --no-cache-dir install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --deploy --system && rm -rf /root/.cache

COPY ["predict.py", "*.bin", "./"]

EXPOSE $PORT

CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT predict:app
