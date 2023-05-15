# Scrapper
Scrapy + Playwright + PostgreSQL + FastAPI scrapper example

## Review
It's an example of dockerized dynamic site (reactstorefront.vercel.app) web-scrapper, with backend made with FastAPI for handy fetching data.

## Intstallation
1. Copy project - 
    ```commandline
    git clone https://github.com/Wesson1337/Scrapper
    ```
3. Istall docker - https://docs.docker.com/engine/install/
4. Set up env variables (check environment variables paragraph).
5. Build up containers from root directory of the project.
    ```commandline
    docker compose up --build
    ```
4. Go to "localhost:8000/docs" in your browser.

## Environment variables
To use application you should create .env files in root directory of the project.
You should write down into it next variables:
- POSTGRES_DB - name of database, example: "postgres"
- POSTGRES_HOST - host of your db, default - "db"
- POSTGRES_PASSWORD - db password
- POSTGRES_USER - db user, example: "postgres"
- POSTGRES_PORT - db port, default - "5432"
