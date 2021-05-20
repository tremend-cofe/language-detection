FROM python:3.8-slim-buster

RUN apt-get update &&  apt-get install -y --no-install-recommends \
  g++

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


RUN apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
&& rm -rf /var/lib/apt/lists/*

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
