# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#import json

class ScrapyTutorialPipeline(object):

    def process_item(self, item, spider):
#        self.file.write(json.dumps(dict(item)) + "\n")
        return item
    
    def open_spider(self, spider):
#        self.file = open('dumps.json', 'w')
        pass

    def close_spider(self, spider):
#        self.file.close()
        pass
