# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RecordItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    cd_usd_price = scrapy.Field()
    vinyl_usd_price = scrapy.Field()
    release_type = scrapy.Field()
    artist = scrapy.Field()
    artist_page = scrapy.Field()
    genre = scrapy.Field()
    release_year = scrapy.Field()
    label = scrapy.Field()
    country = scrapy.Field()

