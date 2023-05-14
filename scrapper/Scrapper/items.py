# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


def price_serializer(value: str) -> str:
    return float(value.replace("$", ""))


def year_serializer(value: str) -> int | None:
    return None if value == "0" else int(value)


def country_serializer(value: str) -> str | None:
    return None if value == "Unknown" else value


class RecordItem(scrapy.Item):
    name = scrapy.Field()
    cd_usd_price = scrapy.Field(serializer=price_serializer)
    vinyl_usd_price = scrapy.Field(serializer=price_serializer)
    release_type = scrapy.Field()
    artist = scrapy.Field()
    artist_page = scrapy.Field()
    genre = scrapy.Field()
    release_year = scrapy.Field(serializer=year_serializer)
    label = scrapy.Field()
    country = scrapy.Field(serializer=country_serializer)

