from scrapy.http import HtmlResponse
import undetected_chromedriver as uc
from time import sleep


class SeleniumMiddleware:

    def __init__(self):
        options = uc.ChromeOptions()
        options.headless = True
        chrome_prefs = {}
        options.experimental_options['prefs'] = chrome_prefs
        chrome_prefs['profile.default_content_settings'] = {'images': 2}
        chrome_prefs['profile.managed_default_content_settings'] = {'images': 2}
        self.driver = uc.Chrome(options=options, use_subprocess=True)

    def process_request(self, request, spider):
        self.driver.get(request.url)
        content = self.driver.page_source
        return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)
