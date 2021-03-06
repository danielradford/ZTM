# Web scraper built using Beautiful Soup
# Takes articles from Hacker News webpage and saves ones with over 100 up votes.
# Will then change page and repeat. 






import requests 
from bs4 import BeautifulSoup
import pprint



res = requests.get('https://news.ycombinator.com/news')

soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def sort_stories_by_votes(hnlist):
    return (sorted(hnlist, key = lambda k:k['votes'], reverse = True))

def create_custom_hn(links, subtext):
    hn=[]
    for idx,item in enumerate(links):
        
        title = links[idx].getText()
        href = links[idx].get('href',None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points > 99:
                hn.append({'title':title, 'link':href,  'votes' : points})
        
    return sort_stories_by_votes(hn)

def next_page():
    print('-> Next page results')
    more = soup.select('.morelink')
    href = more[0].get('href',None)
    res = requests.get('https://news.ycombinator.com/'+ href)
    next_soup = BeautifulSoup(res.text, 'html.parser')
    next_links = next_soup.select('.storylink')
    next_subtext = next_soup.select('.subtext')
    
    return create_custom_hn(next_links, next_subtext)

pprint.pprint(create_custom_hn(links, subtext))

pprint.pprint(next_page())

