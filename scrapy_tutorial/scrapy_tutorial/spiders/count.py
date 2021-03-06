# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 20:44:47 2018
https://doc.scrapy.org/en/latest/intro/tutorial.html
@author: hasee
"""

import scrapy
import json
import fileinput

class CountSpider(scrapy.Spider):
    name = "count"
    count = 0
    _url = 'https://www.glassdoor.com/Interview/Google-Australia-Interview-Questions-EI_IE9079.0,6_IL.7,16_IN16.htm'

    def __init__(self, url=None, *args, **kwargs):
        super(CountSpider, self).__init__(*args, **kwargs)
        self.log(url)
        if url is not None:
        	self._url = url

    def start_requests(self):
        urls = [
            self._url
        ]
        for u in urls:
            yield scrapy.Request(url=u, callback=self.parse)

    def parse(self, response):
        # Get item number from texts e.g. '94 Candidate Interview Reviews' and generate URLs for other pages
        text = response.xpath('//*[@id="MainCol"]/div[3]/div[1]/div[1]/h2/text()').extract_first()
        self.log(text)
        text_list = text.split()
        if(len(text_list) > 0):
            c = int(int(text_list[0]) / 10)
            url_list = [self._url.replace('.htm', '_IP{0}.htm'.format(i)) for i in range(2, c+2)]
            url_list.insert(0, self._url)
            json_str = json.dumps(url_list)
            
            # Replace the URLs in the spider file. Note the URLs must be written in one line.
            pattern = 'start_urls = ['
            spider_file = "scrapy_tutorial/spiders/fetch.py"
            self.log(spider_file)
            self.log(pattern)
            for line in fileinput.FileInput(spider_file, inplace=1):
                if pattern in line:
                    idx = line.find('[')
                    print(line[0:idx] + json_str)
                else:
                    print(line.rstrip('\r\n'))
            
            yield {'count': text, 'URLs': json_str}

    def spider_closed(self, spider):
        spider.logger.info('Spider closed: %s', spider.name)
