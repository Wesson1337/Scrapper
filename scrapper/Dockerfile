FROM python:3.11

WORKDIR /home/app/Scrapper

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt update && apt upgrade -y
RUN apt install gcc netcat -y

RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN playwright install && playwright install-deps

COPY . .

ENTRYPOINT ["sh", "/home/app/Scrapper/entrypoint.sh"]