import logging

import playwright.async_api
# import playwright.async_api
# import time

# import requests
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_playwright.page import PageMethod

from ..items import PromoItem


# import scrapy
# from scrapy_playwright.page import PageMethod
#
# from ..items import PromoItem

# logging.getLogger('scrapy-playwright').setLevel(level=logging.WARNING)


# class PromoSpider(scrapy.Spider):
#     name = "promo_spider"
#
#     def start_requests(self):
#         yield scrapy.Request(
#             'https://www.ozon.ru/highlight/globalpromo/',
#             meta=dict(
#                 playwright=True,
#                 playwright_page_methods=[
#                     PageMethod("wait_for_selector", "div[data-widget='objectBannerList']"),
#                     PageMethod("wait_for_selector", "div[data-widget='banner']"),
#                     PageMethod("wait_for_selector", "div[data-widget='objectGrid']")
#                 ]
#             ),
#             callback=self.parse_first
#         )
#
#     def parse_first(self, response: scrapy.http.Response):
#         for url in response.css(
#                 "div[data-widget='objectGrid'] a, div[data-widget='banner'] a, div[data-widget='objectBannerList'] a"):
#             yield scrapy.Request(
#                 response.urljoin(url.attrib["href"]),
#                 meta=dict(
#                     playwright=True,
#                     playwright_page_methods=[
#                         PageMethod("wait_for_timeout", 10000),
#                         PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)"),
#                         PageMethod("wait_for_selector", "div[data-widget='resultsHeader'], div[data-widget='sellerTransparency'], div[data-widget='meta']"
#                                    )
#                     ]
#                 ),
#                 callback=self.parse_second,
#                 errback=self.errback
#             )
#
#     def parse_second(self, response: scrapy.http.Response):
#         item = PromoItem()
#         yield {"url": response.url}
#
#     def errback(self, failure):
#         logging.getLogger('scrapy-playwright').error(failure)


# class PromoSpider(scrapy.Spider):
#     name = "promo_spider"
# 
#     def start_requests(self):
#         yield scrapy.Request(
#             f'https://www.litres.ru/pages/new_genres/',
#             callback=self.parse_first
#         )
# 
#     def parse_first(self, response: scrapy.http.response):
#         for url in response.css('a'):
#             if url.attrib.get("href") and url.attrib.get("href").startswith("/genre/"):
#                 for i in range(10):
# 
#                     yield scrapy.Request(
#                         f'{response.urljoin(url.attrib["href"])}?page={i}',
#                         # meta=dict(
#                         #     playwright=True,
#                         #     playwright_page_methods=[
#                         #         PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)"),
#                         #         PageMethod("wait_for_selector", 'h1[itemprop="name"]')
#                         #     ],
#                         # ),
#                         callback=self.parse_second
#                     )
# 
#     async def parse_second(self, response: scrapy.http.response):
#         pass


# class PromoSpider(scrapy.Spider):
#     name = "promo_spider"
#
#     def start_requests(self):
#         yield scrapy.Request(
#             'https://www.scrapethissite.com/pages/ajax-javascript/',
#             meta=dict(
#                 playwright=True,
#                 playwright_goto_kwargs={
#                     "wait_until": "commit"
#                 },
#                 playwright_page_methods=[
#                     # PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)"),
#                     # PageMethod("wait_for_selector", 'a.year-link-active')
#                 ],
#                 playwright_include_page=True
#             ),
#             callback=self.parse_first
#         )
#
#     async def parse_first(self, response):
#         page: playwright.async_api.Page = response.meta["playwright_page"]
#         await page.wait_for_load_state(timeout=0)
#
#         for link in await page.locator("year-link").all():
#             await link.click()
#             await page.locator("table.table").wait_for(state="visible")
#             await page.locator("td.film-title").wait_for()
#             yield {"page": page.locator("td.film-title").all()}
#
#
#         count = 0
#         for url in response.css('a'):
#             if count >= 20:
#                 break
#             if not url.attrib["href"].startswith("/await.php?"):
#                 yield scrapy.Request(
#                     response.urljoin(url.attrib["href"]),
#                     meta=dict(
#                         playwright=True,
#                         playwright_page_methods=[
#                             # PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)"),
#                             PageMethod("wait_for_selector", 'h1[itemprop="name"]')
#                         ],
#                     ),
#                     callback=self.parse
#                 )
#                 count += 1
#
#
#     async def parse(self, response, **kwargs):
#         return {"url": response.url}



# class PromoSpider(scrapy.spiders.CrawlSpider):
#     name = "promo_spider"
#     allowed_domains = ["litres.ru"]
#     start_urls = ["http://www.litres.ru/"]
#     rules = (
#         Rule(LinkExtractor(allow=)),
#         Rule(LinkExtractor(allow=['/book/', '/audiobook/']), callback="parse_item"),
#     )
#
#     def parse_item(self, response):
#         yield {"url": response.url}



class PromoSpider(scrapy.Spider):
    name = "promo_spider"

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
        item = PromoItem()
        item['name'] = response.css('h1[data-testid="productName"]::text').get()

        return item





