import playwright.async_api
import scrapy
from scrapy_playwright.page import PageMethod

from ..item_loaders import RecordLoader
from ..items import RecordItem


class RecordsSpider(scrapy.Spider):
    name = "records_spider"

    def start_requests(self):
        yield scrapy.Request(
            'https://reactstorefront.vercel.app/default-channel/en-US/category/records/',
            meta=dict(
                playwright=True,
                playwright_include_page=True,
                playwright_page_methods=[
                    PageMethod('wait_for_selector', 'button.relative.text-base')
                ]
            ),
            callback=self.parse_first
        )

    async def parse_first(self, response: scrapy.http.Response):
        page: playwright.async_api.Page = response.meta["playwright_page"]
        while True:
            button = page.locator('button.relative.text-base')
            if (await button.count()) == 0:
                break
            await button.click()
            for url in await page.locator('a').all():
                href = await url.get_attribute('href')
                if href.startswith('/default-channel/en-US/products/'):
                    yield scrapy.Request(
                        response.urljoin(href),
                        callback=self.parse_item
                    )

    def parse_item(self, response: scrapy.http.Response):
        loader = RecordLoader(item=RecordItem(), response=response)
        loader.add_value("url", response.url)
        loader.add_css('name', 'h1[data-testid="productName"]::text')

        prices = response.css('div.flex.flex-row.gap-2.w-full.font-semibold.text-md>div:nth-child(2)::text').getall()
        loader.add_value("cd_usd_price", prices[0])
        loader.add_value("vinyl_usd_price", prices[1])

        attributes = []
        for attribute in response.css('div[class="grid grid-cols-2"]>div:nth-child(even)'):
            text_of_attribute = ' '.join(attribute.css("p::text").getall())
            attributes.append(text_of_attribute)

        loader.add_value("release_type", attributes[0])
        loader.add_value("artist", attributes[1])
        loader.add_value("artist_page", attributes[2])
        loader.add_value("genre", attributes[3])
        loader.add_value("release_year", attributes[4])
        loader.add_value("label", attributes[5])
        loader.add_value("country", attributes[6])

        return loader.load_item()
