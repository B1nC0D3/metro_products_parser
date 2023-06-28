import unicodedata

from scrapy import spiders
from scrapy.linkextractors import LinkExtractor
from metro_crawler.items import MetroProductItem
from metro_crawler.settings import (ITEM_ID_XPATH, ITEM_NAME_XPATH, PRICE_XPATH,
                                    ITEM_BRAND_XPATH, PRODUCTS_XPATH, NAV_XPATH)


class CheeseSpider(spiders.CrawlSpider):
    name = "cheese_spider"
    allowed_domains = ('online.metro-cc.ru',)
    start_urls = (
        'https://online.metro-cc.ru/category/molochnye-prodkuty-syry-i-yayca/syry?in_stock=1',)

    rules = (
        spiders.Rule(LinkExtractor(restrict_xpaths=(NAV_XPATH,), unique=True),
                     callback='_requests_to_follow'),
        spiders.Rule(LinkExtractor(restrict_xpaths=(PRODUCTS_XPATH,), unique=True),
                     callback='parse_item'),
    )

    def parse_item(self, response):
        item_id_string = response.xpath(ITEM_ID_XPATH).get()
        item_id = item_id_string.split(':')[-1].strip()
        item_name = response.xpath(ITEM_NAME_XPATH).get().strip()
        raw_prices = response.xpath(PRICE_XPATH).getall()
        prices = [unicodedata.normalize('NFKC', i) for i in raw_prices]
        if len(prices) == 1:
            prices.append('Не выставлена')
        common_price, promo_price = prices[0], prices[1]
        item_brand = response.xpath(ITEM_BRAND_XPATH).get().strip()
        yield MetroProductItem(
                item_id=item_id,
                item_name=item_name,
                item_url=response.url,
                common_price=common_price,
                promo_price=promo_price,
                item_brand=item_brand)
