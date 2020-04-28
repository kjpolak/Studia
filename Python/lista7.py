import urllib.request
from bs4 import BeautifulSoup
from bs4.element import Comment
import re
from multiprocessing import Pool,cpu_count 

def gethrefs(url):
    hrefs = []
    try:
        uf = urllib.request.urlopen(url)
    except urllib.request.HTTPError as e:
        print(f'Failed at {url}: {e}')
        return
    html = uf.read()
    soup = BeautifulSoup(html, "html.parser")
    for a in soup.find_all('a', href=True):
        if(a['href'].startswith('http')):
            hrefs.append(str(a['href']))
    return hrefs

def visible(tag):
    if isinstance(tag, Comment):
        return False
    if tag.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    return True

def words_from_site(url):
    words_on_site = {}
    try:
        uf = urllib.request.urlopen(url)
        html = uf.read()
        soup = BeautifulSoup(html, "html.parser")
        texts = soup.findAll(text=True)
        visible_texts = filter(visible, texts)
        tmp = " ".join(t.strip() for t in visible_texts)
        text = [re.sub(r'\W+', '', t) for t in tmp.lower().split()]
        for word in text:
            if word in words_on_site:
                words_on_site[word]+=1
            else:
                words_on_site[word]=1
        return [url, words_on_site]
    except:
        return [url, {}]
    

def indexer(url, k):
    cores = cpu_count()
    hrefset = [url]
    levelset = [url]
    level = 0
    while level<k:
        new_level_sites =[]
        p = Pool(cores)
        new_sites = p.map(gethrefs, levelset)
        p.terminate()
        p.join()
        for e in new_sites:
            new_level_sites +=e
            hrefset +=e
        levelset= new_level_sites
        level+=1
    p = Pool(cores)
    dicts= p.map(words_from_site, hrefset)
    p.terminate()
    p.join()
    DICT = {}
    for url, diki in dicts:
        for word in diki:
            if word in DICT:
                DICT[word].append((url, diki[word]))
            else:
                DICT[word] = [(url, diki[word])]
    for word in DICT:
        tmp = sorted(DICT[word], key=lambda x: x[1], reverse = True)
        DICT[word] = [url for url, i in tmp]
    return DICT
    
if __name__ == "__main__":
    d = indexer('https://www.ii.uni.wroc.pl/~marcinm/dyd/python/',1)
    print(d['python'])
