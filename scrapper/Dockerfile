FROM python:3.11

WORKDIR /home/app/OzonScrapper

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#RUN apk update
#RUN apk upgrade
#RUN apk add netcat-openbsd && apk add postgresql-dev gcc python3-dev musl-dev

RUN apt update && apt upgrade
RUN apt install gcc

RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

#ENTRYPOINT ["sh", "/home/app/Scrapper/entrypoint.sh"]

CMD ["tail", "-f", "/dev/null"]