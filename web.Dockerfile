FROM ubuntu:18.04

RUN apt update \
    && apt install -y software-properties-common \
    && apt install -y python3.7 \
    && apt install -y python3-pip

# for 'pip3 install psycopg2'
RUN apt install -y libpq-dev python-dev

# Prevents python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1
ENV PATH /usr/local/bin:$PATH

# set working directory
RUN mkdir /online_store
WORKDIR /online_store

COPY requirements.txt /online_store/
RUN pip3 install -r requirements.txt
COPY . /online_store/
