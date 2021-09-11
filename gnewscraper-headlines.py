import os
from pygooglenews import GoogleNews
from outputs import output_json
import argparse

topics = ["WORLD", "NATION", "BUSINESS", "TECHNOLOGY", "ENTERTAINMENT", "SCIENCE", "SPORTS", "HEALTH" ]

def parse_args():
    parser = argparse.ArgumentParser(description='Google News Scraper')
    parser.add_argument('-t', '--topic', default='TECHNOLOGY', help='Enter headline topic')
    parser.add_argument('-n', '--name', default='output', help='json file name of where you would want result to be saved')
    args = vars(parser.parse_args())

    if args['topic'].strip().upper() not in topics:
        print(f" key word must be any of {topics}")
        return

    return search_news(args)

def search_news(args):
    # default GoogleNews instance
    gn = GoogleNews(lang='en', country='US')

    topic = args['topic'].strip().upper()
    name = args['name'].strip()

    print('scraping search word or phrase')
    data = gn.topic_headlines(topic)
    return output_json(data, name)


if __name__ == '__main__':
    parse_args()
