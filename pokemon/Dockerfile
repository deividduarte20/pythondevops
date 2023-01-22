FROM python:3.8-slim-buster

WORKDIR /app
COPY api_poke.py /app
COPY requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD [ "python3", "./api_poke.py" ]