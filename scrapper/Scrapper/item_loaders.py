from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader


def price_serializer(value: str) -> str:
    return float(value.replace("$", ""))


def year_serializer(value: str) -> int | None:
    return None if value == "0" else int(value)


def country_serializer(value: str) -> str | None:
    return None if value == "Unknown" else value


class RecordLoader(ItemLoader):
    default_output_processor = TakeFirst()

    cd_usd_price_in = MapCompose(price_serializer)

    vinyl_usd_price_in = MapCompose(price_serializer)

    release_year_in = MapCompose(year_serializer)

    country_in = MapCompose(country_serializer)
