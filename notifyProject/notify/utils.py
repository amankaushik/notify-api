'''
Utils module
'''
import json
from notify.implementation import HackerNewsAPIImpl
#from ConfigParser import SafeConfigParser
from notify.models import  NewsItem
#import io


def wirite_json_to_file(filename, collection):
    '''
    Write JSON data to file
    '''
    print 'Writing Stories to File ...'
    with open(filename, 'w', encoding='utf8') as out_f:
        for item in collection:
            json.dump(item.__dict__, out_f)
    print 'Stories written to file'


def refresh_news_data():
    '''
    Refresh db
    '''
    hacker_news_api_impl = HackerNewsAPIImpl()
    story_base_url = 'https://hacker-news.firebaseio.com/v0/item/'
    response_format = '.json'
    top_stories_base_url = 'https://hacker-news.firebaseio.com/v0/topstories'
    limit = 5
    new_ids = set(hacker_news_api_impl.getStoryIDs(top_stories_base_url,
                                                   response_format, limit))
    old_ids = set(NewsItem.objects.all().values_list('itemId', flat=True))
    updates = new_ids.intersection(old_ids)
    inserts = new_ids.difference(updates)
    deletes = old_ids.difference(updates)

    NewsItem.objects.filter(itemId__in=list(deletes)).delete()
    all_stories = hacker_news_api_impl.getStories(list(inserts), story_base_url,
                                                  response_format)
    NewsItem.objects.bulk_create(all_stories)
    NewsItem.objects.filter(itemId__in=list(updates)).update(isNew=False)

'''
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
'''
