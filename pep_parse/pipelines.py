# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import datetime as dt
from itemadapter import ItemAdapter
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


class PepParsePipeline:
    results = {}
    total = 0

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.results[item['status']] = self.results.get(item['status'], 0) + 1
        self.total += 1
        return item
    
    def close_spider(self, spider):
        format = "%Y-%m-%dT%H-%M-%S"
        time = dt.datetime.now().strftime(format)
        filename = BASE_DIR / 'results' / f'status_summary_{time}.csv'

        with open(filename, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for key, value in self.results.items():
                f.write(f'{key},{value}\n')
            f.write(f"total,{self.total}\n")

