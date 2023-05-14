echo "Waiting for postgres..."

while ! nc -z db "$POSTGRES_PORT"; do
  sleep 0.1
done

echo "PostgreSQL started"

while true; do
  echo "Starting crawling"
  scrapy crawl records_spider;
  echo "Crawling is done, sleeping for 12 hours"
  sleep 12h;
done