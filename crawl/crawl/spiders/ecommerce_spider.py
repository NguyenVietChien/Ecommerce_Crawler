import scrapy
from scrapy.crawler import CrawlerProcess
from twisted.internet import reactor
from ..items import CrawlItem
from scrapy.utils.project import get_project_settings

class EcommerceSpiderSpider(scrapy.Spider):
    name = 'tiki'
    page_number = 2
    keyword = 'đồ+ăn'
    url = 'https://tiki.vn/search?q=' + keyword
    start_urls = [
        url
    ]

    def parse(self, response):
        items = CrawlItem() 
        product = response.css("a.product-item") # Save div of items from web to scrape
        # Save details from item
        for responses in product:
            product_name = responses.css("h3::text").extract();
            product_discount = responses.css(".price-discount__discount::text").getall();
            product_link = "https://tiki.vn"+ str(responses.attrib['href'])
            product_price = responses.css(".price-discount__price").css("::text").get();
            
            product_review_rating_point = response.css(".review-rating__point::text").get();
            product_comments = response.css(".review-rating__total::text").get()
            product_review_rating_5_star = response.xpath('//*[@id="__next"]/div[1]/main/div[3]/div[4]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div[3]/text()').get()
            product_review_rating_4_star = response.xpath('//*[@id="__next"]/div[1]/main/div[3]/div[4]/div/div[2]/div[1]/div[1]/div/div[2]/div[2]/div[3]/text()').get()
            product_review_rating_3_star = response.xpath('//*[@id="__next"]/div[1]/main/div[3]/div[4]/div/div[2]/div[1]/div[1]/div/div[2]/div[3]/div[3]/text()').get()
            product_review_rating_2_star = response.xpath('//*[@id="__next"]/div[1]/main/div[3]/div[4]/div/div[2]/div[1]/div[1]/div/div[2]/div[4]/div[3]/text()').get()
            product_review_rating_1_star = response.xpath('//*[@id="__next"]/div[1]/main/div[3]/div[4]/div/div[2]/div[1]/div[1]/div/div[2]/div[5]/div[3]/text()').get()
            # Store data into item.
            items['product_link'] = product_link
            items['product_name'] = product_name
            items['product_price'] = int(product_price.replace("₫", "").replace(".", "").replace(" ", ""))
            items['product_discount'] = product_discount
            yield items

        numpage = str(EcommerceSpiderSpider.page_number)
        
        print(numpage+ "------------------------------------------------")
        next_page = EcommerceSpiderSpider.url + "&page=" + numpage
        if EcommerceSpiderSpider.page_number < 4:
            EcommerceSpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)

#Run Scrapy from a script
# process = CrawlerProcess(get_project_settings())
# process.crawl('tiki', domain='tiki.vn')
# process.start() # the script will block here until the crawling is finished
