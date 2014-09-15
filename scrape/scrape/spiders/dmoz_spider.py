import scrapy
import re
from scrapy.http import FormRequest
from scrapy.http import Request
from scrape.items import DmozItem
import unicodedata

class DmozSpider(scrapy.Spider):
    name = "dmoz"
   
    allowed_domains = ["linkedin.com"]
    start_urls=['https://www.linkedin.com/uas/login']
    # start_urls = [
    #     "http://www.linkedin.com/profile/view?id=99333136"
    # ]
    def parse(self, response):
        return [FormRequest.from_response(response,
                    formdata={'session_key': '', 'session_password': ''},#linkedin login
                    callback=self.after_login)]
    def after_login(self, response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.log("Login failed", level=log.ERROR)
            return
        else:
            lines = open('../../../urlList.txt').read().splitlines()
            for line in lines:
                request=Request(url=line,
               callback=self.parse_tastypage)
                # request.meta['item'] = item
                yield request
    def parse_tastypage(self, response):
        f = open('../../../emailList','a')
        
        item = DmozItem()

        email=re.search("\{\"email\":\"(.[^\"]*)",response.body).group(1)
        name=re.search("\"fmt__full_name\":\"(.[^\"]*)",response.body).group(1)
        company=re.search("\"companyName\":\"(.[^\"]*)",response.body).group(1)
        f.write(email+", "+name+", "+company+"\n")
        f.close()
        item['email'] = email

        return item

    # def parse(self, response):
    #     for sel in response.xpath('//ul/li'):
    #         item = DmozItem()
    #         item['email'] = sel.xpath('div[@id=\'email-view\']/ul/li/a/@href').extract()
    #         yield item

