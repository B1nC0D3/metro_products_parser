import scrapy


class MetroProductItem(scrapy.Item):
    item_id = scrapy.Field()
    item_name = scrapy.Field()
    item_url = scrapy.Field()
    common_price = scrapy.Field()
    promo_price = scrapy.Field()
    item_brand = scrapy.Field()
