from html.parser import HTMLParser  
from urllib.request import urlopen  
from urllib import parse
import re

class LinkParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    newUrl = parse.urljoin(self.baseUrl, value)
                    self.links += [newUrl]

    def get_links(self, url):
        self.links = []
        self.baseUrl = url
        response = urlopen(url)
        if response.getheader('Content-Type')=='text/html':
            htmlString = response.read().decode("utf-8")
            self.feed(htmlString)
            return self.links
        else:
            return[]



def sents_with_python(page):
        pattern = r"([^.]*Python[^.]*\.)"
        python_parser = PythonParser(pattern)
        with urlopen(page) as data:
            python_parser.feed(data.read().decode('utf-8'))
            sentences = python_parser.sentences
        return "\n\nNA %s ZNALEZIONO:\n" % page + '\n\n'.join(sentences)


class PythonParser(HTMLParser):
    def __init__(self, pattern):
        super().__init__()
        self.regex = re.compile(pattern)
        self.sentences = []

    def handle_data(self, data):
        self.sentences.extend(map(str.strip, self.regex.findall(data)))

def crawl(start_page, distance, action):  
    pages_to_visit = [start_page]
    visited = set()
    number_of_visited = 0
    while number_of_visited < distance and pages_to_visit != []:
        tmp = []
        for url in pages_to_visit:
            if url not in visited:
                visited.add(url)
            else:
                continue
            try:
                print("Level:",number_of_visited, " Visiting:", url)
                parser = LinkParser()
                links = parser.get_links(url)
                yield action(url)
                tmp += links
            except:
                print(" **Failed!**")
        number_of_visited +=1
        pages_to_visit = tmp


sp = crawl('https://www.ii.uni.wroc.pl/~marcinm/dyd/python/', 2, sents_with_python)
for s in sp:
    print(s)
