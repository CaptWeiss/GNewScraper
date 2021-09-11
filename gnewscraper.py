from pygooglenews import GoogleNews
from outputs import output_json
import argparse


def parse_args():
	parser = argparse.ArgumentParser(description='Google News Scraper')
	parser.add_argument('-k', '--keyword', default='top_news', help='Enter Keyword')
	parser.add_argument('-n', '--name', default='output', help='json file name of where you would want result to be saved')
	args = vars(parser.parse_args())

	return search_news(args)


def search_news(args):
    # default GoogleNews instance
    gn = GoogleNews(lang='en', country='US')

    keyword = args['keyword'].strip()
    name = args['name'].strip()

    if keyword=='top_news':
        print('scraping top news of the day')
        top_news = gn.top_news()
        return output_json(top_news,name)

    print('scraping search word or phrase')
    data = gn.search(keyword)
    return output_json(data, name)


if __name__ == '__main__':
    parse_args()
