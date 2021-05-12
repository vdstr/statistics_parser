from collections import defaultdict
from pprint import pprint

from bs4 import BeautifulSoup, NavigableString
import re

with open('source/messages.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

statistics = defaultdict(int)
texts = soup.html.find_all(attrs={'class': 'text'})
for text in texts:
    if 'Статистика по домашним работам' in text.text:
        for content in text.contents:
            if isinstance(content, NavigableString) and (res := re.findall(r'(\d{2}.\d{2}): (\d*)', content)):
                date = res[0][0]
                value = int(res[0][1])
                if statistics[date] < value:
                    statistics[date] = value
print(sum(statistics.values()))
pprint(statistics)
