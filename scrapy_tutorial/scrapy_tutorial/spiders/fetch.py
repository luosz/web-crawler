# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 20:44:47 2018
https://doc.scrapy.org/en/latest/intro/tutorial.html
@author: hasee
"""

import scrapy
from unidecode import unidecode

class FetchSpider(scrapy.Spider):
    name = "fetch"
    count = 0
    start_urls = ["https://www.glassdoor.com/Interview/Accenture-Australia-Interview-Questions-EI_IE4138.0,9_IL.10,19_IN16.htm", "https://www.glassdoor.com/Interview/Accenture-Australia-Interview-Questions-EI_IE4138.0,9_IL.10,19_IN16_IP2.htm", "https://www.glassdoor.com/Interview/Accenture-Australia-Interview-Questions-EI_IE4138.0,9_IL.10,19_IN16_IP3.htm", "https://www.glassdoor.com/Interview/Accenture-Australia-Interview-Questions-EI_IE4138.0,9_IL.10,19_IN16_IP4.htm", "https://www.glassdoor.com/Interview/Accenture-Australia-Interview-Questions-EI_IE4138.0,9_IL.10,19_IN16_IP5.htm", "https://www.glassdoor.com/Interview/Accenture-Australia-Interview-Questions-EI_IE4138.0,9_IL.10,19_IN16_IP6.htm", "https://www.glassdoor.com/Interview/Accenture-Australia-Interview-Questions-EI_IE4138.0,9_IL.10,19_IN16_IP7.htm", "https://www.glassdoor.com/Interview/Accenture-Australia-Interview-Questions-EI_IE4138.0,9_IL.10,19_IN16_IP8.htm", "https://www.glassdoor.com/Interview/Accenture-Australia-Interview-Questions-EI_IE4138.0,9_IL.10,19_IN16_IP9.htm", "https://www.glassdoor.com/Interview/Accenture-Australia-Interview-Questions-EI_IE4138.0,9_IL.10,19_IN16_IP10.htm", "https://www.glassdoor.com/Interview/Accenture-Australia-Interview-Questions-EI_IE4138.0,9_IL.10,19_IN16_IP11.htm", "https://www.glassdoor.com/Interview/Accenture-Australia-Interview-Questions-EI_IE4138.0,9_IL.10,19_IN16_IP12.htm", "https://www.glassdoor.com/Interview/Accenture-Australia-Interview-Questions-EI_IE4138.0,9_IL.10,19_IN16_IP13.htm"]

    def parse(self, response):
        items = response.xpath('//*/div[3]/div/div[2]/div[2]/div/div/ul/li/span/text()').extract()
        for d in items:
            self.count += 1
            data = {'q': unidecode(d), 'id': self.count, 'page': response.url.split(',')[-1].split('.')[0]}
            yield data
