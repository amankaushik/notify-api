from implementation import HackerNewsAPIImpl
from ConfigParser import SafeConfigParser
import json
from models import  NewsItem
import io

def wiriteJSONToFile(self, filename, collection):
		print('Writing Stories to File ...')
		with open(filename, 'w', encoding='utf8') as outF:
			for item in collection:
				json.dump(item.__dict__, outF)
		print('Stories written to file')


def refreshNewsData(refreshType='all'):
	hackerNewsAPIImpl = HackerNewsAPIImpl()
	config = SafeConfigParser()
	# config.readfp(io.BytesIO('config.ini'))
	config.read('config.ini')
	# hnProperty = config.get('hackernews')

	# storyBaseUrl = config.get("hackernews", "storyBaseUrl")
	# responseFormat = config.get('hackernews', 'fromat')
	# topStoriesBaseUrl = config.get('hackernews', 'topStoriesBaseUrl')
	# limit = int(config.get('default', 'hnLimit'))
	storyBaseUrl = 'https://hacker-news.firebaseio.com/v0/item/'
	responseFormat = '.json'
	topStoriesBaseUrl = 'https://hacker-news.firebaseio.com/v0/topstories'
	limit = 5
	newIds = set(hackerNewsAPIImpl.getStoryIDs(topStoriesBaseUrl, responseFormat, limit))
	oldIds = set(NewsItem.objects.all().values_list('itemId', flat=True))
	updates = newIds.intersection(oldIds)
	inserts = newIds.difference(updates)
	deletes = oldIds.difference(updates)

	NewsItem.objects.filter(itemId__in=list(deletes))
	allStories = hackerNewsAPIImpl.getStories(list(inserts), storyBaseUrl, responseFormat)
	NewsItem.objects.bulk_create(allStories)
	NewsItem.objects.filter(itemId__in=list(updates)).update(isNew=False)
